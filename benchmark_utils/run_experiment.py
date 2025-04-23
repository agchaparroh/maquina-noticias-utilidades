#!/usr/bin/env python3

# run_experiment.py

import os
import json
import time
import logging
import asyncio
import csv
import re
import argparse
import sys
from pathlib import Path
from groq import AsyncGroq, GroqError, APITimeoutError, RateLimitError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from tqdm import tqdm # Usar tqdm normal para el bucle principal
from datetime import datetime, timezone
from typing import Optional, Tuple, Dict, Any, List


# --- Configuración y Argumentos ---
def parse_arguments() -> argparse.Namespace:
    """Parsea los argumentos de línea de comandos para el experimento."""
    parser = argparse.ArgumentParser(description="Ejecuta un experimento de evaluación de prompts con Groq.")
    parser.add_argument(
        "--exp-id",
        type=str,
        required=True,
        help="Identificador único para este experimento (ej. 'exp_01_llama3.1_prompts_v2')."
    )
    parser.add_argument(
        "--articles",
        nargs='+',
        required=True,
        help="Lista de IDs de artículos de prueba a procesar (ej. test_005 test_069 test_040)."
    )
    parser.add_argument(
        "--prompt-dir",
        type=Path,
        default=Path("./prompt_templates"),
        help="Directorio que contiene las plantillas de prompts (ej. 'relevancia.txt')."
    )
    parser.add_argument(
        "--model",
        type=str,
        default="llama3-8b-8192",
        help="ID del modelo Groq a utilizar en el experimento."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("../data/benchmark_test_set"),
        help="Directorio con los archivos JSON de artículos originales."
    )
    parser.add_argument(
        "--output-base-dir",
        type=Path,
        default=Path("./experiments"),
        help="Directorio base donde se crearán las carpetas de experimentos."
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="Temperatura para la generación del modelo."
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=4096,
        help="Máximo de tokens de completado."
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=7, # Aumentado por defecto
        help="Número máximo de reintentos por llamada API."
    )
    parser.add_argument(
        "--max-wait",
        type=int,
        default=120, # Aumentado por defecto
        help="Tiempo máximo de espera exponencial en segundos para reintentos."
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Timeout de la API de Groq en segundos."
    )
    return parser.parse_args()


# --- Constantes y Configuración Global ---
args = parse_arguments()

# Modelo a usar
MODEL_TO_USE = args.model

# Tareas a realizar
TASKS = [
    "relevancia", "extraccion_hechos", "extraccion_entidades",
    "extraccion_citas", "extraccion_datos"
]

# Directorios
INPUT_ARTICLES_DIR = args.input_dir
PROMPT_TEMPLATE_DIR = args.prompt_dir
OUTPUT_EXPERIMENT_DIR = args.output_base_dir / args.exp_id
METRICS_FILE = OUTPUT_EXPERIMENT_DIR / f"metricas_{args.exp_id}.csv"
MARKDOWN_FILE = OUTPUT_EXPERIMENT_DIR / f"informe_{args.exp_id}.md"

# Parámetros API
API_TEMPERATURE = args.temperature
API_MAX_TOKENS = args.max_tokens
API_TIMEOUT = args.timeout

# Parámetros de Reintento
MAX_RETRIES = args.retries
MAX_WAIT_SECONDS = args.max_wait

# Configuración de Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Definiciones de Taxonomía (para reemplazar en prompts) ---
TAXONOMY = {
    "LISTA_CATEGORIAS_PERMITIDAS": '["Política Nacional", "Política Internacional", "Economía", "Conflicto/Seguridad", "Justicia/Legal", "Sociedad/Derechos", "Análisis/Contexto", "Elecciones", "Diplomacia"]',
    "LISTA_TIPOS_HECHO": '["SUCESO", "ANUNCIO", "DECLARACION", "BIOGRAFIA", "CONCEPTO", "NORMATIVA", "EVENTO"]',
    "LISTA_PRECISION_TEMPORAL": '["exacta", "dia", "semana", "mes", "trimestre", "año", "decada", "periodo"]',
    "LISTA_TIPOS_ENTIDAD": '["PERSONA", "ORGANIZACION", "INSTITUCION", "LUGAR", "EVENTO", "NORMATIVA", "CONCEPTO", "OTRO"]',
    "LISTA_CATEGORIAS_DATOS": '["económico", "demográfico", "electoral", "social", "presupuestario", "sanitario", "ambiental", "conflicto", "otro"]',
    "LISTA_TIPOS_PERIODO": '["anual", "trimestral", "mensual", "semanal", "diario", "puntual", "acumulado"]'
}


