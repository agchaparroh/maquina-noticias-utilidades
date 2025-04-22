import os
import json
import time
import logging
import asyncio
import csv
from pathlib import Path
from groq import AsyncGroq, GroqError, APITimeoutError, RateLimitError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from tqdm.asyncio import tqdm_asyncio # Barra de progreso para async
from datetime import datetime, timezone

# --- Configuración ---
# Modelos a probar (IDs de la API de Groq)
MODELOS_A_PROBAR = [
    "llama-3.1-8b-instant",
    "gemma2-9b-it",
    "llama3-8b-8192",
    "llama3-70b-8192",
    "llama-3.3-70b-versatile" # Añadimos este también
]

# Tareas a realizar (mapeo a nombres internos)
TAREAS = [
    "relevancia", # Fase 2
    "extraccion_hechos", # Fase 3a
    "extraccion_entidades", # Fase 3b
    "extraccion_citas", # Fase 3c
    "extraccion_datos" # Fase 3d
]

# Directorios
INPUT_DIR = Path("../data/benchmark_test_set") # Carpeta con test_XXX.json
OUTPUT_DIR_BASE = Path("./benchmark_results") # Carpeta base para guardar resultados
METRICS_FILE = OUTPUT_DIR_BASE / "benchmark_metrics.csv" # Archivo CSV para métricas

# Parámetros API Groq
DEFAULT_TEMPERATURE = 0.2
DEFAULT_MAX_TOKENS = 4096 # Puedes necesitar ajustar esto, especialmente para modelos grandes y tareas complejas

# Configuración de Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Funciones Auxiliares ---

def load_api_key():
    """Carga la API Key de Groq desde variable de entorno."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        logger.error("Error: Variable de entorno GROQ_API_KEY no encontrada.")
        logger.error("Por favor, ejecute: export GROQ_API_KEY='su_clave_aqui'")
        raise ValueError("GROQ_API_KEY no configurada")
    return api_key

def load_article(filepath: Path) -> dict | None:
    """Carga y parsea un archivo JSON de artículo."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        logger.error(f"Error: Archivo JSON mal formado: {filepath.name}")
        return None
    except Exception as e:
        logger.error(f"Error cargando archivo {filepath.name}: {e}")
        return None

# --- Generación de Prompts (Basado en la Documentación) ---

