#!/usr/bin/env python3

# run_pipeline_experiment.py (Versión Correcta con Paso de Datos)

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
from tqdm import tqdm
from datetime import datetime, timezone
from typing import Optional, Tuple, Dict, Any, List


# --- Configuración y Argumentos ---
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ejecuta un pipeline de prompts multi-paso con Groq.")
    parser.add_argument("--exp-id", type=str, required=True, help="ID único del experimento.")
    parser.add_argument("--articles", nargs='+', required=True, help="Lista de IDs de artículos (ej. test_005 test_069).")
    parser.add_argument("--prompt-dir", type=Path, default=Path("./prompt_templates_pipeline"), help="Directorio con plantillas (.txt).")
    parser.add_argument("--model", type=str, default="llama3-8b-8192", help="ID del modelo Groq.")
    parser.add_argument("--input-dir", type=Path, default=Path("../data/benchmark_test_set"), help="Directorio de artículos JSON.")
    parser.add_argument("--output-base-dir", type=Path, default=Path("./experiments"), help="Directorio base para resultados.")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-tokens", type=int, default=4096)
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--max-wait", type=int, default=60)
    parser.add_argument("--timeout", type=int, default=180)
    return parser.parse_args()


# --- Constantes y Configuración Global ---
args = parse_arguments()
MODEL_TO_USE = args.model
TASKS_PIPELINE = [
    "prompt_0_filtrado", "prompt_1_elementos_basicos", "prompt_2_citas_datos",
    "prompt_3_relaciones", "prompt_4_json_final"
]
INPUT_ARTICLES_DIR = args.input_dir
PROMPT_TEMPLATE_DIR = args.prompt_dir
OUTPUT_EXPERIMENT_DIR = args.output_base_dir / args.exp_id
METRICS_FILE = OUTPUT_EXPERIMENT_DIR / f"metricas_{args.exp_id}.csv"
MARKDOWN_FILE = OUTPUT_EXPERIMENT_DIR / f"informe_{args.exp_id}.md"
RAW_OUTPUT_DIR = OUTPUT_EXPERIMENT_DIR / "raw_outputs"

API_TEMPERATURE = args.temperature
API_MAX_TOKENS = args.max_tokens
API_TIMEOUT = args.timeout
MAX_RETRIES = args.retries
MAX_WAIT_SECONDS = args.max_wait

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
    if not api_key: raise ValueError("GROQ_API_KEY no configurada")
    return api_key


def load_article(filepath: Path) -> Optional[Dict[str, Any]]:
    if not filepath.is_file(): logger.error(f"Artículo no encontrado: {filepath}"); return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f: return json.load(f)
    except Exception as e: logger.error(f"Error cargando artículo {filepath.name}: {e}"); return None


def load_prompt_template(prompt_dir: Path, task_filename_base: str) -> Optional[str]:
    filepath = prompt_dir / f"{task_filename_base}.txt"
    if not filepath.is_file(): logger.error(f"Plantilla no encontrada: {filepath}"); return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f: return f.read()
    except Exception as e: logger.error(f"Error cargando plantilla {filepath.name}: {e}"); return None


