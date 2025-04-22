# run_prompt_test.py
import os
import json
import time
import logging
import asyncio
import csv
import re # Importar regex para limpieza
from pathlib import Path
from groq import AsyncGroq, GroqError, APITimeoutError, RateLimitError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from tqdm.asyncio import tqdm_asyncio # Barra de progreso para async
from datetime import datetime, timezone
from typing import Optional, Tuple, Dict, Any # Añadir type hints

# --- Configuración ---
# Modelo a probar (ÚNICO)
MODEL_TO_TEST = "llama3-8b-8192"

# Tareas a realizar (mapeo a nombres internos)
TASKS = [
    "relevancia", # Fase 2
    "extraccion_hechos", # Fase 3a
    "extraccion_entidades", # Fase 3b
    "extraccion_citas", # Fase 3c
    "extraccion_datos" # Fase 3d
]

# Directorios
INPUT_DIR = Path("../data/benchmark_test_set") # Carpeta con test_XXX.json originales
OUTPUT_DIR_BASE = Path("./prompt_test_results") # NUEVA Carpeta base para guardar resultados de esta prueba
METRICS_FILE = OUTPUT_DIR_BASE / "prompt_test_metrics.csv" # NUEVO Archivo CSV para métricas

# Parámetros API Groq
DEFAULT_TEMPERATURE = 0.2
DEFAULT_MAX_TOKENS = 4096 # Ajustar si es necesario

# Configuración de Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Funciones Auxiliares ---

def load_api_key() -> str:
    """Carga la API Key de Groq desde variable de entorno."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        logger.error("Error: Variable de entorno GROQ_API_KEY no encontrada.")
        logger.error("Por favor, ejecute: export GROQ_API_KEY='su_clave_aqui'")
        raise ValueError("GROQ_API_KEY no configurada")
    return api_key

def load_article(filepath: Path) -> Optional[Dict[str, Any]]:
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

def _clean_json_string(raw_string: Optional[str]) -> Optional[str]:
    """
    Intenta extraer el primer bloque JSON válido (objeto o array) de una cadena.
    Elimina texto antes del primer '{' o '[' y después del último '}' o ']'.
    """
    if not raw_string:
        return None

    # Buscar el primer '{' o '[' y el último '}' o ']'
    # Usar regex no voraz para encontrar el bloque más interno si hay anidamiento incorrecto al inicio/final
    match = re.search(r"^\s*(?:\{.*\}|\[.*\])\s*$", raw_string, re.DOTALL)

    if match:
        # Si la cadena ya es un JSON válido de principio a fin
         return match.group(0).strip()
    else:
        # Intentar encontrar el primer { o [ y el último } o ] correspondiente
        # Esto es más complejo de hacer perfectamente con regex para casos anidados
        # Un enfoque más simple: buscar el primer {/[ y el último }/]
        start_brace = raw_string.find('{')
        start_bracket = raw_string.find('[')

        if start_brace == -1 and start_bracket == -1:
            # No se encontró inicio de JSON
            return None

        if start_brace == -1:
            start_index = start_bracket
            end_char = ']'
        elif start_bracket == -1:
            start_index = start_brace
            end_char = '}'
        else:
            # Tomar el que aparezca primero
            start_index = min(start_brace, start_bracket)
            end_char = '}' if start_index == start_brace else ']'

        # Buscar la última ocurrencia del carácter de cierre correspondiente
        end_index = raw_string.rfind(end_char)

        if start_index != -1 and end_index != -1 and end_index > start_index:
            # Extraer el contenido potencial JSON
            potential_json = raw_string[start_index : end_index + 1]
            # Validar si esto al menos parece un JSON (simple check)
            try:
                json.loads(potential_json)
                return potential_json
            except json.JSONDecodeError:
                 # Si falla, quizás la extracción simple no funcionó, devolver None
                 logger.warning(f"No se pudo extraer un bloque JSON limpio de la respuesta.")
                 return None
        else:
            # No se encontró un par válido de inicio/fin
            return None


# --- Generación de Prompts (REVISADOS) ---

def generar_prompt(tarea: str, articulo: dict) -> str:
    """Genera el prompt específico REVISADO para una tarea y un artículo."""
    titulo = articulo.get("titular", "")
    contenido = articulo.get("contenido_texto", "")
    medio = articulo.get("medio", "Desconocido")
    pais = articulo.get("pais_publicacion", "Desconocido")
    fecha_pub_str = articulo.get("fecha_publicacion", "Fecha desconocida")
    # Intentar parsear fecha para usarla en prompts si es válida
    try:
        # Manejar diferentes formatos de zona horaria, incluyendo Z
        if fecha_pub_str.endswith('Z'):
            fecha_pub_dt = datetime.fromisoformat(fecha_pub_str.replace('Z', '+00:00'))
        else:
            fecha_pub_dt = datetime.fromisoformat(fecha_pub_str)
        fecha_pub = fecha_pub_dt.date().isoformat() # Usar solo YYYY-MM-DD en prompts
    except (ValueError, TypeError):
        fecha_pub = fecha_pub_str # Usar como string si no es formato ISO válido

    # --- Definición de Listas (Asegúrate de que coincidan con tu esquema final) ---
    lista_categorias_permitidas = '["Política Nacional", "Política Internacional", "Economía", "Conflicto/Seguridad", "Justicia/Legal", "Sociedad/Derechos", "Análisis/Contexto", "Elecciones", "Diplomacia"]'
    lista_tipos_hecho = '["SUCESO", "ANUNCIO", "DECLARACION", "BIOGRAFIA", "CONCEPTO", "NORMATIVA", "EVENTO"]'
    lista_precision_temporal = '["exacta", "dia", "semana", "mes", "trimestre", "año", "decada", "periodo"]'
    lista_tipos_entidad = '["PERSONA", "ORGANIZACION", "INSTITUCION", "LUGAR", "EVENTO", "NORMATIVA", "CONCEPTO", "OTRO"]'
    lista_categorias_datos = '["económico", "demográfico", "electoral", "social", "presupuestario", "sanitario", "ambiental", "conflicto", "otro"]'
    lista_tipos_periodo = '["anual", "trimestral", "mensual", "semanal", "diario", "puntual", "acumulado"]'
    # --- Fin de la sección de listas ---


    if tarea == "relevancia":
        # Prompt REVISADO basado en Fase 2 - Relevancia y Categorización
        contenido_extracto = contenido[:2000] # Primeros 2000 caracteres
        prompt = f"""