# --- Funciones Auxiliares ---
def load_api_key() -> str:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        logger.error("Error: Variable de entorno GROQ_API_KEY no encontrada.")
        raise ValueError("GROQ_API_KEY no configurada")
    return api_key


def load_article(filepath: Path) -> Optional[Dict[str, Any]]:
    if not filepath.is_file():
        logger.error(f"Archivo de artículo no encontrado: {filepath}")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error cargando artículo {filepath.name}: {e}")
        return None


def load_prompt_template(prompt_dir: Path, tarea: str) -> Optional[str]:
    """Carga la plantilla de prompt para una tarea desde un archivo."""
    filepath = prompt_dir / f"{tarea}.txt"
    if not filepath.is_file():
        logger.error(f"Plantilla de prompt no encontrada: {filepath}")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error cargando plantilla {filepath.name}: {e}")
        return None


def _clean_json_string(raw_string: Optional[str]) -> Optional[str]:
    """Intenta extraer y reparar un bloque JSON de una cadena."""
    if not raw_string: return None
    json_match = re.search(r'^\s*(\{.*\}|\[.*\])\s*', raw_string, re.DOTALL)
    if json_match:
        potential_json = json_match.group(1)
        try: json.loads(potential_json); return potential_json
        except json.JSONDecodeError: logger.debug("JSON inicial no válido, intentando limpiar...")
    fixed_string = raw_string
    start_brace = fixed_string.find('{'); start_bracket = fixed_string.find('[')
    end_brace = fixed_string.rfind('}'); end_bracket = fixed_string.rfind(']')
    start_index = -1; end_index = -1
    if start_brace != -1 and end_brace != -1: start_index = start_brace; end_index = end_brace
    if start_bracket != -1 and end_bracket != -1:
        if start_index == -1 or start_bracket < start_index: start_index = start_bracket
        if end_index == -1 or end_bracket > end_index:
             if start_index == start_bracket: end_index = end_bracket
             elif end_bracket > end_brace: end_index = end_bracket
    if start_index != -1 and end_index != -1 and start_index < end_index: fixed_string = fixed_string[start_index : end_index + 1]
    else: logger.warning("No se pudo determinar un bloque JSON principal claro."); fixed_string = raw_string.strip()
    fixed_string = re.sub(r"(?<!\\)'\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*'\s*:", r'"\1":', fixed_string)
    fixed_string = re.sub(r'"cita":\s*""([^"]*?)""', r'"cita": "\1"', fixed_string)
    fixed_string = re.sub(r'\}(?=\s*,\s*"nombre":)', r'}, {', fixed_string)
    fixed_string = re.sub(r'\bNone\b', 'null', fixed_string)
    fixed_string = re.sub(r'\bTrue\b', 'true', fixed_string, flags=re.IGNORECASE)
    fixed_string = re.sub(r'\bFalse\b', 'false', fixed_string, flags=re.IGNORECASE)
    fixed_string = re.sub(r",\s*(\}|\])", r"\1", fixed_string)
    try:
        parsed = json.loads(fixed_string)
        if isinstance(parsed, (dict, list)): logger.info("JSON limpiado/reparado exitosamente."); return fixed_string
        else: logger.error(f"Contenido parseado no es un objeto o lista JSON válido: {type(parsed)}"); return None
    except json.JSONDecodeError as e:
        error_context = fixed_string[max(0, e.pos-20):min(len(fixed_string), e.pos+20)]
        logger.error(f"Falló la reparación del JSON: {e}. Contexto: ...{error_context}..."); return None


def format_json_for_markdown(data: Any) -> str:
    try: return f"```json\n{json.dumps(data, indent=4, ensure_ascii=False)}\n```"
    except Exception: return f"```\n{str(data)}\n```"


def format_seconds(seconds: Optional[float]) -> str:
    if seconds is None: return "N/A"
    minutes, secs = divmod(seconds, 60)
    return f"{int(minutes)}m {secs:.2f}s"