def _clean_json_string(raw_string: Optional[str]) -> Optional[str]:
    if not raw_string: return None
    # Intenta encontrar el bloque JSON principal
    json_match = re.search(r'^\s*(\{.*\}|\[.*\])\s*$', raw_string, re.DOTALL)
    if json_match:
        potential_json = json_match.group(1)
        try:
            json.loads(potential_json)
            return potential_json # Ya es válido
        except json.JSONDecodeError:
            logger.debug("JSON inicial no válido, intentando limpiar...")
    # Si no, intenta extraer el primer { o [ hasta el último } o ]
    start_brace = raw_string.find('{')
    start_bracket = raw_string.find('[')
    end_brace = raw_string.rfind('}')
    end_bracket = raw_string.rfind(']')
    start_index = -1
    end_index = -1
    if start_brace != -1 and end_brace != -1: start_index = start_brace; end_index = end_brace
    if start_bracket != -1 and end_bracket != -1:
        if start_index == -1 or start_bracket < start_index: start_index = start_bracket
        if end_index == -1 or end_bracket > end_index:
            if start_index == start_bracket: end_index = end_bracket
            elif end_bracket > end_brace: end_index = end_bracket
    if start_index != -1 and end_index != -1 and start_index < end_index:
        potential_json = raw_string[start_index : end_index + 1]
        try:
            json.loads(potential_json) # Verificar si es parseable
            logger.info("JSON extraído exitosamente.")
            return potential_json
        except json.JSONDecodeError:
            logger.warning("Bloque JSON extraído no es válido. Intentando reparaciones...")
            # Continuar con reparaciones sobre 'potential_json'
            fixed_string = potential_json
    else:
        logger.warning("No se pudo determinar un bloque JSON principal claro. Intentando reparaciones sobre cadena original.")
        fixed_string = raw_string.strip()

    # Intentar reparaciones (simplificado para brevedad, usar versión robusta si es necesario)
    fixed_string = re.sub(r"(?<!\\)'\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*'\s*:", r'"\1":', fixed_string)
    fixed_string = re.sub(r'\bNone\b', 'null', fixed_string)
    fixed_string = re.sub(r'\bTrue\b', 'true', fixed_string, flags=re.IGNORECASE)
    fixed_string = re.sub(r'\bFalse\b', 'false', fixed_string, flags=re.IGNORECASE)
    fixed_string = re.sub(r",\s*(\}|\])", r"\1", fixed_string)
    try:
        parsed = json.loads(fixed_string)
        if isinstance(parsed, (dict, list)): logger.info("JSON reparado exitosamente."); return fixed_string
        else: logger.error(f"Contenido reparado no es objeto/lista JSON: {type(parsed)}"); return None
    except json.JSONDecodeError as e:
        logger.error(f"Falló la reparación del JSON: {e}."); return None


def format_json_for_markdown(data: Any) -> str:
    try: return f"```json\n{json.dumps(data, indent=4, ensure_ascii=False)}\n```"
    except Exception: return f"```\n{str(data)}\n```"


def format_seconds(seconds: Optional[float]) -> str:
    if seconds is None: return "N/A"
    minutes, secs = divmod(seconds, 60)
    return f"{int(minutes)}m {secs:.2f}s"


# --- Llamada a API ---
RETRYABLE_ERRORS = (APITimeoutError, RateLimitError, GroqError)
retry_decorator = retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_exponential(multiplier=2, min=5, max=MAX_WAIT_SECONDS),
    retry=retry_if_exception_type(RETRYABLE_ERRORS),
    reraise=True
)