Eres un asistente experto en clasificación de noticias para una base de datos periodística especializada en la esfera hispana (política, economía, conflictos, sociedad, legal).

Analiza el siguiente artículo (título, contenido, fuente, país) y proporciona una evaluación en formato JSON con las siguientes claves OBLIGATORIAS:

1.  "puntuacion_relevancia": Un entero entre 0 y 10. Evalúa la importancia **del tema tratado en el artículo** en relación con los ámbitos de interés (política nacional/internacional, economía política, conflictos importantes, legislación clave, figuras relevantes, crisis institucionales/sociales) dentro de la esfera hispana.
    - 0-3: Baja relevancia (probablemente descartable: deportes no políticos, entretenimiento, sucesos locales menores sin impacto amplio, estilo de vida, ciencia/cultura sin conexión política/social clara, etc.).
    - 4-6: Relevancia media (contiene información útil pero no es central para los temas principales, es muy específico/rutinario, o su impacto es limitado).
    - 7-8: Alta relevancia (contiene información significativa sobre los temas de interés, involucra entidades importantes, tiene impacto potencial claro).
    - 9-10: Muy Alta relevancia (reservado para eventos de **gran trascendencia** nacional o internacional como cambios de gobierno, crisis graves, legislación estructural, conflictos de alto impacto, etc.).
    Considera la importancia del evento/tema, las entidades involucradas y el impacto potencial. Sé estricto al asignar puntuaciones altas (7-10).
2.  "justificacion_relevancia": Una frase MUY BREVE (máx. 15 palabras) explicando la puntuación asignada.
3.  "categorias_asignadas": Una lista de strings (entre 1 y 4 categorías) seleccionadas EXCLUSIVAMENTE de la siguiente lista predefinida, ordenadas por relevancia: {lista_categorias_permitidas}
4.  "explicacion_concisa": Una explicación del contenido principal del artículo (**máximo 100 palabras**). Utiliza un lenguaje **claro, profesional y directo**.

Considera el país de publicación y las entidades mencionadas para evaluar la relevancia geopolítica.

Artículo a analizar:
Título: {titulo}
Medio: {medio}
País Publicación: {pais}
Contenido (extracto):
{contenido_extracto}

Responde ÚNICAMENTE con el objeto JSON válido. No incluyas NADA antes ni después del objeto JSON. Asegúrate de que el JSON tenga las claves "puntuacion_relevancia", "justificacion_relevancia", "categorias_asignadas", y "explicacion_concisa".
"""
        return prompt.strip()

    elif tarea == "extraccion_hechos":
        # Prompt REVISADO basado en Fase 3a - Extracción Hechos y Explicaciones
        prompt = f"""
Eres un analista experto en extraer información clave de noticias para una base de datos estructurada. Tu tarea es identificar y extraer TODOS los hechos y explicaciones relevantes del artículo proporcionado.

