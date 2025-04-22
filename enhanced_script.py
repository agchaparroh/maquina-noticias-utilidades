#!/usr/bin/env python3
"""
Script mejorado para testeo de prompts usando llama3-8b-8192 (por defecto) y
llama3-8b-instant (para artículos largos que necesitan ventana de contexto amplia).

Características:
- Selección automática de modelo según la longitud del contenido
- Recuperación automática ante fallos mediante puntos de control
- Configuración flexible mediante variables de entorno
- Cacheo de respuestas para desarrollo
- Validación más robusta con JSON Schema
- Generación de reportes y gráficos de análisis
- Optimización dinámica del umbral de tokens
- Monitoreo detallado del progreso
- Verificación de dependencias
"""
import os
import sys
import json
import time
import logging
import asyncio
import csv
import re
import shutil
import subprocess
from pathlib import Path
from datetime import datetime, timezone, timedelta
from typing import Optional, Tuple, Dict, Any, List, Set
from concurrent.futures import ProcessPoolExecutor
import importlib.util

# --- Verificación inicial de dependencias críticas ---
def verificar_dependencia(paquete):
    return importlib.util.find_spec(paquete) is not None

DEPS_CRITICAS = ["groq", "tenacity", "tqdm"]
deps_faltantes = [dep for dep in DEPS_CRITICAS if not verificar_dependencia(dep)]

if deps_faltantes:
    print(f"DEPENDENCIAS CRÍTICAS FALTANTES: {', '.join(deps_faltantes)}")
    print("Por favor, instálelas antes de continuar:")
    print(f"pip install {' '.join(deps_faltantes)}")
    sys.exit(1)

# --- Importar dependencias principales ---
from groq import AsyncGroq, GroqError, APITimeoutError, RateLimitError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from tqdm.asyncio import tqdm_asyncio

# --- Configuración mediante variables de entorno ---
CONFIG = {
    # Modelos a utilizar
    "MODELO_ESTANDAR": os.environ.get("MODELO_ESTANDAR", "llama3-8b-8192"),
    "MODELO_CONTEXTO_AMPLIO": os.environ.get("MODELO_CONTEXTO_AMPLIO", "llama3-8b-instant"),
    
    # Umbral de tokens para cambiar al modelo de contexto amplio
    "UMBRAL_TOKENS": int(os.environ.get("UMBRAL_TOKENS", "7000")),
    
    # Directorios
    "INPUT_DIR": os.environ.get("INPUT_DIR", "../data/benchmark_test_set"),
    "OUTPUT_DIR_BASE": os.environ.get("OUTPUT_DIR_BASE", "./prompt_test_results"),
    
    # Parámetros de ejecución
    "CONCURRENCY_LIMIT": int(os.environ.get("CONCURRENCY_LIMIT", "2")),
    "REINTENTOS_MAX": int(os.environ.get("REINTENTOS_MAX", "7")),
    "TIEMPO_ESPERA_API": int(os.environ.get("TIEMPO_ESPERA_API", "180")),
    "DEFAULT_TEMPERATURE": float(os.environ.get("DEFAULT_TEMPERATURE", "0.2")),
    "DEFAULT_MAX_TOKENS": int(os.environ.get("DEFAULT_MAX_TOKENS", "4096")),
    
    # Características avanzadas
    "PERMITIR_RECUPERACION": os.environ.get("PERMITIR_RECUPERACION", "true").lower() == "true",
    "USAR_CACHE": os.environ.get("USAR_CACHE", "false").lower() == "true",
    "GENERAR_REPORTES": os.environ.get("GENERAR_REPORTES", "true").lower() == "true",
    "GENERAR_GRAFICOS": os.environ.get("GENERAR_GRAFICOS", "false").lower() == "true",
    "MODO_DEBUG": os.environ.get("MODO_DEBUG", "false").lower() == "true",
    "MODO_SILENCIOSO": os.environ.get("MODO_SILENCIOSO", "false").lower() == "true",
    "OPTIMIZAR_PROMPTS": os.environ.get("OPTIMIZAR_PROMPTS", "true").lower() == "true",
    "VALIDAR_ESQUEMAS": os.environ.get("VALIDAR_ESQUEMAS", "true").lower() == "true"
}

# --- Configuración derivada ---
# Rutas de directorios
INPUT_DIR = Path(CONFIG["INPUT_DIR"])
OUTPUT_DIR_BASE = Path(CONFIG["OUTPUT_DIR_BASE"])
CACHE_DIR = OUTPUT_DIR_BASE / "cache"
REPORTS_DIR = OUTPUT_DIR_BASE / "reports"
LOGS_DIR = OUTPUT_DIR_BASE / "logs"

# Archivos importantes
METRICS_FILE = OUTPUT_DIR_BASE / "prompt_test_metrics.csv"
CHECKPOINT_FILE = OUTPUT_DIR_BASE / "checkpoint.json"
LOG_FILE = LOGS_DIR / f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Constantes para el script
MODELO_ESTANDAR = CONFIG["MODELO_ESTANDAR"]
MODELO_CONTEXTO_AMPLIO = CONFIG["MODELO_CONTEXTO_AMPLIO"]
UMBRAL_TOKENS = CONFIG["UMBRAL_TOKENS"]
USAR_CACHE = CONFIG["USAR_CACHE"]
PERMITIR_RECUPERACION = CONFIG["PERMITIR_RECUPERACION"]
VALIDAR_ESQUEMAS = CONFIG["VALIDAR_ESQUEMAS"]

# Lista de tareas a procesar
TASKS = [
    "relevancia",           # Fase 2
    "extraccion_hechos",    # Fase 3a
    "extraccion_entidades", # Fase 3b
    "extraccion_citas",     # Fase 3c
    "extraccion_datos"      # Fase 3d
]