def generar_prompt(tarea: str, articulo: dict) -> str:
    """Genera el prompt específico para una tarea y un artículo."""
    titulo = articulo.get("titular", "")
    contenido = articulo.get("contenido_texto", "")
    medio = articulo.get("medio", "Desconocido")
    pais = articulo.get("pais_publicacion", "Desconocido")
    fecha_pub = articulo.get("fecha_publicacion", "")

    # Lista de categorías para la tarea de relevancia (ajusta según tu taxonomía final)
    lista_categorias_permitidas = '["Política Nacional", "Política Internacional", "Economía", "Conflicto/Seguridad", "Justicia/Legal", "Sociedad/Derechos", "Análisis/Contexto", "Elecciones", "Diplomacia"]'

    # Lista de tipos de hecho para la extracción (ajusta según tu taxonomía final)
    lista_tipos_hecho = '["SUCESO", "ANUNCIO", "DECLARACION", "BIOGRAFIA", "CONCEPTO", "NORMATIVA", "EVENTO"]'
    lista_precision_temporal = '["exacta", "dia", "semana", "mes", "trimestre", "año", "decada", "periodo"]'

    # Lista de tipos de entidad (ajusta según tu taxonomía final)
    lista_tipos_entidad = '["PERSONA", "ORGANIZACION", "INSTITUCION", "LUGAR", "EVENTO", "NORMATIVA", "CONCEPTO", "OTRO"]'

    # Lista de categorías de datos cuantitativos (ajusta según tu taxonomía final)
    lista_categorias_datos = '["económico", "demográfico", "electoral", "social", "presupuestario", "sanitario", "ambiental", "conflicto", "otro"]'
    lista_tipos_periodo = '["anual", "trimestral", "mensual", "semanal", "diario", "puntual", "acumulado", NULL]' # NULL como string literal aquí


    if tarea == "relevancia":
        # Prompt basado en Fase 2 - Relevancia y Categorización
        # Usamos un extracto del contenido como sugiere la documentación para esta fase
        contenido_extracto = contenido[:2000] # Primeros 2000 caracteres
        prompt = f"""
Eres un asistente experto en clasificación de noticias para una base de datos periodística especializada en la esfera hispana (política, economía, conflictos, sociedad, legal).

Analiza el siguiente artículo (título, contenido, fuente, país) y proporciona una evaluación en formato JSON con las siguientes claves OBLIGATORIAS:

1.  "puntuacion_relevancia": Un entero entre 0 y 10.
    - 0-3: Baja relevancia (probablemente descartable: deportes no políticos, entretenimiento, sucesos locales menores, estilo de vida, ciencia no política, etc.).
    - 4-6: Relevancia media (puede contener información útil pero no es central o es muy específico/rutinario).
    - 7-10: Alta relevancia (contiene información significativa sobre política nacional/internacional, economía política, conflictos importantes, legislación clave, figuras relevantes, crisis institucionales/sociales). Considera la importancia del evento, las entidades involucradas y el impacto potencial.
2.  "justificacion_relevancia": Una frase MUY BREVE (máx. 15 palabras) explicando la puntuación.
3.  "categorias_asignadas": Una lista de strings (entre 1 y 4 categorías) seleccionadas EXCLUSIVAMENTE de la siguiente lista predefinida, ordenadas por relevancia: {lista_categorias_permitidas}
4.  "resumen_breve": Una única frase concisa (máx. 25 palabras) que resuma el tema principal del artículo.

Considera el país de publicación y las entidades mencionadas para evaluar la relevancia geopolítica. Sé estricto al asignar puntuaciones altas.

Artículo a analizar:
Título: {titulo}
Medio: {medio}
País Publicación: {pais}
Contenido (extracto):
{contenido_extracto}

Responde ÚNICAMENTE con el objeto JSON válido. No incluyas NADA antes ni después del objeto JSON.
"""
        return prompt.strip()

    elif tarea == "extraccion_hechos":
        # Prompt basado en Fase 3a - Extracción Hechos y Explicaciones
        prompt = f"""
Eres un analista experto en extraer información clave de noticias para una base de datos estructurada. Analiza el siguiente artículo e identifica TODOS los hechos y explicaciones relevantes.

Un HECHO es un suceso, acción, anuncio, declaración reportada o dato biográfico concreto.
Una EXPLICACIÓN es una definición de un concepto, una descripción de una normativa, un resumen de un proceso o contexto histórico.

Para CADA hecho o explicación, proporciona la siguiente información en formato JSON, como un elemento de una lista:
{{
    "contenido": "Descripción concisa y autocontenida del hecho/explicación en tiempo verbal adecuado (máx. 70 palabras).",
    "tipo_hecho": "Selecciona UNO de: {lista_tipos_hecho}.",
    "fecha_ocurrencia_inicio": "Fecha (YYYY-MM-DD) o fecha-hora (ISO 8601) de inicio del hecho/periodo explicado. Usa la fecha del artículo si no hay otra.",
    "fecha_ocurrencia_fin": "Fecha (YYYY-MM-DD) o fecha-hora (ISO 8601) de fin, si es un rango. Opcional, usar null si no aplica.",
    "precision_temporal": "Precisión de la fecha: Selecciona UNO de {lista_precision_temporal}.",
    "paises": ["Lista de códigos de país (ISO 3166-1 alpha-2, ej. 'ES', 'AR') relevantes."],
    "ubicaciones_especificas": ["Lista de ciudades, regiones u otros lugares mencionados."],
    "importancia": "Puntuación de 1 (baja) a 10 (muy alta) sobre la relevancia periodística del hecho/explicación.",
    "confiabilidad": "Puntuación de 1 (dudoso) a 5 (muy fiable) basada en cómo lo presenta la fuente (confirmado, rumoreado, etc.).",
    "etiquetas": ["Lista de 3-7 keywords o entidades clave relevantes (minúsculas)."],
    "es_evento_futuro": true o false,
    "estado_programacion": "Si es futuro: 'programado', 'confirmado', 'cancelado', etc. (Opcional, usar null si no aplica)"
}}

Instrucciones Adicionales:
- Sé exhaustivo, extrae todos los puntos relevantes.
- Formula el 'contenido' de forma clara y objetiva.
- Para 'tipo_hecho=DECLARACION', extrae afirmaciones reportadas (no citas literales).
- Para 'tipo_hecho=CONCEPTO/NORMATIVA', el 'contenido' debe ser la explicación/definición.
- Infiere fechas y ubicaciones del contexto si no son explícitas. Si no hay fecha para un hecho, usa la fecha de publicación del artículo ({fecha_pub}) como 'fecha_ocurrencia_inicio'.
- Asegúrate de que la salida sea una lista JSON válida: [ {{hecho1}}, {{hecho2}}, ... ]. No incluyas NADA antes ni después de la lista JSON.

IMPORTANTE: La salida DEBE ser un ÚNICO objeto JSON válido que contenga UNA sola clave llamada "resultados". El valor de esta clave "resultados" DEBE ser la lista de los hechos extraídos. Ejemplo de estructura: {{"resultados": [ {{...}}, {{...}}, ... ]}}. No incluyas NADA más fuera de este objeto JSON principal. Verifica la validez del JSON completo.

Artículo:
Título: {titulo}
Fecha Pub: {fecha_pub}
País Pub: {pais}
Contenido:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    elif tarea == "extraccion_entidades":
        # Prompt basado en Fase 3b - Extracción Entidades
        prompt = f"""