DEFINICIONES:
- Un HECHO es un suceso, acción, anuncio, declaración reportada o dato biográfico concreto (Tipos: SUCESO, ANUNCIO, DECLARACION, BIOGRAFIA, EVENTO).
- Una EXPLICACIÓN es una definición de un concepto, una descripción de una normativa, un resumen de un proceso o contexto histórico (Tipos: CONCEPTO, NORMATIVA).

Para CADA hecho o explicación identificado, proporciona la siguiente información estructurada como un objeto JSON dentro de una lista:
{{
    "contenido": "Descripción CLARA, CONCISA (máx. 70 palabras) y AUTOCONTENIDA del hecho/explicación. Debe ser objetiva y redactada en el tiempo verbal adecuado.",
    "tipo_hecho": "Selecciona ESTRICTAMENTE UNO de los siguientes tipos: {lista_tipos_hecho}.",
    "fecha_ocurrencia_inicio": "Fecha de inicio del hecho/periodo en formato ISO 8601 (YYYY-MM-DD o YYYY-MM-DDTHH:MM:SSZ). Si no se menciona fecha específica, INFIERE la más probable del contexto o usa la fecha de publicación del artículo ({fecha_pub}) como último recurso.",
    "fecha_ocurrencia_fin": "Fecha de fin del hecho/periodo en formato ISO 8601 (YYYY-MM-DD o YYYY-MM-DDTHH:MM:SSZ). Usa ESTE CAMPO SOLO si el hecho abarca un RANGO de tiempo explícito. Si no es un rango o la fecha fin no se conoce, usa el valor JSON `null`.",
    "precision_temporal": "Precisión de la fecha/periodo. Selecciona ESTRICTAMENTE UNO de: {lista_precision_temporal}.",
    "paises": ["Lista de códigos de país relevantes en formato ISO 3166-1 alpha-2 (ej. 'ES', 'AR', 'MX'). Extrae TODOS los países mencionados directamente en relación al hecho."],
    "ubicaciones_especificas": ["Lista de ciudades, regiones, provincias u otros lugares específicos mencionados en relación al hecho (ej. 'Bogotá', 'Región Andina', 'Palacio de Miraflores'). Puede ser una lista vacía [] si no hay lugares específicos."],
    "importancia": "Puntuación de 1 (baja) a 10 (muy alta) sobre la relevancia periodística INTRÍNSECA de este hecho/explicación específico.",
    "confiabilidad": "Puntuación de 1 (dudoso/rumor) a 5 (confirmado/muy fiable) basada en CÓMO la fuente presenta la información (ej. 'afirmó', 'según fuentes', 'se rumorea').",
    "etiquetas": ["Lista de 3 a 7 palabras clave o entidades relevantes (en minúsculas) que describan el tema específico de este hecho/explicación."],
    "es_evento_futuro": `true` si el hecho describe un evento programado para ocurrir después de la fecha de publicación del artículo, de lo contrario `false`.",
    "estado_programacion": "Si 'es_evento_futuro' es true, indica el estado (ej. 'programado', 'confirmado', 'cancelado'). Si no es futuro o no se menciona estado, usa el valor JSON `null`."
}}

INSTRUCCIONES ADICIONALES IMPORTANTES:
- **Exhaustividad:** Asegúrate de extraer TODOS los hechos/explicaciones distintos y relevantes.
- **Objetividad:** El 'contenido' debe ser neutral, sin opiniones.
- **DECLARACION vs CITA:** Usa 'DECLARACION' para afirmaciones reportadas o paráfrasis. Las citas textuales exactas NO se extraen aquí.
- **CONCEPTO/NORMATIVA:** El 'contenido' debe ser la definición o explicación en sí.
- **Fechas:** Sé preciso con las fechas. Si infieres, asegúrate de que sea razonable. El formato ISO 8601 es obligatorio. Usa `null` explícitamente donde se indica.
- **Listas:** Los campos 'paises', 'ubicaciones_especificas' y 'etiquetas' DEBEN ser listas JSON (aunque estén vacías: []).
- **JSON Final:** La respuesta COMPLETA debe ser un ÚNICO objeto JSON que contenga UNA sola clave llamada "resultados". El valor de "resultados" DEBE ser la lista JSON de los objetos de hechos/explicaciones extraídos. Ejemplo: {{"resultados": [ {{hecho1}}, {{hecho2}}, ... ]}}. NO incluyas NINGÚN texto antes o después de este objeto JSON principal. Verifica la validez del JSON.