# --- Verificación y carga de dependencias opcionales ---
def verificar_dependencias_opcionales():
    """Verifica e intenta instalar dependencias opcionales si es necesario."""
    deps_opcionales = {
        "tiktoken": "Contador de tokens preciso",
        "jsonschema": "Validación avanzada de JSON",
        "pandas": "Análisis y reportes",
        "matplotlib": "Generación de gráficos",
        "tabulate": "Formateo de reportes"
    }
    
    # Estado de instalación
    deps_status = {}
    
    # Verificar cada dependencia
    for dep, descripcion in deps_opcionales.items():
        if verificar_dependencia(dep):
            deps_status[dep] = True
        else:
            deps_status[dep] = False
            if not CONFIG["MODO_SILENCIOSO"]:
                print(f"Dependencia opcional no encontrada: {dep} - {descripcion}")
    
    # Reportar dependencias faltantes importantes
    if not deps_status.get("tiktoken", False):
        print("ADVERTENCIA: 'tiktoken' no está instalado. La estimación de tokens será menos precisa.")
    
    if not deps_status.get("jsonschema", False) and VALIDAR_ESQUEMAS:
        print("ADVERTENCIA: 'jsonschema' no está instalado. La validación de esquemas estará deshabilitada.")
    
    # Ofrecer instalación si no estamos en modo silencioso
    if not CONFIG["MODO_SILENCIOSO"] and not all(deps_status.values()):
        deps_faltantes = [dep for dep, status in deps_status.items() if not status]
        print(f"Saltando instalación de dependencias opcionales: {', '.join(deps_faltantes)}")
        # Modo no interactivo: no solicitamos input
        # if input(f"¿Desea instalar las dependencias opcionales faltantes? ({', '.join(deps_faltantes)}) [s/n]: ").lower() == 's':
        #     for dep in deps_faltantes:
        #         try:
        #             print(f"Instalando {dep}...")
        #             subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
        #             deps_status[dep] = True
        #             print(f"✓ {dep} instalado correctamente.")
        #         except Exception as e:
        #             print(f"✗ Error instalando {dep}: {e}")
    
    return deps_status

# Ejecutar verificación de dependencias
DEPS_STATUS = verificar_dependencias_opcionales()

# Intentar importar dependencias opcionales
tiktoken_disponible = DEPS_STATUS.get("tiktoken", False)
jsonschema_disponible = DEPS_STATUS.get("jsonschema", False)
pandas_disponible = DEPS_STATUS.get("pandas", False)
matplotlib_disponible = DEPS_STATUS.get("matplotlib", False)
tabulate_disponible = DEPS_STATUS.get("tabulate", False)

if tiktoken_disponible:
    import tiktoken
if jsonschema_disponible and VALIDAR_ESQUEMAS:
    import jsonschema
if pandas_disponible and CONFIG["GENERAR_REPORTES"]:
    import pandas as pd
if matplotlib_disponible and CONFIG["GENERAR_GRAFICOS"]:
    import matplotlib.pyplot as plt

# --- Configuración de Logging ---
def configurar_logging():
    """Configura el sistema de logging."""
    # Crear directorio de logs si no existe
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Configurar nivel de logging según modo
    nivel = logging.DEBUG if CONFIG["MODO_DEBUG"] else logging.INFO
    
    # Configurar formato
    formato = '%(asctime)s - %(levelname)s - %(message)s'
    
    # Configurar logging
    logging.basicConfig(
        level=nivel,
        format=formato,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Obtener logger
    logger = logging.getLogger(__name__)
    
    # Silenciar loggers externos demasiado verbosos
    if not CONFIG["MODO_DEBUG"]:
        logging.getLogger("httpx").setLevel(logging.WARNING)
    
    return logger

# Configurar logging
logger = configurar_logging()

# --- Esquemas de validación JSON ---
JSON_SCHEMAS = {
    "relevancia": {
        "type": "object",
        "required": ["puntuacion_relevancia", "justificacion_relevancia", "categorias_asignadas", "explicacion_concisa"],
        "properties": {
            "puntuacion_relevancia": {"type": "integer", "minimum": 0, "maximum": 10},
            "justificacion_relevancia": {"type": "string", "minLength": 1},
            "categorias_asignadas": {
                "type": "array", 
                "minItems": 1, 
                "maxItems": 4,
                "items": {"type": "string"}
            },
            "explicacion_concisa": {"type": "string", "minLength": 1}
        }
    },
    "extraccion_hechos": {
        "type": "object",
        "required": ["resultados"],
        "properties": {
            "resultados": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["contenido", "tipo_hecho", "fecha_ocurrencia_inicio", "precision_temporal", 
                               "paises", "ubicaciones_especificas", "importancia", "confiabilidad", 
                               "etiquetas", "es_evento_futuro"],
                    "properties": {
                        "tipo_hecho": {"type": "string", "enum": ["SUCESO", "ANUNCIO", "DECLARACION", "BIOGRAFIA", "CONCEPTO", "NORMATIVA", "EVENTO"]}
                    }
                }
            }
        }
    },
    "extraccion_entidades": {
        "type": "object",
        "required": ["resultados"],
        "properties": {
            "resultados": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["nombre", "tipo", "alias"],
                    "properties": {
                        "nombre": {"type": "string", "minLength": 1},
                        "tipo": {"type": "string", "enum": ["PERSONA", "ORGANIZACION", "INSTITUCION", "LUGAR", "EVENTO", "NORMATIVA", "CONCEPTO", "OTRO"]},
                        "alias": {"type": "array", "items": {"type": "string"}}
                    }
                }
            }
        }
    },
    "extraccion_citas": {
        "type": "object",
        "required": ["resultados"],
        "properties": {
            "resultados": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["cita", "emisor_nombre"],
                    "properties": {
                        "cita": {"type": "string", "minLength": 1},
                        "emisor_nombre": {"type": "string", "minLength": 1}
                    }
                }
            }
        }
    },
    "extraccion_datos": {
        "type": "object",
        "required": ["resultados"],
        "properties": {
            "resultados": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["indicador", "categoria", "valor_numerico", "unidad", "ambito_geografico"],
                    "properties": {
                        "valor_numerico": {"type": "number"},
                        "ambito_geografico": {"type": "array"}
                    }
                }
            }
        }
    }
}