@retry_decorator
async def llamar_groq_paso(
    client: AsyncGroq, model_id: str, prompt: str, test_id: str, paso_nombre: str
) -> Tuple[Optional[str], Dict[str, Any]]:
    start_time = time.time(); error_message: Optional[str] = None
    api_success: bool = False; json_valid: bool = False
    response_content: Optional[str] = None; usage_data: Optional[Any] = None
    latency: float = 0.0; cleaned_content: Optional[str] = None
    expect_json = paso_nombre != "prompt_0_filtrado"
    response_format = {"type": "json_object"} if expect_json else None

    try:
        logger.debug(f"[{test_id}][{paso_nombre}][{model_id}] Llamando...")
        chat_completion = await client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}], model=model_id,
            temperature=API_TEMPERATURE, max_completion_tokens=API_MAX_TOKENS,
            response_format=response_format)
        latency = time.time() - start_time
        response_content = chat_completion.choices[0].message.content
        usage_data = chat_completion.usage; api_success = True
        logger.debug(f"[{test_id}][{paso_nombre}][{model_id}] Éxito API.")
        if response_content:
            if expect_json:
                cleaned_content = _clean_json_string(response_content)
                if cleaned_content:
                    try: json.loads(cleaned_content); json_valid = True; logger.debug(f"[{test_id}][{paso_nombre}] JSON válido.")
                    except (json.JSONDecodeError, ValueError) as json_err:
                        error_message = f"JSONValidationError: {json_err}"; cleaned_content = response_content
                        logger.error(f"[{test_id}][{paso_nombre}] Error validando JSON: {json_err}")
                else: error_message = "JSONCleanError"; cleaned_content = response_content; logger.error(f"[{test_id}][{paso_nombre}] Error limpiando JSON.")
            else: json_valid = True; cleaned_content = response_content.strip()
        else: error_message = "API Success but empty content"
    except Exception as e:
        latency = time.time() - start_time
        if isinstance(e, RateLimitError): error_message = f"RateLimitError: {str(e)}"; logger.warning(f"[{test_id}][{paso_nombre}] Rate Limit: {e}")
        else: error_message = f"API_Error: {type(e).__name__}: {str(e)}"; logger.error(f"[{test_id}][{paso_nombre}] Error API: {error_message}")
        api_success = False; json_valid = False

    success = api_success and json_valid
    metrics = {"test_id": test_id, "tarea": paso_nombre, "model_id": model_id, "timestamp_utc": datetime.now(timezone.utc).isoformat(), "latency_seconds": round(latency, 3), "prompt_tokens": usage_data.prompt_tokens if usage_data else None, "completion_tokens": usage_data.completion_tokens if usage_data else None, "total_tokens": usage_data.total_tokens if usage_data else None, "success": success, "api_success": api_success, "json_valid": json_valid, "error_message": error_message}
    content_to_return = cleaned_content if json_valid else response_content
    return content_to_return, metrics