Eres un especialista en Reconocimiento de Entidades Nombradas (NER) para textos periodísticos en español. Analiza el siguiente texto e identifica TODAS las entidades relevantes.

Para CADA entidad, proporciona la siguiente información en formato JSON, como un elemento de una lista:
{{
    "nombre": "Nombre CANÓNICO o más completo de la entidad (ej. 'Organización de las Naciones Unidas (ONU)', 'Pedro Sánchez Pérez-Castejón', 'Ley Orgánica 3/2018'). Intenta desambiguar contextualmente (ej. 'Elecciones Generales España 2023').",
    "tipo": "Selecciona UNO de: {lista_tipos_entidad}.",
    "alias": ["Lista de nombres alternativos o siglas mencionados en el texto (ej. 'ONU', 'PSOE'). Incluye el nombre tal cual apareció si es diferente al canónico."],
    "descripcion_contextual": "Descripción MUY BREVE (máx. 20 palabras) del rol o contexto de la entidad EN ESTE ARTÍCULO.",
    "relevancia_articulo": "Puntuación de 1 (mención pasajera) a 10 (protagonista) de la importancia de la entidad EN ESTE ARTÍCULO."
}}

Instrucciones Adicionales:
- Sé exhaustivo y extrae todas las entidades posibles de los tipos listados.
- Normaliza nombres (ej. nombres completos de personas).
- Para ORGANIZACION, incluye empresas, partidos, ONGs, grupos armados, etc.
- Para INSTITUCION, incluye gobiernos, ministerios, organismos internacionales.
- Para LUGAR, incluye países, regiones, ciudades.
- Para EVENTO, incluye elecciones, cumbres, protestas con nombre.
- Para NORMATIVA, incluye leyes, decretos, tratados.
- Para CONCEPTO, incluye ideas, teorías, mercados, casos ('Caso Gürtel'), relaciones ('Relaciones Argentina-Brasil').
- Asegúrate de que la salida sea una lista JSON válida: [ {{entidad1}}, {{entidad2}}, ... ]. No incluyas NADA antes ni después de la lista JSON.

IMPORTANTE: La salida DEBE ser un ÚNICO objeto JSON válido que contenga UNA sola clave llamada "resultados". El valor de esta clave "resultados" DEBE ser la lista de las entidades extraídas. Ejemplo de estructura: {{"resultados": [ {{...}}, {{...}}, ... ]}}. No incluyas NADA más fuera de este objeto JSON principal. Verifica la validez del JSON completo.