Artículo a analizar:
Título: {titulo}
Fecha Pub: {fecha_pub}
País Pub: {pais}
Contenido:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    elif tarea == "extraccion_entidades":
        # Prompt REVISADO basado en Fase 3b - Extracción Entidades
        prompt = f"""
Eres un especialista en Reconocimiento de Entidades Nombradas (NER) altamente preciso para textos periodísticos en español. Tu objetivo es identificar TODAS las entidades relevantes mencionadas en el texto.

Para CADA entidad identificada, proporciona la siguiente información estructurada como un objeto JSON dentro de una lista:
{{
    "nombre": "El nombre CANÓNICO o más completo y formal de la entidad. Intenta resolver acrónimos (ej. 'Organización de las Naciones Unidas (ONU)') y nombres de personas ('Nombre Completo Apellido1 Apellido2'). Desambigua contextualmente si es necesario (ej. 'Elecciones Generales España 2023' en lugar de solo 'Elecciones').",
    "tipo": "Clasifica la entidad seleccionando ESTRICTAMENTE UNO de los siguientes tipos: {lista_tipos_entidad}.",
    "alias": ["Lista de nombres alternativos, siglas o formas en que la entidad fue MENCIONADA EXPLÍCITAMENTE en el texto si son diferentes del nombre canónico (ej. ['ONU', 'Naciones Unidas']). Puede ser una lista vacía []."]
}}

DEFINICIONES DE TIPOS (Guía):
- PERSONA: Individuos humanos.
- ORGANIZACION: Empresas, partidos, ONGs, grupos armados, sindicatos, medios de comunicación.
- INSTITUCION: Gobiernos, ministerios, parlamentos, tribunales, organismos internacionales (ONU, FMI), fuerzas armadas/policiales.
- LUGAR: Países, regiones, ciudades, edificios específicos.
- EVENTO: Elecciones, cumbres, protestas con nombre, conflictos con nombre, desastres naturales.
- NORMATIVA: Leyes, decretos, tratados, constituciones.
- CONCEPTO: Ideas abstractas, teorías, mercados, casos judiciales ('Caso Gürtel'), problemas sociales ('Crisis Migratoria').
- OTRO: Solo si ninguna otra categoría encaja claramente.

INSTRUCCIONES ADICIONALES IMPORTANTES:
- **Exhaustividad y Precisión:** Identifica TODAS las entidades relevantes de los tipos listados. Prioriza la precisión en el nombre canónico y el tipo.
- **Normalización:** Aplica la normalización al 'nombre' como se indica.
- **Alias:** Incluye en 'alias' solo las formas alternativas mencionadas textualmente.
- **Listas:** El campo 'alias' DEBE ser una lista JSON (aunque esté vacía: []).
- **JSON Final:** La respuesta COMPLETA debe ser un ÚNICO objeto JSON que contenga UNA sola clave llamada "resultados". El valor de "resultados" DEBE ser la lista JSON de los objetos de entidades extraídos. Ejemplo: {{"resultados": [ {{entidad1}}, {{entidad2}}, ... ]}}. NO incluyas NINGÚN texto antes o después de este objeto JSON principal. Verifica la validez del JSON.

Texto a analizar:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    elif tarea == "extraccion_citas":
        # Prompt REVISADO basado en Fase 3c - Extracción Citas
        prompt = f"""
Eres un extractor especializado en identificar y extraer citas textuales DIRECTAS de artículos periodísticos en español.

Tu tarea es encontrar TODAS las frases o fragmentos que sean citas literales (generalmente entre comillas "..." o atribuidas explícitamente con verbos como "dijo", "afirmó", "declaró", "señaló", etc.). NO extraigas paráfrasis ni resúmenes de declaraciones.

Para CADA cita literal encontrada, proporciona la siguiente información estructurada como un objeto JSON dentro de una lista:
{{
    "cita": "El texto EXACTO de la cita, incluyendo la puntuación original, tal como aparece en el artículo.",
    "emisor_nombre": "El nombre de la PERSONA u ORGANIZACIÓN que emitió la cita, identificado de la forma más precisa posible según el texto cercano a la cita.",
    "contexto": "Frase breve (máx. 25 palabras) describiendo el contexto inmediato donde se dijo la cita. Si no hay contexto claro o relevante, usa el valor JSON `null`.",
    "fecha_cita": "Fecha (YYYY-MM-DD) en que se realizó la declaración, SOLO si se menciona explícitamente en el texto. Si no se menciona, usa el valor JSON `null`."
}}