# --- Guardado de Métricas y Salidas ---
def guardar_metricas_csv_incremental(metrics: Dict[str, Any], csv_filepath: Path):
    try:
        csv_filepath.parent.mkdir(parents=True, exist_ok=True)
        write_header = not csv_filepath.exists() or csv_filepath.stat().st_size == 0
        fieldnames = ["test_id", "tarea", "model_id", "timestamp_utc", "latency_seconds", "prompt_tokens", "completion_tokens", "total_tokens", "success", "api_success", "json_valid", "error_message"]
        with open(csv_filepath, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            if write_header: writer.writeheader()
            writer.writerow(metrics)
    except Exception as e: logger.error(f"Error guardando métrica incremental: {e}", exc_info=True)


def guardar_raw_output(test_id: str, paso_nombre: str, output_data: Dict[str, Any]):
    try:
        step_output_dir = RAW_OUTPUT_DIR / test_id
        step_output_dir.mkdir(parents=True, exist_ok=True)
        filepath = step_output_dir / f"{paso_nombre}_output.json"
        with open(filepath, 'w', encoding='utf-8') as f: json.dump(output_data, f, indent=4, ensure_ascii=False)
    except Exception as e: logger.error(f"Error guardando salida cruda {test_id}-{paso_nombre}: {e}")


# --- Generación de Markdown ---
def generar_seccion_prompts(prompt_templates: Dict[str, str]) -> List[str]:
    md_lines = ["## Prompts Utilizados\n", "<details><summary>Ver/Ocultar Prompts</summary>\n"]
    for task_base_name, template in prompt_templates.items():
        md_lines.append(f"### Prompt: {task_base_name}\n")
        md_lines.append(f"```text\n{template}\n```\n")
    md_lines.extend(["</details>\n", "\n---\n"])
    return md_lines


def generar_markdown_articulo(test_id: str, article_data: Dict[str, Any], results_by_task: Dict[str, Tuple[Optional[str], Dict[str, Any]]]) -> List[str]:
    md_lines = [f"\n## Artículo: {test_id}\n", "### Metadatos\n", "| Campo          | Valor |", "|----------------|-------|"]
    md_lines.extend([f"| URL            | {article_data.get('url', 'N/A')} |", f"| Título         | {article_data.get('titular', 'N/A')} |", f"| Medio          | {article_data.get('medio', 'N/A')} |", f"| País Pub.      | {article_data.get('pais_publicacion', 'N/A')} |", f"| Fecha Pub.     | {article_data.get('fecha_publicacion', 'N/A')} |", "\n"])
    md_lines.extend(["### Contenido Analizado\n", "<details><summary>Ver/Ocultar Contenido</summary>\n", f"```text\n{article_data.get('contenido_texto', '*Contenido no disponible*')}\n```", "</details>\n"])
    md_lines.extend(["### Resumen de Tareas\n", "| Tarea | Estado | Modelo Utilizado | Tiempo | Tokens (P/C/T) | Error |", "|-------|--------|------------------|--------|----------------|-------|"])
    for paso_nombre in TASKS_PIPELINE:
        content, metrics = results_by_task.get(paso_nombre, (None, {}))
        estado = "✅" if metrics.get('success') else ("⚠️" if metrics.get('api_success') else "❌"); modelo = metrics.get('model_id', 'N/A'); tiempo = format_seconds(metrics.get('latency_seconds'))
        p, c, t = metrics.get('prompt_tokens', 'N/A'), metrics.get('completion_tokens', 'N/A'), metrics.get('total_tokens', 'N/A'); tokens_str = f"{p}/{c}/{t}"
        error_msg = metrics.get('error_message', '') or ''; error_short = (error_msg[:30] + '...') if len(error_msg) > 30 else error_msg
        md_lines.append(f"| {paso_nombre.replace('prompt_','')} | {estado} | `{modelo}` | {tiempo} | {tokens_str} | `{error_short}` |")
    md_lines.extend(["\n", "### Resultados Detallados por Tarea\n"])
    for paso_nombre in TASKS_PIPELINE:
        md_lines.append(f"#### Paso: {paso_nombre}\n")
        content, metrics = results_by_task.get(paso_nombre, (None, {}))
        if not metrics: md_lines.append("_(Este paso fue omitido o falló previamente)_\n"); continue
        estado_str = "Éxito" if metrics.get('success') else ("Fallo (JSON Inválido)" if metrics.get('api_success') else "Fallo (API Error)")
        md_lines.extend([f"- **Estado:** {estado_str}", f"- **Error:** `{metrics.get('error_message')}`" if metrics.get('error_message') else "- **Error:** Ninguno", f"- **Modelo:** `{metrics.get('model_id', 'N/A')}`", f"- **Tiempo:** {format_seconds(metrics.get('latency_seconds'))}", f"- **Tokens:** P:{metrics.get('prompt_tokens', 'N/A')} / C:{metrics.get('completion_tokens', 'N/A')} / T:{metrics.get('total_tokens', 'N/A')}", "\n<details open><summary>Ver/Ocultar Respuesta LLM</summary>\n"])
        if content:
            if paso_nombre == "prompt_0_filtrado": md_lines.append(f"```text\n{content}\n```")
            elif metrics.get('json_valid'):
                try: md_lines.append(format_json_for_markdown(json.loads(content)))
                except json.JSONDecodeError: md_lines.append(f"_(Error parseando JSON):_\n```\n{content}\n```")
            else: md_lines.append(f"_(Respuesta no válida):_\n```\n{content}\n```")
        else: md_lines.append("_No se recibió contenido del LLM._")
        md_lines.append("</details>\n")
    md_lines.append("\n---\n")
    return md_lines


# --- Lógica Principal del Pipeline ---
async def ejecutar_pipeline_articulo(
    client: AsyncGroq, article_path: Path, prompt_templates: Dict[str, str], model_to_use: str
) -> Dict[str, Tuple[Optional[str], Dict[str, Any]]]:
    """Ejecuta el pipeline completo de 5 pasos para un artículo."""
    test_id = article_path.stem
    resultados_pasos: Dict[str, Tuple[Optional[str], Dict[str, Any]]] = {}
    outputs_pasos_anteriores: Dict[str, Any] = {} # Guarda JSON parseado
    logger.info(f"--- Iniciando Pipeline para Artículo: {test_id} (Modelo: {model_to_use}) ---")
    articulo_data = load_article(article_path)
    if not articulo_data:
        logger.error(f"[{test_id}] No se pudo cargar el artículo, abortando pipeline.")
        for paso_nombre_completo in TASKS_PIPELINE:
             metrics = {"test_id": test_id, "tarea": paso_nombre_completo, "model_id": model_to_use, "success": False, "api_success": False, "json_valid": False, "error_message": "Article load failed"}
             resultados_pasos[paso_nombre_completo] = (None, metrics)
             guardar_metricas_csv_incremental(metrics, METRICS_FILE)
        return resultados_pasos

    prompt_common_data = { "TITULO": articulo_data.get("titular", ""), "CONTENIDO": articulo_data.get("contenido_texto", ""), "MEDIO": articulo_data.get("medio", "Desconocido"), "PAIS": articulo_data.get("pais_publicacion", "Desconocido"), "FECHA_PUB": "Fecha desconocida", "CONTENIDO_EXTRACTO": articulo_data.get("contenido_texto", "")[:2000], **{k: v for k, v in TAXONOMY.items()} }
    try:
        fp_str = articulo_data.get("fecha_publicacion", ""); fp_dt = datetime.fromisoformat(fp_str.replace('Z', '+00:00')) if fp_str.endswith('Z') else datetime.fromisoformat(fp_str); prompt_common_data["FECHA_PUB"] = fp_dt.date().isoformat()
    except: pass

    for paso_index, paso_nombre_completo in enumerate(TASKS_PIPELINE):
        paso_nombre_base = paso_nombre_completo.replace("prompt_", "")
        logger.info(f"[{test_id}] Iniciando Paso {paso_index}: {paso_nombre_completo}")
        template = prompt_templates.get(paso_nombre_base)
        if not template:
            logger.error(f"[{test_id}][{paso_nombre_completo}] No se encontró plantilla."); metrics = {"test_id": test_id, "tarea": paso_nombre_completo, "model_id": model_to_use, "success": False, "api_success": False, "json_valid": False, "error_message": "Prompt template not found"}; resultados_pasos[paso_nombre_completo] = (None, metrics); guardar_metricas_csv_incremental(metrics, METRICS_FILE)
            # Detener pipeline si falta plantilla
            logger.warning(f"[{test_id}] Deteniendo pipeline por falta de prompt."); break

        # Construir prompt inyectando datos JSON de pasos anteriores
        prompt = template; paso_input_data = {**prompt_common_data}
        if paso_nombre_completo == "prompt_2_citas_datos": json_paso_1 = outputs_pasos_anteriores.get("prompt_1_elementos_basicos"); paso_input_data["JSON_PASO_1"] = json.dumps(json_paso_1, indent=2, ensure_ascii=False) if json_paso_1 else "{}"
        elif paso_nombre_completo == "prompt_3_relaciones": json_paso_1 = outputs_pasos_anteriores.get("prompt_1_elementos_basicos"); json_paso_2 = outputs_pasos_anteriores.get("prompt_2_citas_datos"); paso_input_data["JSON_PASO_1"] = json.dumps(json_paso_1, indent=2, ensure_ascii=False) if json_paso_1 else "{}"; paso_input_data["JSON_PASO_2"] = json.dumps(json_paso_2, indent=2, ensure_ascii=False) if json_paso_2 else "{}"
        elif paso_nombre_completo == "prompt_4_json_final": json_paso_1 = outputs_pasos_anteriores.get("prompt_1_elementos_basicos"); json_paso_2 = outputs_pasos_anteriores.get("prompt_2_citas_datos"); json_paso_3 = outputs_pasos_anteriores.get("prompt_3_relaciones"); paso_input_data["JSON_PASO_1"] = json.dumps(json_paso_1, indent=2, ensure_ascii=False) if json_paso_1 else "{}"; paso_input_data["JSON_PASO_2"] = json.dumps(json_paso_2, indent=2, ensure_ascii=False) if json_paso_2 else "{}"; paso_input_data["JSON_PASO_3"] = json.dumps(json_paso_3, indent=2, ensure_ascii=False) if json_paso_3 else "{}"
        for key, value in paso_input_data.items(): placeholder = f"{{{{{key}}}}}"; prompt = prompt.replace(placeholder, str(value))

        try:
            content, metrics = await llamar_groq_paso(client, model_to_use, prompt, test_id, paso_nombre_completo)
            resultados_pasos[paso_nombre_completo] = (content, metrics)
            guardar_metricas_csv_incremental(metrics, METRICS_FILE) # Guardar métrica
            output_data_to_save = {"prompt_used": prompt, "llm_response": content, "metrics": metrics}; guardar_raw_output(test_id, paso_nombre_completo, output_data_to_save)

            if metrics.get("success"):
                logger.info(f"[{test_id}][{paso_nombre_completo}] Completado exitosamente.")
                if metrics.get("json_valid") and paso_nombre_completo != "prompt_0_filtrado":
                    try: outputs_pasos_anteriores[paso_nombre_completo] = json.loads(content) # Guardar JSON parseado
                    except json.JSONDecodeError: logger.warning(f"[{test_id}][{paso_nombre_completo}] JSON válido pero falló al parsear para el siguiente paso.")
                elif paso_nombre_completo == "prompt_0_filtrado" and "DESCARTAR" in content.upper():
                    logger.info(f"[{test_id}] Artículo descartado en Paso 0. Deteniendo pipeline."); break
            else:
                 logger.warning(f"[{test_id}][{paso_nombre_completo}] Falló. Deteniendo pipeline."); break

        except Exception as e:
             logger.error(f"[{test_id}][{paso_nombre_completo}] Error inesperado: {e}", exc_info=True)
             metrics = {"test_id": test_id, "tarea": paso_nombre_completo, "model_id": model_to_use, "success": False, "api_success": False, "json_valid": False, "error_message": f"Pipeline Error: {type(e).__name__}: {str(e)}"}
             resultados_pasos[paso_nombre_completo] = (None, metrics)
             guardar_metricas_csv_incremental(metrics, METRICS_FILE)
             break # Detener pipeline en error inesperado

        await asyncio.sleep(0.3) # Pausa entre pasos

    # Rellenar métricas para pasos omitidos si el pipeline se detuvo
    pasos_ejecutados = set(resultados_pasos.keys())
    for paso_omitido in TASKS_PIPELINE:
        if paso_omitido not in pasos_ejecutados:
             metrics = {"test_id": test_id, "tarea": paso_omitido, "model_id": model_to_use, "success": False, "api_success": False, "json_valid": False, "error_message": "Pipeline stopped in previous step"}
             resultados_pasos[paso_omitido] = (None, metrics)
             guardar_metricas_csv_incremental(metrics, METRICS_FILE)

    logger.info(f"--- Pipeline para Artículo {test_id} finalizado ---")
    return resultados_pasos


async def main():
    start_time_script = time.time()
    logger.info(f"--- Iniciando Experimento Pipeline: {args.exp_id} ---")
    # (Resto de la función main sin cambios significativos,
    #  solo asegura que llama a guardar_metricas_csv_incremental dentro del bucle
    #  o que recopila todas las métricas y las guarda al final con guardar_metricas_csv)
    # ... [Código de main como en la versión anterior, asegurando que las métricas
    #      se recopilen de los resultados de ejecutar_pipeline_articulo y se guarden] ...

    OUTPUT_EXPERIMENT_DIR.mkdir(parents=True, exist_ok=True)
    RAW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Limpiar archivo de métricas anterior si existe
    if METRICS_FILE.exists(): logger.info(f"Eliminando métricas anteriores: {METRICS_FILE}"); METRICS_FILE.unlink()

    try: api_key = load_api_key()
    except ValueError: return 1
    client = AsyncGroq(api_key=api_key, timeout=API_TIMEOUT)
    logger.info("Cliente AsyncGroq inicializado.")

    prompt_templates: Dict[str, str] = {}
    for paso_nombre_completo in TASKS_PIPELINE:
        task_base_name = paso_nombre_completo
        template = load_prompt_template(PROMPT_TEMPLATE_DIR, task_base_name)
        if not template: logger.error(f"Falta plantilla {task_base_name}.txt"); return 1
        prompt_templates[task_base_name.replace("prompt_", "")] = template
    logger.info(f"Cargadas {len(prompt_templates)} plantillas.")

    article_paths: List[Path] = []
    for test_id_input in args.articles:
        test_id = test_id_input
        if test_id.isdigit(): test_id = f"test_{int(test_id):03d}"
        elif not test_id.startswith("test_"): test_id = f"test_{test_id}"
        path = INPUT_ARTICLES_DIR / f"{test_id}.json"
        if path.is_file(): article_paths.append(path)
        else: logger.warning(f"No se encontró archivo para ID: {test_id_input}")
    if not article_paths: logger.error("No hay artículos válidos."); return 1
    logger.info(f"Procesando {len(article_paths)} artículos...")

    all_markdown_content: List[str] = []
    results_all_articles: Dict[str, Dict[str, Any]] = {}

    # Cabecera del Informe
    all_markdown_content.extend([f"# Informe del Experimento (Pipeline): {args.exp_id}", f"**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", f"**Modelo:** `{MODEL_TO_USE}`", f"**Artículos:** {', '.join(args.articles)}", f"**Directorio Prompts:** `{PROMPT_TEMPLATE_DIR}`", "\n---\n"])
    all_markdown_content.extend(generar_seccion_prompts(prompt_templates))

    # Procesar artículos secuencialmente
    for article_path in tqdm(article_paths, desc="Procesando Artículos"):
        try:
            pipeline_results = await ejecutar_pipeline_articulo(client, article_path, prompt_templates, MODEL_TO_USE)
            test_id = article_path.stem
            results_all_articles[test_id] = pipeline_results
            article_data = load_article(article_path) or {}
            article_md_section = generar_markdown_articulo(test_id, article_data, pipeline_results)
            all_markdown_content.extend(article_md_section)
        except Exception as e:
             logger.error(f"Error irrecuperable procesando {article_path.stem}: {e}", exc_info=True)
             # Podríamos añadir una sección de error al markdown aquí si quisiéramos

        await asyncio.sleep(0.5) # Pausa entre artículos

    # Guardar informe Markdown
    try:
        with open(MARKDOWN_FILE, 'w', encoding='utf-8') as f: f.write("\n".join(all_markdown_content))
        logger.info(f"Informe Markdown guardado en: {MARKDOWN_FILE}")
    except Exception as e: logger.error(f"Error guardando informe Markdown: {e}")

    # Las métricas se guardaron incrementalmente, no es necesario guardarlas aquí de nuevo.
    # Si no se implementó el guardado incremental, se recopilarían y guardarían aquí.

    end_time_script = time.time()
    logger.info(f"--- Experimento Pipeline {args.exp_id} Completado ---")
    logger.info(f"Resultados guardados en: {OUTPUT_EXPERIMENT_DIR.resolve()}")
    logger.info(f"Métricas guardadas en: {METRICS_FILE.resolve()}")
    logger.info(f"Tiempo total de ejecución: {time.time() - start_time_script:.2f} segundos")
    return 0


# --- Punto de Entrada ---
if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)