# --- Llamada a API y Procesamiento ---
RETRYABLE_ERRORS = (APITimeoutError, RateLimitError, GroqError)

# Crear decorador de reintento dinámicamente basado en argumentos
retry_decorator = retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_exponential(multiplier=2, min=10, max=MAX_WAIT_SECONDS), # Usar max_wait
    retry=retry_if_exception_type(RETRYABLE_ERRORS),
    reraise=True
)


@retry_decorator
async def llamar_groq_con_metricas(
    client: AsyncGroq,
    model_id: str,
    prompt: str,
    test_id: str,
    tarea: str
) -> Tuple[Optional[str], Dict[str, Any]]:
    """Llama a Groq, mide métricas, limpia, valida JSON y maneja errores/reintentos."""
    start_time = time.time()
    error_message: Optional[str] = None; api_success: bool = False; json_valid: bool = False
    response_content: Optional[str] = None; usage_data: Optional[Any] = None
    latency: float = 0.0; cleaned_content: Optional[str] = None

    try:
        logger.debug(f"[{test_id}][{tarea}][{model_id}] Llamando a Groq...")
        chat_completion = await client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model_id,
            temperature=API_TEMPERATURE,
            max_completion_tokens=API_MAX_TOKENS,
            response_format={"type": "json_object"},
            # El timeout se pasa al inicializar el cliente AsyncGroq
        )
        latency = time.time() - start_time
        response_content = chat_completion.choices[0].message.content
        usage_data = chat_completion.usage
        api_success = True
        logger.debug(f"[{test_id}][{tarea}][{model_id}] Éxito API.")

        if response_content:
            cleaned_content = _clean_json_string(response_content)
            if cleaned_content:
                try:
                    json_parsed = json.loads(cleaned_content)
                    if tarea != "relevancia":
                        if not isinstance(json_parsed, dict): raise ValueError("Respuesta no es objeto")
                        if "resultados" not in json_parsed: raise ValueError("Falta clave 'resultados'")
                        if not isinstance(json_parsed.get("resultados"), list): raise ValueError("'resultados' no es lista")
                    json_valid = True
                    logger.debug(f"[{test_id}][{tarea}][{model_id}] JSON válido y estructura OK.")
                except (json.JSONDecodeError, ValueError) as json_err:
                    logger.error(f"[{test_id}][{tarea}][{model_id}] Error validando JSON (limpio): {json_err}")
                    error_message = f"JSONValidationError: {json_err}"
                    cleaned_content = response_content # Guardar original si falla validación
            else:
                logger.error(f"[{test_id}][{tarea}][{model_id}] Error: No se pudo extraer/reparar bloque JSON.")
                error_message = "JSONCleanError: No JSON block found or repaired"
                cleaned_content = response_content
        else:
             logger.error(f"[{test_id}][{tarea}][{model_id}] API Success but empty content received")
             error_message = "API Success but empty content received"

    except Exception as e:
        latency = time.time() - start_time
        if isinstance(e, RateLimitError): error_message = f"RateLimitError: {str(e)}"; logger.warning(f"[{test_id}][{tarea}][{model_id}] Rate Limit: {e}")
        else: error_message = f"API_Error: {type(e).__name__}: {str(e)}"; logger.error(f"[{test_id}][{tarea}][{model_id}] Error API: {error_message}")
        api_success = False; json_valid = False

    success = api_success and json_valid
    metrics = {
        "test_id": test_id, "tarea": tarea, "model_id": model_id,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "latency_seconds": round(latency, 3),
        "prompt_tokens": usage_data.prompt_tokens if usage_data else None,
        "completion_tokens": usage_data.completion_tokens if usage_data else None,
        "total_tokens": usage_data.total_tokens if usage_data else None,
        "success": success, "api_success": api_success, "json_valid": json_valid,
        "error_message": error_message
    }
    content_to_return = cleaned_content if json_valid else response_content
    return content_to_return, metrics