INSTRUCCIONES ADICIONALES IMPORTANTES:
- **Literalidad:** Extrae ÚNICAMENTE citas textuales directas.
- **Atribución:** Identifica claramente al emisor en 'emisor_nombre'.
- **Valores Nulos:** Usa `null` explícitamente para 'contexto' y 'fecha_cita' cuando no aplique o no se encuentre la información.
- **JSON Final:** La respuesta COMPLETA debe ser un ÚNICO objeto JSON que contenga UNA sola clave llamada "resultados". El valor de "resultados" DEBE ser la lista JSON de los objetos de citas extraídos. Ejemplo: {{"resultados": [ {{cita1}}, {{cita2}}, ... ]}}. NO incluyas NINGÚN texto antes o después de este objeto JSON principal. Verifica la validez del JSON.

Texto a analizar:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    elif tarea == "extraccion_datos":
        # Prompt REVISADO basado en Fase 3d - Extracción Datos Cuantitativos
        prompt = f"""
Eres un especialista altamente preciso en extraer datos cuantitativos estructurados de textos periodísticos en español. Tu tarea es identificar TODAS las menciones a cifras, estadísticas, porcentajes, cantidades monetarias, etc., que sean relevantes y estén claramente definidas.

Para CADA dato cuantitativo identificado, proporciona la siguiente información estructurada como un objeto JSON dentro de una lista:
{{
    "indicador": "Descripción CLARA y específica de QUÉ magnitud se está midiendo (ej. 'Tasa de inflación interanual', 'PIB trimestral real', 'Presupuesto asignado a Defensa', 'Número de votos obtenidos por el partido X', 'Hectáreas deforestadas').",
    "categoria": "Categoría general del dato. Selecciona ESTRICTAMENTE UNA de: {lista_categorias_datos}.",
    "valor_numerico": "El valor numérico EXACTO. **IMPORTANTE**: Debe ser un tipo de dato NUMÉRICO JSON válido (entero o decimal con punto '.'). NO uses comas ',' para miles. NO incluyas símbolos como '%' o '$'. Convierte texto como '1.5 millones' a 1500000 o 'tres mil' a 3000 si es posible sin ambigüedad.",
    "unidad": "La unidad de medida asociada al valor numérico (ej. '%', 'USD', 'EUR', 'personas', 'votos', 'barriles por día', 'hectáreas', 'toneladas métricas'). Sé lo más específico posible.",
    "ambito_geografico": ["Lista de nombres de países, regiones o ciudades a los que aplica específicamente este dato. Puede ser una lista vacía [] si el ámbito no está claro o es global."],
    "periodo_referencia_inicio": "Fecha de inicio (YYYY-MM-DD) del periodo al que se refiere el dato. Si no se especifica, usa el valor JSON `null`.",
    "periodo_referencia_fin": "Fecha de fin (YYYY-MM-DD) del periodo. Usa la misma fecha que inicio si es un dato puntual. Si no se especifica, usa el valor JSON `null`.",
    "tipo_periodo": "Tipo de periodo temporal del dato. Selecciona ESTRICTAMENTE UNO de: {lista_tipos_periodo}. Si no aplica o no se especifica, usa el valor JSON `null`.",
    "fuente_especifica": "La fuente original del dato si se menciona explícitamente en el texto (ej. 'INE', 'Banco Mundial', 'FMI', 'Ministerio de Hacienda'). Si no se menciona, usa el valor JSON `null`.",
    "notas_contexto": "Cualquier nota breve (máx. 30 palabras) que sea ESENCIAL para interpretar correctamente el dato (ej. 'ajustado estacionalmente', 'estimación preliminar', 'comparado con el año anterior'). Si no hay notas esenciales, usa el valor JSON `null`."
}}

INSTRUCCIONES ADICIONALES IMPORTANTES:
- **Precisión Numérica:** La exactitud del 'valor_numerico' y su formato como número JSON es CRÍTICA.
- **Claridad del Indicador:** El 'indicador' debe dejar claro qué mide el número.
- **Unidades:** La 'unidad' debe ser precisa.
- **Contexto:** Infiere el ámbito geográfico y el periodo del contexto cercano si no son explícitos junto al número.
- **Datos Concretos:** Extrae solo datos numéricos específicos, ignora estimaciones vagas sin cifras (ej. "muchos", "varios miles").
- **Valores Nulos:** Usa `null` explícitamente para los campos opcionales cuando no haya información.
- **Listas:** El campo 'ambito_geografico' DEBE ser una lista JSON (aunque esté vacía: []).
- **JSON Final:** La respuesta COMPLETA debe ser un ÚNICO objeto JSON que contenga UNA sola clave llamada "resultados". El valor de "resultados" DEBE ser la lista JSON de los objetos de datos extraídos. Ejemplo: {{"resultados": [ {{dato1}}, {{dato2}}, ... ]}}. NO incluyas NINGÚN texto antes o después de este objeto JSON principal. Verifica la validez del JSON.

Texto a analizar:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    else:
        logger.warning(f"Tarea desconocida: {tarea}. Generando prompt vacío.")
        return ""

# --- Función Principal de Llamada a Groq (Con Limpieza y Validación JSON) ---
RETRYABLE_ERRORS = (APITimeoutError, RateLimitError, GroqError)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(RETRYABLE_ERRORS),
    reraise=True # Re-lanza la excepción si todos los reintentos fallan
)
async def llamar_groq_con_metricas(
    client: AsyncGroq,
    model_id: str, # Será siempre MODEL_TO_TEST
    prompt: str,
    test_id: str,
    tarea: str,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    response_format: Dict[str, str] = {"type": "json_object"}
) -> Tuple[Optional[str], Dict[str, Any]]:
    """Llama a Groq, mide métricas, limpia, valida JSON y maneja errores/reintentos."""
    start_time = time.time()
    error_message: Optional[str] = None
    api_success: bool = False
    json_valid: bool = False
    response_content: Optional[str] = None
    usage_data: Optional[Any] = None # Usar Any o el tipo específico si se conoce
    latency: float = 0.0
    cleaned_content: Optional[str] = None # Contenido después de limpiar

    try:
        logger.debug(f"[{test_id}][{tarea}][{model_id}] Llamando a Groq...")
        chat_completion = await client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=model_id,
            temperature=temperature,
            max_completion_tokens=max_tokens,
            response_format=response_format,
        )
        latency = time.time() - start_time
        response_content = chat_completion.choices[0].message.content
        usage_data = chat_completion.usage
        api_success = True # Éxito de la llamada API
        logger.debug(f"[{test_id}][{tarea}][{model_id}] Éxito API.")

        # --- LIMPIEZA Y VALIDACIÓN JSON ---
        if response_content:
            cleaned_content = _clean_json_string(response_content)
            if cleaned_content:
                try:
                    # Intentar parsear para validar
                    json_parsed = json.loads(cleaned_content)

                    # Validación de estructura básica para tareas de extracción
                    if tarea != "relevancia":
                        if not isinstance(json_parsed, dict):
                             raise ValueError("Respuesta JSON no es un objeto (dict)")
                        if "resultados" not in json_parsed:
                             raise ValueError("Respuesta JSON no contiene la clave 'resultados'")
                        if not isinstance(json_parsed.get("resultados"), list):
                             raise ValueError("El valor de 'resultados' no es una lista JSON")
                    # Podríamos añadir más validaciones con jsonschema si fuera necesario aquí

                    # Si todo va bien:
                    json_valid = True
                    logger.debug(f"[{test_id}][{tarea}][{model_id}] Respuesta JSON válida y estructura básica OK.")
                except json.JSONDecodeError as json_err:
                    logger.error(f"[{test_id}][{tarea}][{model_id}] Error: Respuesta LLM (limpia) no es JSON válido. {json_err}")
                    error_message = f"JSONDecodeError: {json_err}"
                except ValueError as val_err: # Captura errores de estructura
                    logger.error(f"[{test_id}][{tarea}][{model_id}] Error: Estructura JSON inválida. {val_err}")
                    error_message = f"JSONStructureError: {val_err}"
                except Exception as parse_err: # Capturar otros errores inesperados
                    logger.error(f"[{test_id}][{tarea}][{model_id}] Error inesperado validando/parseando JSON: {parse_err}")
                    error_message = f"JSONParseError: {parse_err}"
            else:
                # Si _clean_json_string devolvió None
                logger.error(f"[{test_id}][{tarea}][{model_id}] Error: No se pudo extraer un bloque JSON limpio de la respuesta.")
                error_message = "JSONCleanError: No JSON block found in response"
        else:
             # Si response_content está vacío tras éxito de API (raro pero posible)
             logger.error(f"[{test_id}][{tarea}][{model_id}] API Success but empty content received")
             error_message = "API Success but empty content received"

    except Exception as e:
        # Captura errores de API tras reintentos (si reraise=True) u otros errores
        latency = time.time() - start_time
        error_message = f"API_Error: {type(e).__name__}: {str(e)}"
        logger.error(f"[{test_id}][{tarea}][{model_id}] Error final API: {error_message}")
        api_success = False # La API falló definitivamente
        json_valid = False # No se puede validar JSON si la API falló

    # Determinar éxito general
    success = api_success and json_valid

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
        "success": success, # Éxito general (API OK + JSON Válido y estructura OK)
        "api_success": api_success, # Indica si la llamada API en sí tuvo éxito
        "json_valid": json_valid, # Indica si el JSON fue parseable y con estructura ok
        "error_message": error_message
    }

    # Devolver el contenido LIMPIO si fue válido, o el original si no, para depuración
    content_to_return = cleaned_content if json_valid else response_content
    return content_to_return, metrics

# --- Función para Guardar Resultados (Adaptada) ---

def guardar_resultado_llm(test_id: str, tarea: str, model_id: str, content: Optional[str], metrics: Dict[str, Any], output_dir: Path):
    """Guarda la respuesta del LLM (limpia si es válida) en un archivo JSON."""
    # Crear subdirectorio para el test_id si no existe
    test_dir = output_dir / test_id
    test_dir.mkdir(parents=True, exist_ok=True)

    # Nombre de archivo basado en la tarea
    filename = f"{tarea}.json"
    filepath = test_dir / filename

    # Guardar el contenido y metadatos del resultado
    result_data = {
        "test_id": test_id,
        "tarea": tarea,
        "model_id": model_id, # Será siempre MODEL_TO_TEST
        "success": metrics["success"],
        "api_success": metrics["api_success"],
        "json_valid": metrics["json_valid"],
        "error_message": metrics["error_message"],
        # Guardar el contenido que se devolvió (limpio si era válido, original si no)
        "llm_response_content": content if content is not None else "Error: No content received or generated"
    }

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result_data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.error(f"[{test_id}][{tarea}][{model_id}] Error guardando resultado en {filepath}: {e}")

def guardar_metricas_csv(metrics: Dict[str, Any], csv_filepath: Path):
    """Añade una fila de métricas a un archivo CSV."""
    try:
        # Asegurar que el directorio del CSV existe
        csv_filepath.parent.mkdir(parents=True, exist_ok=True)
        write_header = not csv_filepath.exists() or csv_filepath.stat().st_size == 0
        # Añadir nuevos campos al header
        fieldnames = [
            "test_id", "tarea", "model_id", "timestamp_utc",
            "latency_seconds", "prompt_tokens", "completion_tokens",
            "total_tokens", "success", "api_success", "json_valid", "error_message"
        ]
        with open(csv_filepath, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            if write_header:
                writer.writeheader()
            writer.writerow(metrics)
    except Exception as e:
        # Loggear con más detalle el error de escritura
        logger.error(f"Error guardando métricas en {csv_filepath} para {metrics.get('test_id', 'N/A')}: {e}", exc_info=True)


# --- Lógica Principal Asíncrona (Adaptada) ---

async def procesar_articulo(client: AsyncGroq, article_path: Path, output_dir_base: Path, csv_filepath: Path):
    """Procesa un único artículo con todas las tareas usando MODEL_TO_TEST."""
    test_id = article_path.stem
    logger.info(f"--- Procesando Artículo: {test_id} ---")

    articulo = load_article(article_path)
    if not articulo:
        logger.warning(f"Omitiendo artículo {test_id} debido a error de carga.")
        # Registrar fallo de carga si se desea
        metrics = {
             "test_id": test_id, "tarea": "carga_articulo", "model_id": MODEL_TO_TEST,
             "timestamp_utc": datetime.now(timezone.utc).isoformat(),
             "latency_seconds": 0, "prompt_tokens": None, "completion_tokens": None,
             "total_tokens": None, "success": False, "api_success": False, "json_valid": False,
             "error_message": f"Failed to load article from {article_path}"
         }
        guardar_metricas_csv(metrics, csv_filepath)
        return

    # Crear lista de corutinas a ejecutar
    tasks_coroutines = []
    task_info_map = {} # Para mapear corutina a tarea
    for idx, tarea in enumerate(TASKS):
        prompt = generar_prompt(tarea, articulo)
        if not prompt:
            logger.warning(f"[{test_id}][{tarea}] Prompt vacío, omitiendo tarea.")
            continue
        # Crear la corutina
        coro = llamar_groq_con_metricas(
            client=client,
            model_id=MODEL_TO_TEST,
            prompt=prompt,
            test_id=test_id,
            tarea=tarea
        )
        tasks_coroutines.append(coro)
        task_info_map[id(coro)] = {"index": idx, "tarea": tarea} # Guardar info asociada

    if not tasks_coroutines:
        logger.warning(f"[{test_id}] No hay tareas para procesar.")
        return

    # Ejecutar todas las llamadas a Groq para este artículo en paralelo
    logger.info(f"[{test_id}] Lanzando {len(tasks_coroutines)} llamadas a Groq para {MODEL_TO_TEST}...")
    results_or_exceptions = await tqdm_asyncio.gather(
        *tasks_coroutines,
        desc=f"[{test_id}] Llamadas Groq",
        leave=False,
        return_exceptions=True # Capturar excepciones de reintentos fallidos aquí
    )

    # Procesar y guardar resultados
    for i, result_or_exception in enumerate(results_or_exceptions):
         # Identificar la tarea asociada a este resultado/excepción
         # Es más seguro si la función llamada devuelve la tarea en las métricas
         # Si es una excepción, necesitamos inferirla (con cuidado)
        tarea_actual = TASKS[i] # Asumimos que el orden se mantiene si no se omitió ninguna tarea

        if isinstance(result_or_exception, Exception):
            # Esto ocurre si @retry falla todos los intentos y reraise=True
            logger.error(f"[{test_id}][{tarea_actual}][{MODEL_TO_TEST}] Excepción no manejada por reintentos: {result_or_exception}")
            # Registrar métricas de fallo total
            metrics = {
                "test_id": test_id, "tarea": tarea_actual, "model_id": MODEL_TO_TEST,
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "latency_seconds": None, "prompt_tokens": None, "completion_tokens": None,
                "total_tokens": None, "success": False, "api_success": False, "json_valid": False,
                "error_message": f"Unhandled Exception: {type(result_or_exception).__name__}: {str(result_or_exception)}"
            }
            # Guardar indicativo de error y métricas
            guardar_resultado_llm(test_id, tarea_actual, MODEL_TO_TEST, None, metrics, output_dir_base)
            guardar_metricas_csv(metrics, csv_filepath)
        else:
            # La llamada (con reintentos) tuvo éxito o falló de forma controlada
            response_content, metrics = result_or_exception
            # Asegurarnos de usar la tarea correcta de las métricas
            tarea_actual = metrics['tarea']
            guardar_resultado_llm(test_id, tarea_actual, MODEL_TO_TEST, response_content, metrics, output_dir_base)
            guardar_metricas_csv(metrics, csv_filepath)

    logger.info(f"--- Artículo {test_id} completado ---")


async def main():
    """Función principal del script de testeo de prompts."""
    start_time_script = time.time()
    logger.info(f"--- Iniciando Script de Testeo de Prompts (Modelo: {MODEL_TO_TEST}) ---")

    try:
        api_key = load_api_key()
        # Inicializar el cliente AsyncGroq
        # Aumentar timeout por si acaso con prompts más largos/complejos
        client = AsyncGroq(api_key=api_key, timeout=120.0)
        logger.info("Cliente AsyncGroq inicializado.")
    except ValueError:
        return

    OUTPUT_DIR_BASE.mkdir(parents=True, exist_ok=True)
    logger.info(f"Directorio de resultados: {OUTPUT_DIR_BASE.resolve()}")
    logger.info(f"Archivo de métricas: {METRICS_FILE.resolve()}")

    # Limpiar archivo de métricas anterior si existe
    if METRICS_FILE.exists():
        logger.info(f"Eliminando archivo de métricas anterior: {METRICS_FILE}")
        METRICS_FILE.unlink()

    try:
        test_files_gen = INPUT_DIR.glob("test_*.json")
        test_files = sorted(list(test_files_gen))
        if not test_files:
             raise FileNotFoundError(f"No se encontraron archivos test_*.json en {INPUT_DIR}")
        logger.info(f"Encontrados {len(test_files)} archivos de prueba en {INPUT_DIR.resolve()}")
    except FileNotFoundError as fnf_error:
         logger.error(f"Error: {fnf_error}")
         return
    except Exception as e:
        logger.error(f"Error inesperado listando archivos de prueba: {e}")
        return

    # Procesar artículos concurrentemente
    CONCURRENCY_LIMIT = 5 # Mantener concurrencia razonable
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

    async def process_with_semaphore(article_path):
        async with semaphore:
            await procesar_articulo(client, article_path, OUTPUT_DIR_BASE, METRICS_FILE)

    processing_tasks = [process_with_semaphore(fp) for fp in test_files]

    logger.info(f"Iniciando procesamiento de {len(test_files)} artículos con concurrencia {CONCURRENCY_LIMIT}...")
    await tqdm_asyncio.gather(*processing_tasks, desc="Progreso General Artículos")


    end_time_script = time.time()
    logger.info("--- Testeo de Prompts Completado ---")
    logger.info(f"Resultados LLM guardados en subdirectorios dentro de: {OUTPUT_DIR_BASE.resolve()}")
    logger.info(f"Métricas guardadas en: {METRICS_FILE.resolve()}")
    logger.info(f"Tiempo total de ejecución del script: {time.time() - start_time_script:.2f} segundos")

# --- Punto de Entrada ---
if __name__ == "__main__":
    # Añadir manejo de httpx si es necesario aquí o en la función main
    # import httpx # Asegurar que esté importado si usamos los límites
    asyncio.run(main())