Texto a analizar:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    elif tarea == "extraccion_citas":
        # Prompt basado en Fase 3c - Extracción Citas
        prompt = f"""
Eres un extractor de citas textuales de artículos periodísticos. Identifica TODAS las citas literales directas (generalmente entre comillas o atribuidas con verbos como "dijo", "afirmó", "declaró").

Para CADA cita encontrada, proporciona la siguiente información en formato JSON, como un elemento de una lista:
{{
    "cita": "El texto EXACTO de la cita, tal como aparece en el artículo.",
    "emisor_nombre": "El nombre de la PERSONA u ORGANIZACIÓN que emitió la cita, tal como se menciona cerca de la cita.",
    "contexto": "Frase breve describiendo el contexto o situación donde se dijo la cita (opcional, máx. 25 palabras, usar null si no aplica).",
    "fecha_cita": "Fecha (YYYY-MM-DD) en que se dijo la cita, si se menciona explícitamente (opcional, usar null si no aplica).",
    "relevancia_cita": "Puntuación de 1 (poco relevante) a 5 (muy relevante) de la cita en el contexto del artículo."
}}

Instrucciones Adicionales:
- Extrae solo citas literales, no paráfrasis (esas van como Hechos de tipo DECLARACION).
- Incluye la atribución (quién lo dijo) de la forma más precisa posible en 'emisor_nombre'.
- Asegúrate de que la salida sea una lista JSON válida: [ {{cita1}}, {{cita2}}, ... ]. No incluyas NADA antes ni después de la lista JSON.

IMPORTANTE: La salida DEBE ser un ÚNICO objeto JSON válido que contenga UNA sola clave llamada "resultados". El valor de esta clave "resultados" DEBE ser la lista de las citas extraídas. Ejemplo de estructura: {{"resultados": [ {{...}}, {{...}}, ... ]}}. No incluyas NADA más fuera de este objeto JSON principal. Verifica la validez del JSON completo.

Texto a analizar:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    elif tarea == "extraccion_datos":
        # Prompt basado en Fase 3d - Extracción Datos Cuantitativos
        prompt = f"""
Eres un especialista en extraer datos cuantitativos estructurados de textos periodísticos. Identifica TODAS las menciones a cifras, estadísticas, porcentajes, cantidades monetarias, etc.

Para CADA dato cuantitativo relevante, proporciona la siguiente información en formato JSON, como un elemento de una lista:
{{
    "indicador": "Descripción clara de QUÉ se está midiendo (ej. 'Tasa de inflación interanual', 'PIB trimestral', 'Presupuesto de Defensa', 'Número de asistentes a manifestación').",
    "categoria": "Categoría general del dato. Selecciona UNA de: {lista_categorias_datos}.",
    "valor_numerico": "El número exacto como número (puede ser decimal). EXTRAER SOLO EL NÚMERO. Usar formato numérico estándar (ej. 1234.56, no '1,234.56').",
    "unidad": "La unidad de medida (ej. '%', 'millones de USD', 'personas', 'barriles', 'votos', 'hectáreas').",
    "ambito_geografico": ["Lista de países, regiones o ciudades a los que aplica el dato."],
    "periodo_referencia_inicio": "Fecha de inicio (YYYY-MM-DD) del periodo al que se refiere el dato (opcional, usar null si no aplica).",
    "periodo_referencia_fin": "Fecha de fin (YYYY-MM-DD) del periodo (opcional, usar misma que inicio si es puntual, null si no aplica).",
    "tipo_periodo": "Tipo de periodo. Selecciona UNO de: {lista_tipos_periodo} (usar null si no aplica).",
    "fuente_especifica": "La fuente específica del dato si se menciona (ej. 'INE', 'Banco Central', 'Ministerio X'). (Opcional, usar null si no aplica)",
    "notas_contexto": "Cualquier nota breve adicional necesaria para interpretar el dato (ej. 'ajustado estacionalmente', 'según estimaciones preliminares'). (Opcional, usar null si no aplica)"
}}

Instrucciones Adicionales:
- Sé preciso con los números y unidades. Convierte texto como 'mil millones' a números si es posible.
- Infiere el ámbito geográfico y el periodo del contexto si no son explícitos junto al número.
- Extrae solo datos concretos, no estimaciones vagas si no tienen número.
- Asegúrate de que la salida sea una lista JSON válida: [ {{dato1}}, {{dato2}}, ... ]. No incluyas NADA antes ni después de la lista JSON.

IMPORTANTE: La salida DEBE ser un ÚNICO objeto JSON válido que contenga UNA sola clave llamada "resultados". El valor de esta clave "resultados" DEBE ser la lista de los datos extraídos. Ejemplo de estructura: {{"resultados": [ {{...}}, {{...}}, ... ]}}. No incluyas NADA más fuera de este objeto JSON principal. Verifica la validez del JSON completo.

Texto a analizar:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    else:
        logger.warning(f"Tarea desconocida: {tarea}. Generando prompt vacío.")
        return ""