# --- Funciones de manejo de puntos de control ---
def cargar_checkpoint() -> Set[str]:
    """Carga el conjunto de archivos ya procesados desde el checkpoint."""
    procesados = set()
    
    if PERMITIR_RECUPERACION and CHECKPOINT_FILE.exists():
        try:
            with open(CHECKPOINT_FILE, 'r') as f:
                checkpoint = json.load(f)
                procesados = set(checkpoint.get("procesados", []))
                timestamp = checkpoint.get("timestamp")
                
                logger.info(f"Checkpoint cargado del {timestamp}")
                logger.info(f"Artículos ya procesados: {len(procesados)}")
        except Exception as e:
            logger.warning(f"Error cargando checkpoint: {e}")
    
    return procesados

def guardar_checkpoint(procesados: Set[str]):
    """Guarda el conjunto de archivos procesados en el checkpoint."""
    if not PERMITIR_RECUPERACION:
        return
    
    checkpoint = {
        "procesados": list(procesados),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    
    try:
        with open(CHECKPOINT_FILE, 'w') as f:
            json.dump(checkpoint, f)
    except Exception as e:
        logger.warning(f"Error guardando checkpoint: {e}")

# --- Funciones de caché ---
def cargar_de_cache(test_id: str, tarea: str, model_id: str) -> Optional[Tuple[str, Dict[str, Any]]]:
    """Intenta cargar una respuesta previamente guardada de la caché."""
    if not USAR_CACHE:
        return None
    
    cache_path = CACHE_DIR / f"{test_id}_{tarea}_{model_id}.json"
    if cache_path.exists():
        try:
            with open(cache_path, 'r') as f:
                data = json.load(f)
                # Devolver tanto el contenido como las métricas
                return data.get("content"), data.get("metrics")
        except Exception as e:
            logger.warning(f"Error cargando caché: {e}")
    
    return None

def guardar_en_cache(test_id: str, tarea: str, model_id: str, content: str, metrics: Dict[str, Any]):
    """Guarda una respuesta en la caché para uso futuro."""
    if not USAR_CACHE:
        return
    
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / f"{test_id}_{tarea}_{model_id}.json"
    
    try:
        with open(cache_path, 'w') as f:
            json.dump({
                "content": content,
                "metrics": metrics,
                "cached_at": datetime.now(timezone.utc).isoformat()
            }, f)
    except Exception as e:
        logger.warning(f"Error guardando en caché: {e}")

# --- Funciones auxiliares ---
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

def contar_tokens(texto: str) -> int:
    """Cuenta aproximadamente el número de tokens en un texto."""
    if tiktoken_disponible:
        try:
            # Usar el tokenizador de GPT-4 como aproximación
            enc = tiktoken.encoding_for_model("gpt-4")
            return len(enc.encode(texto))
        except Exception as e:
            logger.warning(f"Error con tiktoken: {e}. Usando estimación por caracteres.")
    
    # Estimación simple basada en caracteres
    return len(texto) // 4

def optimizar_umbral_tokens() -> int:
    """Analiza datos de ejecución para determinar un umbral óptimo de tokens."""
    if not pandas_disponible or not os.path.exists(METRICS_FILE):
        return UMBRAL_TOKENS
    
    try:
        # Cargar métricas
        df = pd.read_csv(METRICS_FILE)
        
        if len(df) < 10:  # Necesitamos suficientes datos para un análisis significativo
            return UMBRAL_TOKENS
        
        # Análisis básico: esta implementación podría ser más sofisticada
        # con datos adicionales como el conteo de tokens por artículo
        modelo_estandar_success = df[df['model_id'] == MODELO_ESTANDAR]['success'].mean()
        modelo_amplio_success = df[df['model_id'] == MODELO_CONTEXTO_AMPLIO]['success'].mean()
        
        # Si el modelo estándar tiene buen rendimiento, podemos aumentar el umbral
        if modelo_estandar_success > 0.95:
            nuevo_umbral = UMBRAL_TOKENS * 1.1  # Aumentar 10%
        # Si el modelo amplio está teniendo mejor rendimiento, reducir umbral
        elif modelo_amplio_success > modelo_estandar_success + 0.1:
            nuevo_umbral = UMBRAL_TOKENS * 0.9  # Reducir 10%
        else:
            nuevo_umbral = UMBRAL_TOKENS
        
        logger.info(f"Umbral optimizado: {nuevo_umbral:.0f} tokens (anterior: {UMBRAL_TOKENS})")
        return int(nuevo_umbral)
    except Exception as e:
        logger.warning(f"Error optimizando umbral de tokens: {e}")
        return UMBRAL_TOKENS

def seleccionar_modelo(articulo: Dict[str, Any]) -> str:
    """
    Selecciona el modelo adecuado basándose en la longitud del contenido del artículo.
    """
    # Obtener el texto del artículo
    contenido = articulo.get("contenido_texto", "")
    titulo = articulo.get("titular", "")
    
    # El texto completo que se usará en el prompt
    texto_completo = f"{titulo}\n\n{contenido}"
    
    # Contar tokens
    num_tokens = contar_tokens(texto_completo)
    
    # Seleccionar modelo según el umbral
    if num_tokens > UMBRAL_TOKENS:
        logger.info(f"Artículo largo detectado ({num_tokens} tokens). Usando modelo de contexto amplio.")
        return MODELO_CONTEXTO_AMPLIO
    else:
        logger.info(f"Artículo de longitud normal ({num_tokens} tokens). Usando modelo estándar.")
        return MODELO_ESTANDAR

def _clean_json_string(raw_string: Optional[str]) -> Optional[str]:
    """
    Intenta extraer el primer bloque JSON válido (objeto o array) de una cadena.
    Elimina texto antes del primer '{' o '[' y después del último '}' o ']'.
    Incluye correcciones específicas para problemas comunes en citas y estructuras.
    """
    if not raw_string:
        return None

    # 1. Intentar extraer el bloque JSON más obvio (objeto o array)
    json_match = re.search(r'^\s*(\{.*\}|\[.*\])\s*', raw_string, re.DOTALL)
    if json_match:
        potential_json = json_match.group(1)
        try:
            json.loads(potential_json)
            return potential_json # Ya es válido
        except json.JSONDecodeError:
            logger.debug("JSON inicial no válido o con texto extra, intentando limpiar...")

    # 2. Si no es válido directamente, intentar reparaciones comunes
    fixed_string = raw_string

    # 2a. Eliminar texto antes del primer '{' o '[' y después del último '}' o ']'
    start_brace = fixed_string.find('{')
    start_bracket = fixed_string.find('[')
    end_brace = fixed_string.rfind('}')
    end_bracket = fixed_string.rfind(']')

    start_index = -1
    end_index = -1

    if start_brace != -1 and end_brace != -1:
        start_index = start_brace
        end_index = end_brace
    if start_bracket != -1 and end_bracket != -1:
        if start_index == -1 or start_bracket < start_index:
            start_index = start_bracket
        if end_index == -1 or end_bracket > end_index:
             # Cuidado con arrays dentro de objetos, priorizar el cierre del tipo de apertura
             if start_index == start_bracket:
                  end_index = end_bracket
             # Si empieza con { y termina con ], es raro, pero mantenemos el brace/bracket
             # Si empieza con [ y termina con }, también raro.
             # La lógica simple es tomar el rango más amplio
             elif end_bracket > end_brace:
                 end_index = end_bracket

    if start_index != -1 and end_index != -1 and start_index < end_index:
        fixed_string = fixed_string[start_index : end_index + 1]
    else:
         logger.warning("No se pudo determinar un bloque JSON principal claro.")
         # Aún así, intentar las siguientes reparaciones sobre la cadena original limpia de espacios
         fixed_string = raw_string.strip()

    # 2b. Reemplazar comillas simples por dobles en keys
    fixed_string = re.sub(r"'\s*([^'\s]+)\s*'\s*:", r'"\1":', fixed_string)

    # 2c. Corregir problemas específicos de comillas en citas
    # Problema común: ""texto"" -> "texto"
    fixed_string = re.sub(r'"cita":\s*""([^"]*?)""', r'"cita": "\1"', fixed_string)
    
    # 2d. Corregir comillas anidadas sin escapar
    # Buscar patrones como: "cita": ""Texto "con comillas" internas""
    fixed_string = re.sub(r'"cita":\s*"([^"]*)"([^"]*)"([^"]*)"', r'"cita": "\1\\\"\2\\\"\3"', fixed_string)
    
    # 2e. Corregir estructuras de entidades con llaves faltantes
    # Problema: }, "nombre": ... (falta la llave de apertura)
    fixed_string = re.sub(r'\},\s*"nombre":', r'}, {"nombre":', fixed_string)

    # 2f. Asegurarse de que null, true, false están en minúsculas
    fixed_string = re.sub(r'\bNone\b', 'null', fixed_string) # Python None -> JSON null
    fixed_string = re.sub(r'\bTrue\b', 'true', fixed_string) # Python True -> JSON true
    fixed_string = re.sub(r'\bFalse\b', 'false', fixed_string) # Python False -> JSON false

    # 2g. Eliminar comas finales antes de '}' o ']' (causa común de error)
    fixed_string = re.sub(r",\s*(\}|\])", r"\1", fixed_string)

    # 3. Intentar parsear el string reparado
    try:
        json.loads(fixed_string)
        logger.info("JSON reparado exitosamente.")
        return fixed_string
    except json.JSONDecodeError as e:
        logger.error(f"Falló la reparación del JSON: {e}. Devolviendo None.")
        return None

# --- Generación de Prompts ---
def generar_prompt_base(tarea: str, articulo: dict) -> str:
    """Genera el prompt base para una tarea y un artículo."""
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

EJEMPLO DE FORMATO ESPERADO:
{{
  "resultados": [
    {{
      "contenido": "Descripción concisa del primer hecho...",
      "tipo_hecho": "SUCESO",
      "fecha_ocurrencia_inicio": "2025-04-15T10:00:00Z",
      "fecha_ocurrencia_fin": null,
      "precision_temporal": "exacta",
      "paises": ["ES", "AR"],
      "ubicaciones_especificas": ["Madrid", "Congreso"],
      "importancia": 8,
      "confiabilidad": 5,
      "etiquetas": ["política", "acuerdo", "gobierno"],
      "es_evento_futuro": false,
      "estado_programacion": null
    }},
    {{
      "contenido": "Explicación del concepto de 'lawfare'...",
      "tipo_hecho": "CONCEPTO",
      "fecha_ocurrencia_inicio": "2025-04-15", 
      "fecha_ocurrencia_fin": null,
      "precision_temporal": "dia", 
      "paises": [],
      "ubicaciones_especificas": [],
      "importancia": 6,
      "confiabilidad": 4,
      "etiquetas": ["justicia", "política", "definición", "lawfare"],
      "es_evento_futuro": false,
      "estado_programacion": null
    }}
  ]
}}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    elif tarea == "extraccion_entidades":
        # Prompt REVISADO basado en Fase 3b - Extracción Entidades con mejor estructura JSON
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
- **Estructura correcta:** Asegúrate de que cada entidad tenga su propia estructura completa con apertura y cierre adecuados. Cada objeto JSON debe tener sus llaves de apertura y cierre.
- **Formato correcto:** Verifica que el formato JSON sea válido.
- **JSON Final:** La respuesta COMPLETA debe ser un ÚNICO objeto JSON que contenga UNA sola clave llamada "resultados". El valor de "resultados" DEBE ser la lista JSON de los objetos de entidades extraídos. Ejemplo: {{"resultados": [ {{entidad1}}, {{entidad2}}, ... ]}}. NO incluyas NINGÚN texto antes o después de este objeto JSON principal. Verifica la validez del JSON.

EJEMPLO DE FORMATO CORRECTO:
{{
  "resultados": [
    {{
      "nombre": "Pedro Sánchez Pérez-Castejón",
      "tipo": "PERSONA",
      "alias": ["Pedro Sánchez", "Sánchez"]
    }},
    {{
      "nombre": "Organización de las Naciones Unidas (ONU)",
      "tipo": "INSTITUCION",
      "alias": ["ONU", "Naciones Unidas"]
    }}
  ]
}}

Texto a analizar:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    elif tarea == "extraccion_citas":
        # Prompt REVISADO basado en Fase 3c - Extracción Citas con mejor manejo de comillas
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
- **Formato correcto de comillas:** Si la cita original contiene comillas internas, asegúrate de escaparlas correctamente en JSON. 
  Por ejemplo, si la cita original es 'El presidente dijo "no abandonaremos el país"', en el JSON debe aparecer como: "El presidente dijo \\"no abandonaremos el país\\"".
- **JSON Final:** La respuesta COMPLETA debe ser un ÚNICO objeto JSON que contenga UNA sola clave llamada "resultados". El valor de "resultados" DEBE ser la lista JSON de los objetos de citas extraídos. Ejemplo: {{"resultados": [ {{cita1}}, {{cita2}}, ... ]}}. NO incluyas NINGÚN texto antes o después de este objeto JSON principal. Verifica la validez del JSON.

EJEMPLOS CORRECTOS DE CITAS CON COMILLAS:

Ejemplo 1:
Texto original: María dijo: "El gobierno es ineficiente".
JSON correcto: {{"cita": "El gobierno es ineficiente", "emisor_nombre": "María", "contexto": null, "fecha_cita": null}}

Ejemplo 2:
Texto original: "El presidente afirmó que 'nunca permitiré' este tipo de acciones", señaló el ministro.
JSON correcto: {{"cita": "El presidente afirmó que 'nunca permitiré' este tipo de acciones", "emisor_nombre": "ministro", "contexto": null, "fecha_cita": null}}

Ejemplo 3:
Texto original: "Cuando el gobernador dijo \\"no negociaremos con terroristas\\" estaba mintiendo", declaró la oposición.
JSON correcto: {{"cita": "Cuando el gobernador dijo \\\\"no negociaremos con terroristas\\\\" estaba mintiendo", "emisor_nombre": "oposición", "contexto": null, "fecha_cita": null}}

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

EJEMPLO DE FORMATO ESPERADO:
{{
  "resultados": [
    {{
      "indicador": "Tasa de inflación interanual",
      "categoria": "económico",
      "valor_numerico": 5.7,
      "unidad": "%",
      "ambito_geografico": ["España"],
      "periodo_referencia_inicio": "2024-03-01",
      "periodo_referencia_fin": "2025-03-31",
      "tipo_periodo": "anual",
      "fuente_especifica": "INE",
      "notas_contexto": "Dato provisional"
    }},
    {{
      "indicador": "Presupuesto de Defensa",
      "categoria": "presupuestario",
      "valor_numerico": 1500000000.0,
      "unidad": "USD",
      "ambito_geografico": ["Colombia"],
      "periodo_referencia_inicio": "2025-01-01",
      "periodo_referencia_fin": "2025-12-31",
      "tipo_periodo": "anual",
      "fuente_especifica": null,
      "notas_contexto": null
    }}
  ]
}}

Texto a analizar:
{contenido}

Respuesta (objeto JSON con clave "resultados"):
"""
        return prompt.strip()

    else:
        logger.warning(f"Tarea desconocida: {tarea}. Generando prompt vacío.")
        return ""

def generar_prompt(tarea: str, articulo: dict, modelo: str) -> str:
    """
    Genera el prompt optimizado para una tarea, artículo y modelo específico.
    Aplica ajustes específicos según el modelo utilizado.
    """
    # Obtener el prompt base
    prompt_base = generar_prompt_base(tarea, articulo)
    
    # Si no hay optimización de prompts o es el modelo estándar, devolver el prompt base
    if not CONFIG["OPTIMIZAR_PROMPTS"] or modelo == MODELO_ESTANDAR:
        return prompt_base
    
    # Ajustes específicos para el modelo de contexto amplio
    if modelo == MODELO_CONTEXTO_AMPLIO:
        # Para tareas que pueden beneficiarse de una ventana de contexto mayor
        if tarea in ["extraccion_hechos", "extraccion_entidades"]:
            prompt_adicional = """
NOTA IMPORTANTE SOBRE EXHAUSTIVIDAD: 
Dado que estás procesando un texto largo, asegúrate de analizar TODO el contenido para extraer información relevante, no solo las primeras o últimas partes. El artículo puede contener información importante distribuida a lo largo de todo el texto que debe ser capturada completamente.
"""
            return prompt_base + prompt_adicional
    
    # En cualquier otro caso, devolver el prompt base sin modificaciones
    return prompt_base

# --- Función Principal de Llamada a Groq (Con Limpieza y Validación JSON) ---
RETRYABLE_ERRORS = (APITimeoutError, RateLimitError, GroqError)

@retry(
    stop=stop_after_attempt(CONFIG["REINTENTOS_MAX"]),
    wait=wait_exponential(multiplier=2, min=10, max=120),
    retry=retry_if_exception_type(RETRYABLE_ERRORS),
    reraise=True # Re-lanza la excepción si todos los reintentos fallan
)
async def llamar_groq_con_metricas(
    client: AsyncGroq,
    model_id: str,
    prompt: str,
    test_id: str,
    tarea: str,
    temperature: float = CONFIG["DEFAULT_TEMPERATURE"],
    max_tokens: int = CONFIG["DEFAULT_MAX_TOKENS"],
    response_format: Dict[str, str] = {"type": "json_object"}
) -> Tuple[Optional[str], Dict[str, Any]]:
    """Llama a Groq, mide métricas, limpia, valida JSON y maneja errores/reintentos."""
    # Intentar obtener de caché
    cached_result = cargar_de_cache(test_id, tarea, model_id)
    if cached_result:
        cached_content, cached_metrics = cached_result
        logger.info(f"[{test_id}][{tarea}][{model_id}] Usando resultado en caché")
        return cached_content, cached_metrics
    
    # Inicializar variables
    start_time = time.time()
    error_message: Optional[str] = None
    api_success: bool = False
    json_valid: bool = False
    response_content: Optional[str] = None
    usage_data: Optional[Any] = None
    latency: float = 0.0
    cleaned_content: Optional[str] = None
    schema_valid: bool = False

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
        api_success = True
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
                    
                    # Validación de esquema
                    if jsonschema_disponible and VALIDAR_ESQUEMAS and tarea in JSON_SCHEMAS:
                        try:
                            jsonschema.validate(instance=json_parsed, schema=JSON_SCHEMAS[tarea])
                            schema_valid = True
                            logger.debug(f"[{test_id}][{tarea}][{model_id}] Validación de esquema exitosa.")
                        except Exception as schema_err:
                            logger.warning(f"[{test_id}][{tarea}][{model_id}] Error de validación de esquema: {schema_err}")
                            # No fallamos por errores de esquema, solo registramos
                    else:
                        schema_valid = True  # Si no hay validación, asumimos que es válido
                    
                    # Si todo va bien con la estructura básica:
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
        api_success = False
        json_valid = False

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
        "success": success,
        "api_success": api_success,
        "json_valid": json_valid,
        "schema_valid": schema_valid,
        "error_message": error_message
    }

    # Guardar en caché si fue exitoso
    content_to_return = cleaned_content if json_valid else response_content
    if success and content_to_return:
        guardar_en_cache(test_id, tarea, model_id, content_to_return, metrics)

    return content_to_return, metrics

# --- Función para Guardar Resultados ---
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
        "model_id": model_id,
        "success": metrics["success"],
        "api_success": metrics["api_success"],
        "json_valid": metrics["json_valid"],
        "schema_valid": metrics.get("schema_valid", False),
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
        
        # Definir campos en el CSV
        fieldnames = [
            "test_id", "tarea", "model_id", "timestamp_utc",
            "latency_seconds", "prompt_tokens", "completion_tokens",
            "total_tokens", "success", "api_success", "json_valid", 
            "schema_valid", "error_message"
        ]
        
        with open(csv_filepath, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            if write_header:
                writer.writeheader()
            writer.writerow(metrics)
    except Exception as e:
        # Loggear con más detalle el error de escritura
        logger.error(f"Error guardando métricas en {csv_filepath} para {metrics.get('test_id', 'N/A')}: {e}", exc_info=True)

# --- Generación de reportes ---
def generar_reportes():
    """Genera reportes y visualizaciones de los resultados."""
    if not CONFIG["GENERAR_REPORTES"] or not pandas_disponible:
        return
    
    try:
        # Crear directorio de reportes
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        
        # Cargar datos
        if not METRICS_FILE.exists():
            logger.warning("No se puede generar reportes: archivo de métricas no encontrado.")
            return
        
        # Leer datos
        df = pd.read_csv(METRICS_FILE)
        
        # Generar reporte básico
        reporte_path = REPORTS_DIR / "reporte_rendimiento.md"
        
        with open(reporte_path, 'w', encoding='utf-8') as f:
            # Cabecera
            f.write(f"# Reporte de Rendimiento del Testeo de Prompts\n\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Resumen general
            total_articulos = len(df['test_id'].unique())
            total_tareas = len(df)
            tasa_exito = df['success'].mean() * 100
            
            f.write(f"## Resumen General\n\n")
            f.write(f"- **Artículos procesados:** {total_articulos}\n")
            f.write(f"- **Tareas totales:** {total_tareas}\n")
            f.write(f"- **Tasa de éxito general:** {tasa_exito:.2f}%\n\n")
            
            # Rendimiento por modelo
            f.write(f"## Rendimiento por Modelo\n\n")
            stats_modelo = df.groupby('model_id').agg({
                'success': ['mean', 'count'],
                'latency_seconds': ['mean', 'min', 'max'],
                'total_tokens': 'mean'
            })
            
            if tabulate_disponible:
                from tabulate import tabulate
                f.write(tabulate(stats_modelo, headers='keys', tablefmt='pipe'))
            else:
                f.write(f"```\n{stats_modelo}\n```\n\n")
            
            # Rendimiento por tarea
            f.write(f"\n## Rendimiento por Tarea\n\n")
            stats_tarea = df.groupby('tarea').agg({
                'success': ['mean', 'count'],
                'latency_seconds': 'mean'
            })
            
            if tabulate_disponible:
                f.write(tabulate(stats_tarea, headers='keys', tablefmt='pipe'))
            else:
                f.write(f"```\n{stats_tarea}\n```\n\n")
            
            # Errores comunes
            f.write(f"\n## Tipos de Errores Comunes\n\n")
            errores = df[df['success'] == False]['error_message'].value_counts().head(10)
            
            if tabulate_disponible:
                errores_df = pd.DataFrame({'Error': errores.index, 'Frecuencia': errores.values})
                f.write(tabulate(errores_df, headers='keys', tablefmt='pipe'))
            else:
                f.write(f"```\n{errores}\n```\n\n")
        
        logger.info(f"Reporte generado en: {reporte_path}")
        
        # Generar gráficos si está habilitado
        if CONFIG["GENERAR_GRAFICOS"] and matplotlib_disponible:
            # Gráfico 1: Tasa de éxito por modelo
            plt.figure(figsize=(10, 6))
            success_by_model = df.groupby('model_id')['success'].mean() * 100
            success_by_model.plot(kind='bar', color='skyblue')
            plt.title('Tasa de Éxito por Modelo (%)')
            plt.ylabel('Tasa de Éxito (%)')
            plt.xlabel('Modelo')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.savefig(REPORTS_DIR / "tasa_exito_por_modelo.png")
            
            # Gráfico 2: Tiempo de latencia por tarea y modelo
            plt.figure(figsize=(12, 7))
            latency_pivot = df.pivot_table(
                values='latency_seconds', 
                index='tarea', 
                columns='model_id', 
                aggfunc='mean'
            )
            latency_pivot.plot(kind='bar')
            plt.title('Tiempo de Latencia Promedio por Tarea y Modelo')
            plt.ylabel('Latencia (segundos)')
            plt.xlabel('Tarea')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.legend(title='Modelo')
            plt.tight_layout()
            plt.savefig(REPORTS_DIR / "latencia_por_tarea_modelo.png")
            
            logger.info(f"Gráficos generados en: {REPORTS_DIR}")
    
    except Exception as e:
        logger.error(f"Error generando reportes: {e}", exc_info=True)

# --- Lógica Principal Asíncrona ---
async def procesar_articulo(client: AsyncGroq, article_path: Path, output_dir_base: Path, csv_filepath: Path, procesados: Set[str]):
    """Procesa un único artículo con todas las tareas usando el modelo apropiado."""
    test_id = article_path.stem
    logger.info(f"--- Procesando Artículo: {test_id} ---")

    # Cargar el artículo
    articulo = load_article(article_path)
    if not articulo:
        logger.warning(f"Omitiendo artículo {test_id} debido a error de carga.")
        # Registrar fallo de carga si se desea
        metrics = {
             "test_id": test_id, "tarea": "carga_articulo", "model_id": MODELO_ESTANDAR,
             "timestamp_utc": datetime.now(timezone.utc).isoformat(),
             "latency_seconds": 0, "prompt_tokens": None, "completion_tokens": None,
             "total_tokens": None, "success": False, "api_success": False, "json_valid": False,
             "error_message": f"Failed to load article from {article_path}"
         }
        guardar_metricas_csv(metrics, csv_filepath)
        return

    # Determinar qué modelo usar para este artículo
    modelo_seleccionado = seleccionar_modelo(articulo)
    logger.info(f"[{test_id}] Modelo seleccionado: {modelo_seleccionado}")

    # Crear lista de corutinas a ejecutar
    tasks_coroutines = []
    for idx, tarea in enumerate(TASKS):
        # Generar prompt optimizado para el modelo específico
        prompt = generar_prompt(tarea, articulo, modelo_seleccionado)
        if not prompt:
            logger.warning(f"[{test_id}][{tarea}] Prompt vacío, omitiendo tarea.")
            continue
        
        # Crear la corutina
        coro = llamar_groq_con_metricas(
            client=client,
            model_id=modelo_seleccionado,
            prompt=prompt,
            test_id=test_id,
            tarea=tarea
        )
        tasks_coroutines.append(coro)

    if not tasks_coroutines:
        logger.warning(f"[{test_id}] No hay tareas para procesar.")
        return

    # Ejecutar todas las llamadas a Groq para este artículo en paralelo
    logger.info(f"[{test_id}] Lanzando {len(tasks_coroutines)} llamadas a Groq para {modelo_seleccionado}...")
    results_or_exceptions = await asyncio.gather(
        *tasks_coroutines,
        return_exceptions=True # Capturar excepciones de reintentos fallidos aquí
    )

    # Procesar y guardar resultados
    for i, result_or_exception in enumerate(results_or_exceptions):
        # Identificar la tarea asociada a este resultado/excepción
        tarea_actual = TASKS[i] # Asumimos que el orden se mantiene si no se omitió ninguna tarea

        if isinstance(result_or_exception, Exception):
            # Esto ocurre si @retry falla todos los intentos y reraise=True
            logger.error(f"[{test_id}][{tarea_actual}][{modelo_seleccionado}] Excepción no manejada por reintentos: {result_or_exception}")
            # Registrar métricas de fallo total
            metrics = {
                "test_id": test_id, "tarea": tarea_actual, "model_id": modelo_seleccionado,
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "latency_seconds": None, "prompt_tokens": None, "completion_tokens": None,
                "total_tokens": None, "success": False, "api_success": False, "json_valid": False,
                "schema_valid": False,
                "error_message": f"Unhandled Exception: {type(result_or_exception).__name__}: {str(result_or_exception)}"
            }
            # Guardar indicativo de error y métricas
            guardar_resultado_llm(test_id, tarea_actual, modelo_seleccionado, None, metrics, output_dir_base)
            guardar_metricas_csv(metrics, csv_filepath)
        else:
            # La llamada (con reintentos) tuvo éxito o falló de forma controlada
            response_content, metrics = result_or_exception
            # Asegurarnos de usar la tarea correcta de las métricas
            tarea_actual = metrics['tarea']
            guardar_resultado_llm(test_id, tarea_actual, modelo_seleccionado, response_content, metrics, output_dir_base)
            guardar_metricas_csv(metrics, csv_filepath)

    # Añadir a la lista de procesados y actualizar checkpoint
    procesados.add(test_id)
    guardar_checkpoint(procesados)
    
    logger.info(f"--- Artículo {test_id} completado ---")
    
    return test_id

async def mostrar_progreso(procesando: Dict[str, Dict], total: int, inicio: float):
    """Muestra información sobre el progreso de la ejecución mientras se procesa."""
    if CONFIG["MODO_SILENCIOSO"]:
        return
    
    # Solo actualizar cada 5 segundos para no saturar la salida
    while True:
        await asyncio.sleep(5)
        
        num_procesados = len([estado for estado, info in procesando.items() if info["completado"]])
        num_en_proceso = len([estado for estado, info in procesando.items() if not info["completado"]])
        
        tiempo_transcurrido = time.time() - inicio
        horas, resto = divmod(tiempo_transcurrido, 3600)
        minutos, segundos = divmod(resto, 60)
        
        # Calcular velocidad (artículos/minuto)
        if minutos > 0:
            velocidad = num_procesados / (tiempo_transcurrido / 60)
        else:
            velocidad = 0
        
        # Calcular tiempo estimado restante
        if velocidad > 0 and total > num_procesados:
            tiempo_restante = (total - num_procesados) / velocidad
            horas_r, resto_r = divmod(tiempo_restante, 60)
            minutos_r, segundos_r = divmod(resto_r, 60)
            
            tiempo_est = f"ETA: {int(horas_r)}h {int(minutos_r)}m"
        else:
            tiempo_est = "ETA: ?"
        
        # Si hay artículos en proceso, mostrar sus nombres
        en_proceso = [id for id, info in procesando.items() if not info["completado"]]
        if en_proceso:
            estado_actual = f"Procesando: {', '.join(en_proceso[:3])}"
            if len(en_proceso) > 3:
                estado_actual += f" y {len(en_proceso)-3} más"
        else:
            estado_actual = "Esperando..."
        
        # Construir barra de progreso visual
        porcentaje = num_procesados / total * 100
        barra_len = 30
        barra_completa = "█" * int(barra_len * porcentaje / 100)
        barra_vacia = "░" * (barra_len - len(barra_completa))
        barra = f"{barra_completa}{barra_vacia}"
        
        # Mostrar progreso
        print(f"\r[{barra}] {porcentaje:.1f}% ({num_procesados}/{total}) | "
              f"Tiempo: {int(horas)}h {int(minutos)}m {int(segundos)}s | "
              f"Velocidad: {velocidad:.2f} art/min | {tiempo_est} | {estado_actual}", 
              end="", flush=True)

async def main():
    """Función principal del script de testeo de prompts."""
    global UMBRAL_TOKENS, procesados  # Para permitir actualizaciones globales
    start_time_script = time.time()
    logger.info(f"--- Iniciando Script de Testeo de Prompts Mejorado ---")
    logger.info(f"Modelos configurados: {MODELO_ESTANDAR} / {MODELO_CONTEXTO_AMPLIO}")
    logger.info(f"Umbral de tokens: {UMBRAL_TOKENS}")

    # Crear directorios necesarios
    OUTPUT_DIR_BASE.mkdir(parents=True, exist_ok=True)
    logger.info(f"Directorio de resultados: {OUTPUT_DIR_BASE.resolve()}")
    logger.info(f"Archivo de métricas: {METRICS_FILE.resolve()}")

    try:
        api_key = load_api_key()
        # Inicializar el cliente AsyncGroq
        # Aumentar timeout para prompts más largos/complejos
        client = AsyncGroq(api_key=api_key, timeout=CONFIG["TIEMPO_ESPERA_API"])
        logger.info("Cliente AsyncGroq inicializado.")
    except ValueError:
        return

    # Cargar checkpoint si existe y está habilitado
    procesados = cargar_checkpoint()

    # Optimizar umbral de tokens si hay datos previos
    umbral_optimizado = optimizar_umbral_tokens()
    if umbral_optimizado != UMBRAL_TOKENS:
        UMBRAL_TOKENS = umbral_optimizado
        logger.info(f"Umbral de tokens optimizado a: {UMBRAL_TOKENS}")

    try:
        test_files_gen = INPUT_DIR.glob("test_*.json")
        test_files = sorted(list(test_files_gen))
        if not test_files:
             raise FileNotFoundError(f"No se encontraron archivos test_*.json en {INPUT_DIR}")
        logger.info(f"Encontrados {len(test_files)} archivos de prueba en {INPUT_DIR.resolve()}")
        
        # Filtrar archivos ya procesados
        if PERMITIR_RECUPERACION:
            test_files = [f for f in test_files if f.stem not in procesados]
            logger.info(f"Archivos pendientes de procesar: {len(test_files)}")
    except FileNotFoundError as fnf_error:
         logger.error(f"Error: {fnf_error}")
         return
    except Exception as e:
        logger.error(f"Error inesperado listando archivos de prueba: {e}")
        return

    # Procesar artículos concurrentemente
    CONCURRENCY_LIMIT = CONFIG["CONCURRENCY_LIMIT"]
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    
    # Diccionario para seguimiento de estado
    estado_procesamiento = {}
    total_archivos = len(test_files)

    async def process_with_semaphore(article_path):
        article_id = article_path.stem
        estado_procesamiento[article_id] = {"completado": False, "inicio": time.time()}
        
        async with semaphore:
            try:
                await procesar_articulo(client, article_path, OUTPUT_DIR_BASE, METRICS_FILE, procesados)
                estado_procesamiento[article_id]["completado"] = True
                estado_procesamiento[article_id]["fin"] = time.time()
                return article_id
            except Exception as e:
                logger.error(f"Error procesando {article_id}: {e}", exc_info=True)
                estado_procesamiento[article_id]["error"] = str(e)
                estado_procesamiento[article_id]["completado"] = True
                estado_procesamiento[article_id]["fin"] = time.time()
                return None

    # Crear task de monitoreo
    monitor_task = asyncio.create_task(
        mostrar_progreso(estado_procesamiento, total_archivos, start_time_script)
    )
    
    # Crear tareas de procesamiento
    processing_tasks = [process_with_semaphore(fp) for fp in test_files]

    logger.info(f"Iniciando procesamiento de {len(test_files)} artículos con concurrencia {CONCURRENCY_LIMIT}...")
    
    # Procesar artículos
    if processing_tasks:
        resultados = await asyncio.gather(*processing_tasks)
        # Filtrar resultados None (errores)
        completados = [r for r in resultados if r]
        logger.info(f"Completados {len(completados)} de {len(processing_tasks)} artículos.")
    else:
        logger.info("No hay artículos para procesar.")

    # Detener el monitor
    monitor_task.cancel()
    try:
        await monitor_task
    except asyncio.CancelledError:
        pass
    
    # Generar reportes si está configurado
    if CONFIG["GENERAR_REPORTES"]:
        logger.info("Generando reportes...")
        generar_reportes()

    # Mostrar resumen final
    end_time_script = time.time()
    duracion_total = end_time_script - start_time_script
    horas, resto = divmod(duracion_total, 3600)
    minutos, segundos = divmod(resto, 60)
    
    logger.info("--- Testeo de Prompts Completado ---")
    logger.info(f"Resultados LLM guardados en: {OUTPUT_DIR_BASE.resolve()}")
    logger.info(f"Métricas guardadas en: {METRICS_FILE.resolve()}")
    if CONFIG["GENERAR_REPORTES"]:
        logger.info(f"Reportes generados en: {REPORTS_DIR.resolve()}")
    logger.info(f"Tiempo total de ejecución: {int(horas)}h {int(minutos)}m {int(segundos)}s")
    
    # Si estamos en modo consola, mostrar un resumen más completo
    if not CONFIG["MODO_SILENCIOSO"]:
        print("\n" + "="*80)
        print(f"RESUMEN DE LA EJECUCIÓN")
        print("="*80)
        print(f"Artículos procesados: {len(procesados)}")
        print(f"Tiempo total: {int(horas)}h {int(minutos)}m {int(segundos)}s")
        if len(procesados) > 0 and duracion_total > 0:
            print(f"Tiempo promedio por artículo: {duracion_total/len(procesados):.2f} segundos")
        print(f"Resultados guardados en: {OUTPUT_DIR_BASE.resolve()}")
        if CONFIG["GENERAR_REPORTES"]:
            print(f"Reportes disponibles en: {REPORTS_DIR.resolve()}")
        print("="*80)

# --- Punto de Entrada ---
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        sys.exit(1)
    except Exception as e:
        logger.critical(f"Error crítico: {e}", exc_info=True)
        print(f"\nERROR CRÍTICO: {e}")
        sys.exit(2)
