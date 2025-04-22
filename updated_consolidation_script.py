#!/usr/bin/env python3
"""
Script para consolidar resultados de evaluación de prompts en archivos Markdown.
Versión mejorada para trabajar con run_prompt_test_enhanced.py y mostrar métricas relevantes.
"""
import os
import json
import time
import logging
import csv
from pathlib import Path
from typing import Optional, Dict, Any, List

# --- Configuración ---
# Directorios (Ajustar según necesidad)
INPUT_ARTICLES_DIR = Path("../data/benchmark_test_set")
INPUT_RESULTS_DIR = Path("./prompt_test_results")
OUTPUT_MARKDOWN_DIR = Path("./prompt_test_markdowns")

# Archivo de métricas generado por run_prompt_test_enhanced.py
METRICS_FILE = INPUT_RESULTS_DIR / "prompt_test_metrics.csv"

# Tareas procesadas
TASKS = [
    "relevancia",
    "extraccion_hechos",
    "extraccion_entidades",
    "extraccion_citas",
    "extraccion_datos"
]

# Configuración de Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Funciones Auxiliares ---

def load_json_safe(filepath: Path) -> Optional[Dict[str, Any]]:
    """Carga un archivo JSON de forma segura, devolviendo None si falla."""
    if not filepath.is_file():
        logger.warning(f"Archivo no encontrado: {filepath}")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        logger.error(f"Error: Archivo JSON mal formado: {filepath.name}")
        return None
    except Exception as e:
        logger.error(f"Error cargando archivo {filepath.name}: {e}")
        return None