# --- Función Principal de Llamada a Groq (Adaptada de antes) ---
RETRYABLE_ERRORS = (APITimeoutError, RateLimitError, GroqError)
def es_error_reintentable(exception):
    """Comprueba si una excepción es de un tipo que queremos reintentar."""
    # Podríamos añadir lógica para reintentar solo en errores 5xx de GroqError
    if isinstance(exception, GroqError):
        # Asumiendo que GroqError puede tener un status_code, aunque la librería actual no lo expone fácilmente
        # Si tuviera status code, podríamos hacer: return getattr(exception, 'status_code', 500) >= 500
        # Por ahora, reintentamos en cualquier GroqError, RateLimit o Timeout
        return True
    return isinstance(exception, (APITimeoutError, RateLimitError))


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(RETRYABLE_ERRORS),
    reraise=True
)
async def llamar_groq_con_metricas(
    client: AsyncGroq,
    model_id: str,
    prompt: str,
    test_id: str,
    tarea: str,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    # Groq espera un objeto JSON, lo que ahora coincide con nuestro formato {"resultados": [...]}
    response_format: dict = {"type": "json_object"}
) -> tuple[str | None, dict]:
    """Llama a Groq, mide métricas, maneja errores y reintentos."""
    start_time = time.time()
    error_message = None
    success = False
    response_content = None
    usage_data = None
    latency = 0

    try:
        logger.debug(f"[{test_id}][{tarea}][{model_id}] Llamando a Groq...")
        chat_completion = await client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model_id,
            temperature=temperature,
            max_completion_tokens=max_tokens,
            response_format=response_format,
            # seed=42 # Para reproducibilidad si ayuda
        )
        latency = time.time() - start_time
        response_content = chat_completion.choices[0].message.content
        usage_data = chat_completion.usage
        success = True
        logger.debug(f"[{test_id}][{tarea}][{model_id}] Éxito.")

    except Exception as e:
        latency = time.time() - start_time
        error_message = f"{type(e).__name__}: {str(e)}"
        logger.error(f"[{test_id}][{tarea}][{model_id}] Error final tras reintentos: {error_message}")
        success = False
        # No relanzamos la excepción aquí para que el bucle principal continúe
        # La información del error queda registrada en las métricas.

    # Construir diccionario de métricas
    metrics = {
        "test_id": test_id,
        "tarea": tarea,
        "model_id": model_id,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "latency_seconds": round(latency, 3),
        "prompt_tokens": usage_data.prompt_tokens if usage_data else None,
        "completion_tokens": usage_data.completion_tokens if usage_data else None,
        "total_tokens": usage_data.total_tokens if usage_data else None,
        "success": success,
        "error_message": error_message
    }

    return response_content, metrics

# --- Función para Guardar Resultados ---

def guardar_resultado_llm(test_id: str, tarea: str, model_id: str, content: str | None, output_dir: Path):
    """Guarda la respuesta del LLM en un archivo JSON."""
    # Crear subdirectorios si no existen
    task_dir = output_dir / test_id / tarea
    task_dir.mkdir(parents=True, exist_ok=True)

    # Nombre de archivo basado en el modelo
    filename = f"{model_id.replace('/', '_')}.json" # Reemplazar '/' para nombres de archivo válidos
    filepath = task_dir / filename

    # Guardar el contenido (string JSON devuelto por Groq o mensaje de error)
    result_data = {
        "test_id": test_id,
        "tarea": tarea,
        "model_id": model_id,
        "llm_response_content": content if content is not None else "Error: No content received"
    }

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result_data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.error(f"[{test_id}][{tarea}][{model_id}] Error guardando respuesta LLM en {filepath}: {e}")

def guardar_metricas_csv(metrics: dict, csv_filepath: Path):
    """Añade una fila de métricas a un archivo CSV."""
    try:
        write_header = not csv_filepath.exists() or csv_filepath.stat().st_size == 0

        with open(csv_filepath, 'a', newline='', encoding='utf-8') as f:
            # Asegurar un orden consistente de columnas
            fieldnames = [
                "test_id", "tarea", "model_id", "timestamp_utc",
                "latency_seconds", "prompt_tokens", "completion_tokens",
                "total_tokens", "success", "error_message"
            ]
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore') # Ignorar campos extra

            if write_header:
                writer.writeheader()
            writer.writerow(metrics)
    except Exception as e:
        logger.error(f"[{metrics['test_id']}][{metrics['tarea']}][{metrics['model_id']}] Error guardando métricas en {csv_filepath}: {e}")

# --- Lógica Principal Asíncrona ---