def guardar_metricas_csv(metrics_list: List[Dict[str, Any]], csv_filepath: Path):
    """Guarda una lista de métricas en un archivo CSV."""
    if not metrics_list: return
    try:
        csv_filepath.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = list(metrics_list[0].keys()) # Usar claves del primer registro
        # Asegurar orden consistente si es posible
        ordered_fields = [
            "test_id", "tarea", "model_id", "timestamp_utc", "latency_seconds",
            "prompt_tokens", "completion_tokens", "total_tokens", "success",
            "api_success", "json_valid", "error_message"
        ]
        # Incluir todos los campos, poniendo los ordenados primero
        final_fieldnames = ordered_fields + [f for f in fieldnames if f not in ordered_fields]

        with open(csv_filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=final_fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(metrics_list)
        logger.info(f"Métricas guardadas en {csv_filepath}")
    except Exception as e:
        logger.error(f"Error guardando métricas CSV en {csv_filepath}: {e}", exc_info=True)


def generar_markdown_articulo(test_id: str, article_data: Dict[str, Any], results_by_task: Dict[str, Tuple[Optional[str], Dict[str, Any]]]) -> List[str]:
    """Genera la sección Markdown para un artículo."""
    md_lines: List[str] = []
    md_lines.append(f"\n## Artículo: {test_id}\n")

    # --- Metadatos ---
    md_lines.append("### Metadatos\n")
    md_lines.append("| Campo          | Valor                                      |")
    md_lines.append("|----------------|--------------------------------------------|")
    md_lines.append(f"| **URL**        | {article_data.get('url', 'N/A')}           |")
    md_lines.append(f"| **Título**     | {article_data.get('titular', 'N/A')}       |")
    md_lines.append(f"| **Medio**      | {article_data.get('medio', 'N/A')}         |")
    md_lines.append(f"| **País Pub.**  | {article_data.get('pais_publicacion', 'N/A')} |")
    md_lines.append(f"| **Fecha Pub.** | {article_data.get('fecha_publicacion', 'N/A')} |")
    md_lines.append("\n")

    # --- Contenido ---
    md_lines.append("### Contenido Analizado\n")
    contenido_texto = article_data.get('contenido_texto', '*Contenido no disponible*')
    md_lines.append("<details>")
    md_lines.append("<summary>Ver/Ocultar Contenido Completo</summary>\n")
    md_lines.append(f"```text\n{contenido_texto}\n```")
    md_lines.append("</details>\n")

    # --- Tabla Resumen Tareas ---
    md_lines.append("### Resumen de Tareas\n")
    md_lines.append("| Tarea | Estado | Modelo Utilizado | Tiempo | Tokens (P/C/T) | Error |")
    md_lines.append("|-------|--------|------------------|--------|----------------|-------|")
    for tarea in TASKS:
        content, metrics = results_by_task.get(tarea, (None, {}))
        estado = "✅" if metrics.get('success') else ("⚠️" if metrics.get('api_success') else "❌")
        modelo = metrics.get('model_id', 'N/A')
        tiempo = format_seconds(metrics.get('latency_seconds'))
        p_tokens = metrics.get('prompt_tokens', 'N/A')
        c_tokens = metrics.get('completion_tokens', 'N/A')
        t_tokens = metrics.get('total_tokens', 'N/A')
        tokens_str = f"{p_tokens}/{c_tokens}/{t_tokens}"
        error_msg = metrics.get('error_message', '') or ''
        # Acortar mensaje de error para tabla
        error_short = (error_msg[:30] + '...') if len(error_msg) > 30 else error_msg
        md_lines.append(f"| {tarea} | {estado} | `{modelo}` | {tiempo} | {tokens_str} | `{error_short}` |")
    md_lines.append("\n")

    # --- Resultados Detallados Tareas ---
    md_lines.append("### Resultados Detallados por Tarea\n")
    for tarea in TASKS:
        md_lines.append(f"#### Tarea: {tarea}\n")
        content, metrics = results_by_task.get(tarea, (None, {}))

        if not metrics: md_lines.append("_(No se procesó esta tarea)_"); continue

        estado_str = "Éxito" if metrics.get('success') else ("Fallo (JSON Inválido)" if metrics.get('api_success') else "Fallo (API Error)")
        md_lines.append(f"- **Estado:** {estado_str}")
        if metrics.get('error_message'): md_lines.append(f"- **Error:** `{metrics.get('error_message')}`")
        md_lines.append(f"- **Modelo:** `{metrics.get('model_id', 'N/A')}`")
        md_lines.append(f"- **Tiempo:** {format_seconds(metrics.get('latency_seconds'))}")
        md_lines.append(f"- **Tokens:** P:{metrics.get('prompt_tokens', 'N/A')} / C:{metrics.get('completion_tokens', 'N/A')} / T:{metrics.get('total_tokens', 'N/A')}")

        md_lines.append("\n<details open>")
        md_lines.append("<summary>Ver/Ocultar Respuesta LLM</summary>\n")
        if content:
            if metrics.get('json_valid'):
                try: md_lines.append(format_json_for_markdown(json.loads(content)))
                except json.JSONDecodeError: md_lines.append(f"_(Error parseando JSON para formateo):_\n```\n{content}\n```")
            else: md_lines.append(f"_(Respuesta no válida o estructura incorrecta):_\n```\n{content}\n```")
        else: md_lines.append("_No se recibió contenido del LLM._")
        md_lines.append("</details>\n")

    md_lines.append("\n---\n") # Separador entre artículos
    return md_lines


# --- Lógica Principal Asíncrona ---
async def procesar_articulo_experimental(
    client: AsyncGroq,
    article_path: Path,
    prompt_templates: Dict[str, str],
    model_to_use: str
) -> Tuple[str, Dict[str, Tuple[Optional[str], Dict[str, Any]]]]:
    """Procesa un artículo con todas las tareas secuencialmente."""
    test_id = article_path.stem
    logger.info(f"--- Procesando Artículo: {test_id} (Modelo: {model_to_use}) ---")
    results_by_task: Dict[str, Tuple[Optional[str], Dict[str, Any]]] = {}

    articulo = load_article(article_path)
    if not articulo:
        logger.error(f"No se pudo cargar el artículo {test_id}")
        # Registrar fallo para todas las tareas
        for tarea in TASKS:
             metrics = {"test_id": test_id, "tarea": tarea, "model_id": model_to_use, "success": False, "api_success": False, "json_valid": False, "error_message": "Article load failed"}
             results_by_task[tarea] = (None, metrics)
        return test_id, results_by_task

    # --- Preparar datos para reemplazo en prompts ---
    titulo = articulo.get("titular", "")
    contenido = articulo.get("contenido_texto", "")
    medio = articulo.get("medio", "Desconocido")
    pais = articulo.get("pais_publicacion", "Desconocido")
    fecha_pub_str = articulo.get("fecha_publicacion", "Fecha desconocida")
    try:
        if fecha_pub_str.endswith('Z'): fecha_pub_dt = datetime.fromisoformat(fecha_pub_str.replace('Z', '+00:00'))
        else: fecha_pub_dt = datetime.fromisoformat(fecha_pub_str)
        fecha_pub = fecha_pub_dt.date().isoformat()
    except: fecha_pub = fecha_pub_str
    contenido_extracto = contenido[:2000]

    prompt_data = {
        "TITULO": titulo, "CONTENIDO": contenido, "MEDIO": medio, "PAIS": pais,
        "FECHA_PUB": fecha_pub, "CONTENIDO_EXTRACTO": contenido_extracto,
        **{k: v for k, v in TAXONOMY.items()} # Añadir listas de taxonomía
    }
    # --- Fin preparación datos ---

    for tarea in TASKS:
        template = prompt_templates.get(tarea)
        if not template:
            logger.warning(f"[{test_id}][{tarea}] No se encontró plantilla de prompt.")
            metrics = {"test_id": test_id, "tarea": tarea, "model_id": model_to_use, "success": False, "api_success": False, "json_valid": False, "error_message": "Prompt template not found"}
            results_by_task[tarea] = (None, metrics)
            continue

        # Reemplazar placeholders en la plantilla
        prompt = template
        for key, value in prompt_data.items():
            placeholder = f"{{{{{key}}}}}" # Formato {{PLACEHOLDER}}
            prompt = prompt.replace(placeholder, str(value))

        try:
            content, metrics = await llamar_groq_con_metricas(client, model_to_use, prompt, test_id, tarea)
            results_by_task[tarea] = (content, metrics)
        except Exception as e:
             logger.error(f"[{test_id}][{tarea}][{model_to_use}] Error final procesando tarea: {e}")
             metrics = {"test_id": test_id, "tarea": tarea, "model_id": model_to_use, "success": False, "api_success": False, "json_valid": False, "error_message": f"Processing Error: {type(e).__name__}: {str(e)}"}
             results_by_task[tarea] = (None, metrics)

        await asyncio.sleep(0.2) # Pequeña pausa entre tareas

    logger.info(f"--- Artículo {test_id} completado ---")
    return test_id, results_by_task


async def main():
    """Función principal del script de experimentos."""
    start_time_script = time.time()
    logger.info(f"--- Iniciando Experimento: {args.exp_id} ---")
    logger.info(f"Modelo: {MODEL_TO_USE}, Artículos: {args.articles}")
    logger.info(f"Directorio de Prompts: {PROMPT_TEMPLATE_DIR}")
    logger.info(f"Directorio de Salida: {OUTPUT_EXPERIMENT_DIR}")

    # Crear directorio de salida para este experimento
    OUTPUT_EXPERIMENT_DIR.mkdir(parents=True, exist_ok=True)

    # Cargar API Key
    try: api_key = load_api_key()
    except ValueError: return 1
    client = AsyncGroq(api_key=api_key, timeout=API_TIMEOUT)
    logger.info("Cliente AsyncGroq inicializado.")

    # Cargar plantillas de prompt
    prompt_templates: Dict[str, str] = {}
    for tarea in TASKS:
        template = load_prompt_template(PROMPT_TEMPLATE_DIR, tarea)
        if not template:
            logger.error(f"No se pudo cargar la plantilla para la tarea '{tarea}'. Abortando.")
            return 1
        prompt_templates[tarea] = template
    logger.info(f"Cargadas {len(prompt_templates)} plantillas de prompt.")

    # Obtener rutas de los artículos a procesar
    article_paths: List[Path] = []
    for test_id in args.articles:
        # Asegurar formato test_XXX si solo se pasa número
        if test_id.isdigit(): test_id = f"test_{int(test_id):03d}"
        elif not test_id.startswith("test_"): test_id = f"test_{test_id}"
        path = INPUT_ARTICLES_DIR / f"{test_id}.json"
        if path.is_file(): article_paths.append(path)
        else: logger.warning(f"No se encontró el archivo para el artículo ID: {test_id}")

    if not article_paths:
        logger.error("No se especificaron artículos válidos para procesar.")
        return 1

    logger.info(f"Procesando {len(article_paths)} artículos...")

    all_markdown_content: List[str] = []
    all_metrics: List[Dict[str, Any]] = []

    # Añadir cabecera al Markdown del experimento
    all_markdown_content.append(f"# Informe del Experimento: {args.exp_id}")
    all_markdown_content.append(f"**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    all_markdown_content.append(f"**Modelo:** `{MODEL_TO_USE}`")
    all_markdown_content.append(f"**Artículos:** {', '.join(args.articles)}")
    all_markdown_content.append(f"**Directorio Prompts:** `{PROMPT_TEMPLATE_DIR}`")
    all_markdown_content.append("\n---\n")

    # Procesar artículos secuencialmente
    for article_path in tqdm(article_paths, desc="Procesando Artículos"):
        test_id, results_by_task = await procesar_articulo_experimental(
            client, article_path, prompt_templates, MODEL_TO_USE
        )

        # Cargar datos del artículo para el markdown
        article_data = load_article(article_path) or {}

        # Generar sección Markdown para este artículo
        article_md_section = generar_markdown_articulo(test_id, article_data, results_by_task)
        all_markdown_content.extend(article_md_section)

        # Recopilar métricas
        for _, metrics in results_by_task.values():
             if metrics: # Asegurarse de que hay métricas
                 all_metrics.append(metrics)

        await asyncio.sleep(0.5) # Pausa entre artículos

    # Guardar el informe Markdown completo
    try:
        with open(MARKDOWN_FILE, 'w', encoding='utf-8') as f:
            f.write("\n".join(all_markdown_content))
        logger.info(f"Informe Markdown guardado en: {MARKDOWN_FILE}")
    except Exception as e:
        logger.error(f"Error guardando informe Markdown: {e}")

    # Guardar las métricas CSV
    guardar_metricas_csv(all_metrics, METRICS_FILE)

    end_time_script = time.time()
    logger.info(f"--- Experimento {args.exp_id} Completado ---")
    logger.info(f"Resultados guardados en: {OUTPUT_EXPERIMENT_DIR.resolve()}")
    logger.info(f"Tiempo total de ejecución: {time.time() - start_time_script:.2f} segundos")
    return 0


# --- Punto de Entrada ---
if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)