def load_metrics_csv(filepath: Path) -> Dict[str, Dict[str, Dict[str, Any]]]:
    """
    Carga las métricas del archivo CSV y las organiza por test_id y tarea.
    Retorna un diccionario con estructura {test_id: {tarea: {métricas}}}
    """
    metrics_by_id_task = {}
    
    if not filepath.exists():
        logger.warning(f"Archivo de métricas no encontrado: {filepath}")
        return metrics_by_id_task
    
    try:
        with open(filepath, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                test_id = row.get('test_id')
                tarea = row.get('tarea')
                
                # Convertir valores numéricos
                for key in ['latency_seconds', 'prompt_tokens', 'completion_tokens', 'total_tokens']:
                    if row.get(key) and row[key].replace('.', '', 1).isdigit():
                        row[key] = float(row[key])
                
                # Convertir valores booleanos
                for key in ['success', 'api_success', 'json_valid', 'schema_valid']:
                    if key in row:
                        row[key] = row[key].lower() == 'true'
                
                if test_id and tarea:
                    if test_id not in metrics_by_id_task:
                        metrics_by_id_task[test_id] = {}
                    metrics_by_id_task[test_id][tarea] = row
    
    except Exception as e:
        logger.error(f"Error leyendo archivo de métricas {filepath}: {e}")
    
    return metrics_by_id_task

def format_json_for_markdown(data: Any) -> str:
    """Formatea datos Python (parseados de JSON) como un bloque de código Markdown."""
    try:
        # Usar json.dumps para formatear con indentación
        formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
        return f"```json\n{formatted_json}\n```"
    except Exception as e:
        logger.error(f"Error formateando JSON para Markdown: {e}")
        # Devolver la representación string como fallback
        return f"```\n{str(data)}\n```"

def format_seconds(seconds: float) -> str:
    """Formatea segundos en un formato legible (min:seg)."""
    if seconds is None:
        return "N/A"
    
    minutes, secs = divmod(seconds, 60)
    return f"{int(minutes)}m {secs:.2f}s"

# --- Generación de Markdown (Con Mejoras) ---

def generate_markdown_content(
    test_id: str, 
    article_data: Dict[str, Any], 
    results_by_task: Dict[str, Dict[str, Any]],
    metrics_by_task: Dict[str, Dict[str, Any]]
) -> str:
    """Genera el contenido Markdown completo para un artículo con métricas."""
    markdown_content: List[str] = []

    # --- Cabecera y Metadatos ---
    markdown_content.append(f"# Evaluación Artículo: {test_id}")
    markdown_content.append("\n## Metadatos del Artículo Original")
    markdown_content.append("")
    # Usar tabla Markdown para metadatos
    markdown_content.append("| Campo          | Valor                                      |")
    markdown_content.append("|----------------|--------------------------------------------|")
    markdown_content.append(f"| **URL**        | {article_data.get('url', 'N/A')}           |")
    markdown_content.append(f"| **Título**     | {article_data.get('titular', 'N/A')}       |")
    markdown_content.append(f"| **Medio**      | {article_data.get('medio', 'N/A')}         |")
    markdown_content.append(f"| **País Pub.**  | {article_data.get('pais_publicacion', 'N/A')} |")
    markdown_content.append(f"| **Fecha Pub.** | {article_data.get('fecha_publicacion', 'N/A')} |")
    markdown_content.append(f"| **Recopilado** | {article_data.get('timestamp_recopilacion', 'N/A')} |")
    markdown_content.append("\n---\n")

    # --- Contenido del Artículo (Plegable) ---
    markdown_content.append("## Contenido del Artículo Analizado")
    markdown_content.append("")
    contenido_texto = article_data.get('contenido_texto', '*Contenido no disponible*')
    markdown_content.append("<details>") # Cerrado por defecto para ahorrar espacio
    markdown_content.append("<summary>Ver/Ocultar Contenido Completo</summary>\n")
    markdown_content.append(f"```text\n{contenido_texto}\n```")
    markdown_content.append("</details>")
    markdown_content.append("\n---\n")

    # --- Resumen de Evaluación ---
    markdown_content.append("## Resumen de Evaluación\n")
    
    markdown_content.append("| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |")
    markdown_content.append("|-------|--------|--------|--------|--------|-------|")
    
    for tarea in TASKS:
        result_data = results_by_task.get(tarea, {})
        metrics = metrics_by_task.get(tarea, {})
        
        # Estado
        estado = "✅" if result_data.get('success', False) else "❌"
        
        # Modelo usado
        modelo = result_data.get('model_id', metrics.get('model_id', 'N/A'))
        
        # Tiempo de ejecución
        tiempo = format_seconds(metrics.get('latency_seconds'))
        
        # Tokens
        total_tokens = metrics.get('total_tokens', 'N/A')
        
        # Ratio de tokens completados vs prompt (eficiencia)
        prompt_tokens = metrics.get('prompt_tokens', 0) or 0
        completion_tokens = metrics.get('completion_tokens', 0) or 0
        
        if prompt_tokens and completion_tokens:
            ratio = f"{completion_tokens / prompt_tokens:.2f}"
        else:
            ratio = "N/A"
        
        markdown_content.append(f"| {tarea} | {estado} | `{modelo}` | {tiempo} | {total_tokens} | {ratio} |")
    
    markdown_content.append("\n---\n")

    # --- Resultados detallados por Tarea ---
    markdown_content.append("## Resultados Detallados por Tarea")

    for tarea in TASKS:
        markdown_content.append(f"\n### Tarea: {tarea}\n")
        result_data = results_by_task.get(tarea) # Obtener resultado para la tarea
        metrics = metrics_by_task.get(tarea, {}) # Obtener métricas para la tarea

        if not result_data:
            markdown_content.append("⚠️ **Estado:** No se encontraron resultados para esta tarea.\n")
            continue

        # Mostrar estado con iconos
        if result_data.get('success'):
            markdown_content.append("✅ **Estado:** Éxito")
        else:
            if result_data.get('api_success') is False:
                 markdown_content.append("❌ **Estado:** Fallo (Error API)")
            elif result_data.get('json_valid') is False:
                 markdown_content.append("⚠️ **Estado:** Fallo (JSON Inválido/Estructura Incorrecta)")
            else:
                 # Otro tipo de fallo no especificado
                 markdown_content.append("❌ **Estado:** Fallo (Desconocido)")

        # Mostrar mensaje de error si existe
        if result_data.get('error_message'):
            markdown_content.append(f"\n   **Mensaje Error:** `{result_data['error_message']}`")
            
        # Mostrar métricas importantes
        markdown_content.append("\n**Métricas:**")
        markdown_content.append(f"- **Modelo:** `{result_data.get('model_id', metrics.get('model_id', 'N/A'))}`")
        markdown_content.append(f"- **Tiempo:** {format_seconds(metrics.get('latency_seconds'))}")
        markdown_content.append(f"- **Tokens prompt:** {metrics.get('prompt_tokens', 'N/A')}")
        markdown_content.append(f"- **Tokens respuesta:** {metrics.get('completion_tokens', 'N/A')}")
        markdown_content.append(f"- **Total tokens:** {metrics.get('total_tokens', 'N/A')}")

        markdown_content.append("\n") # Nueva línea después de las métricas

        # Mostrar la respuesta del LLM (Plegable)
        llm_response_str = result_data.get('llm_response_content')
        if llm_response_str:
             markdown_content.append("<details open>") # Abierto por defecto
             markdown_content.append("<summary>Ver/Ocultar Respuesta LLM</summary>\n")
             # Intentar parsear el contenido para formatearlo bien si era válido
             if result_data.get('json_valid'):
                 try:
                     parsed_llm_response = json.loads(llm_response_str)
                     markdown_content.append(format_json_for_markdown(parsed_llm_response))
                 except json.JSONDecodeError:
                     logger.warning(f"[{test_id}][{tarea}] Inconsistencia: json_valid=True pero falló parseo en consolidación.")
                     markdown_content.append(f"_(Error al parsear JSON para formateo, mostrando raw):_\n```\n{llm_response_str}\n```")
             else:
                 # Si el JSON no era válido, mostrar el string raw
                 markdown_content.append(f"_(Respuesta no es JSON válido o estructura incorrecta, mostrando raw):_\n```\n{llm_response_str}\n```")
             markdown_content.append("</details>\n") # Fin del details
        else:
             markdown_content.append("_No se recibió contenido del LLM._\n")

    return "\n".join(markdown_content)


# --- Lógica Principal ---

def main():
    """Función principal para consolidar resultados en Markdown."""
    start_time = time.time()
    logger.info("--- Iniciando Consolidación de Resultados para Evaluación ---")

    try:
        # Crear directorio de salida
        OUTPUT_MARKDOWN_DIR.mkdir(parents=True, exist_ok=True)
        logger.info(f"Directorio de salida Markdown: {OUTPUT_MARKDOWN_DIR.resolve()}")

        # Cargar métricas
        logger.info(f"Cargando métricas desde: {METRICS_FILE}")
        metrics_by_id_task = load_metrics_csv(METRICS_FILE)
        logger.info(f"Métricas cargadas para {len(metrics_by_id_task)} artículos")

        # Buscar archivos de artículos
        article_files = sorted(list(INPUT_ARTICLES_DIR.glob("test_*.json")))
        if not article_files:
            logger.error(f"No se encontraron archivos 'test_*.json' en {INPUT_ARTICLES_DIR.resolve()}")
            return 1 # Indicar error

        logger.info(f"Procesando {len(article_files)} artículos...")
        markdown_count = 0
        error_count = 0

        for article_path in article_files:
            test_id = article_path.stem
            logger.info(f"Procesando: {test_id}")

            # 1. Cargar artículo original
            article_data = load_json_safe(article_path)
            if not article_data:
                logger.warning(f"Omitiendo {test_id} debido a error al cargar artículo original.")
                error_count += 1
                continue

            # 2. Cargar resultados por tarea
            results_by_task: Dict[str, Dict[str, Any]] = {}
            for tarea in TASKS:
                result_file_path = INPUT_RESULTS_DIR / test_id / f"{tarea}.json"
                result_data = load_json_safe(result_file_path)
                if result_data:
                    results_by_task[tarea] = result_data

            # 3. Obtener métricas para este artículo
            metrics_by_task = metrics_by_id_task.get(test_id, {})

            # 4. Generar contenido Markdown
            markdown_text = generate_markdown_content(test_id, article_data, results_by_task, metrics_by_task)

            # 5. Escribir archivo Markdown
            output_md_path = OUTPUT_MARKDOWN_DIR / f"{test_id}_prompt_eval.md"
            try:
                with open(output_md_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_text)
                markdown_count += 1
            except Exception as e:
                logger.error(f"Error escribiendo archivo Markdown {output_md_path.name}: {e}")
                error_count += 1

        end_time = time.time()
        logger.info("--- Consolidación Completada ---")
        logger.info(f"Generados {markdown_count} archivos Markdown en: {OUTPUT_MARKDOWN_DIR.resolve()}")
        if error_count > 0:
            logger.warning(f"Se encontraron {error_count} errores durante el proceso.")
        logger.info(f"Tiempo total de ejecución: {end_time - start_time:.2f} segundos")
        return 0 # Éxito

    except KeyboardInterrupt:
        logger.info("Proceso interrumpido por el usuario.")
        return 1
    except Exception as e:
        logger.error(f"Error inesperado durante la consolidación: {e}", exc_info=True)
        return 1


# --- Punto de Entrada ---
if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) # Salir con el código de retorno apropiado