async def procesar_articulo(client: AsyncGroq, article_path: Path, output_dir_base: Path, csv_filepath: Path):
    """Procesa un único artículo con todas las tareas y modelos."""
    test_id = article_path.stem
    logger.info(f"--- Procesando Artículo: {test_id} ---")

    articulo = load_article(article_path)
    if not articulo:
        logger.warning(f"Omitiendo artículo {test_id} debido a error de carga.")
        # Registrar métrica de fallo de carga si se desea
        return

    tasks_to_process = []
    for tarea in TAREAS:
        prompt = generar_prompt(tarea, articulo)
        if not prompt:
            logger.warning(f"[{test_id}][{tarea}] Prompt vacío, omitiendo tarea.")
            continue
        for model_id in MODELOS_A_PROBAR:
             tasks_to_process.append(
                 llamar_groq_con_metricas(
                    client=client,
                    model_id=model_id,
                    prompt=prompt,
                    test_id=test_id,
                    tarea=tarea
                )
            )

    # Ejecutar todas las llamadas a Groq para este artículo en paralelo
    logger.info(f"[{test_id}] Lanzando {len(tasks_to_process)} llamadas a Groq...")
    results = await tqdm_asyncio.gather(
        *tasks_to_process,
        desc=f"[{test_id}] Llamadas Groq",
        leave=False
    )

    # Procesar y guardar resultados
    for i, (response_content, metrics) in enumerate(results):
        # Recuperar tarea y modelo de las métricas (ya que gather no mantiene el orden original fácilmente si hay reintentos)
        tarea = metrics['tarea']
        model_id = metrics['model_id']

        guardar_resultado_llm(test_id, tarea, model_id, response_content, output_dir_base)
        guardar_metricas_csv(metrics, csv_filepath)

    logger.info(f"--- Artículo {test_id} completado ---")


async def main():
    """Función principal del script de benchmarking."""
    start_time_script = time.time()
    logger.info("--- Iniciando Script de Benchmarking Groq ---")

    try:
        api_key = load_api_key()
        # Inicializar el cliente AsyncGroq
        client = AsyncGroq(api_key=api_key, timeout=90.0)
        logger.info("Cliente AsyncGroq inicializado.")
    except ValueError:
        return

    OUTPUT_DIR_BASE.mkdir(parents=True, exist_ok=True)
    logger.info(f"Directorio de resultados: {OUTPUT_DIR_BASE.resolve()}")
    logger.info(f"Archivo de métricas: {METRICS_FILE.resolve()}")

    try:
        # Usar Path.glob para encontrar archivos, manejar posibles errores
        test_files_gen = INPUT_DIR.glob("test_*.json")
        test_files = sorted(list(test_files_gen))
        if not test_files:
             raise FileNotFoundError # Lanzar error si glob no encontró nada
        logger.info(f"Encontrados {len(test_files)} archivos de prueba en {INPUT_DIR.resolve()}")
    except FileNotFoundError:
         logger.error(f"Error: No se encontraron archivos 'test_*.json' o el directorio de entrada no existe: {INPUT_DIR.resolve()}")
         return
    except Exception as e:
        logger.error(f"Error inesperado listando archivos de prueba: {e}")
        return

    # Procesar artículos concurrentemente (con un límite para no sobrecargar Groq)
    CONCURRENCY_LIMIT = 5 # Número de artículos a procesar en paralelo
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

    async def process_with_semaphore(article_path):
        async with semaphore:
            await procesar_articulo(client, article_path, OUTPUT_DIR_BASE, METRICS_FILE)

    processing_tasks = [process_with_semaphore(fp) for fp in test_files]

    # Usar tqdm para la barra de progreso general de artículos
    logger.info(f"Iniciando procesamiento de {len(test_files)} artículos con concurrencia {CONCURRENCY_LIMIT}...")
    await tqdm_asyncio.gather(*processing_tasks, desc="Progreso General Artículos")


    end_time_script = time.time()
    logger.info("--- Benchmarking Completado ---")
    logger.info(f"Resultados LLM guardados en subdirectorios dentro de: {OUTPUT_DIR_BASE.resolve()}")
    logger.info(f"Métricas agregadas guardadas en: {METRICS_FILE.resolve()}")
    logger.info(f"Tiempo total de ejecución del script: {time.time() - start_time_script:.2f} segundos")

# --- Punto de Entrada ---
if __name__ == "__main__":
    # Añadir manejo de httpx si es necesario aquí o en la función main
    import httpx # Asegurar que esté importado si usamos los límites
    asyncio.run(main())