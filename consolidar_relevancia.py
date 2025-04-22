import json
import csv
import logging
from pathlib import Path


# --- Configuración ---
TARGET_MODEL_ID = "llama3-8b-8192"
TARGET_TASK = "relevancia"
RESULTS_DIR = Path("./benchmark_results")
ORIGINAL_DATA_DIR = Path("../data/benchmark_test_set") # Donde están los test_XXX.json originales
OUTPUT_CSV_FILE = RESULTS_DIR / f"{TARGET_TASK}_consolidados_{TARGET_MODEL_ID.replace('/', '_')}.csv"
METRICS_CSV_FILE = RESULTS_DIR / "benchmark_metrics.csv" # Para verificar éxito
# --------------------


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def get_successful_tests(metrics_file: Path, model_id: str, task: str) -> set:
    """Lee el CSV de métricas y devuelve los test_id que tuvieron éxito."""
    successful_ids = set()
    try:
        with open(metrics_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convertir el string 'True'/'False' a booleano
                is_success = row.get('success', '').strip().lower() == 'true'
                if (row.get('model_id') == model_id and
                        row.get('tarea') == task and
                        is_success):
                    successful_ids.add(row['test_id'])
    except FileNotFoundError:
        logger.error(f"Archivo de métricas no encontrado: {metrics_file}")
    except Exception as e:
        logger.error(f"Error leyendo archivo de métricas: {e}")
    return successful_ids


def main():
    logger.info(f"Iniciando consolidación para Tarea='{TARGET_TASK}', Modelo='{TARGET_MODEL_ID}'")
    if not RESULTS_DIR.is_dir():
        logger.error(f"Directorio de resultados no encontrado: {RESULTS_DIR}")
        return
    if not ORIGINAL_DATA_DIR.is_dir():
         logger.error(f"Directorio de datos originales no encontrado: {ORIGINAL_DATA_DIR}")
         return


    successful_test_ids = get_successful_tests(METRICS_CSV_FILE, TARGET_MODEL_ID, TARGET_TASK)
    if not successful_test_ids:
        logger.warning(f"No se encontraron ejecuciones exitosas para {TARGET_MODEL_ID}/{TARGET_TASK} en {METRICS_CSV_FILE}. No se generará CSV.")
        return


    logger.info(f"Encontradas {len(successful_test_ids)} ejecuciones exitosas para procesar.")


    consolidated_data = []
    processed_count = 0


    # Iterar sobre los IDs de test exitosos ordenados
    for test_id in sorted(list(successful_test_ids)):
        # Construir rutas a los archivos necesarios
        model_filename_part = TARGET_MODEL_ID.replace('/', '_')
        result_filename = f"{model_filename_part}.json"
        result_filepath = RESULTS_DIR / test_id / TARGET_TASK / result_filename
        original_filepath = ORIGINAL_DATA_DIR / f"{test_id}.json"


        # Verificar existencia de archivos
        if not result_filepath.is_file():
            logger.warning(f"Archivo de resultado no encontrado para {test_id}/{TARGET_TASK}/{model_filename_part}, omitiendo.")
            continue
        if not original_filepath.is_file():
            logger.warning(f"Archivo original no encontrado para {test_id}, no se puede obtener URL. Omitiendo.")
            continue


        try:
            # Cargar URL del archivo original
            with open(original_filepath, 'r', encoding='utf-8') as f_orig:
                original_data = json.load(f_orig)
                url = original_data.get("url", "URL no encontrada")


            # Cargar resultado del LLM
            with open(result_filepath, 'r', encoding='utf-8') as f_res:
                result_data = json.load(f_res)
                # Extraer el contenido de la respuesta (string JSON anidado)
                llm_response_str = result_data.get("llm_response_content")


                # Verificar si la respuesta no es un error guardado
                if not llm_response_str or llm_response_str.startswith("Error:"):
                     logger.warning(f"Respuesta LLM vacía o con error para {test_id}/{TARGET_TASK}/{model_filename_part}, omitiendo.")
                     continue


                # Parsear el JSON de la respuesta del LLM
                # El prompt de relevancia devuelve un objeto directamente, no necesita ["resultados"]
                relevance_output = json.loads(llm_response_str)


                # Extraer los datos específicos para el CSV
                consolidated_data.append({
                    "test_id": test_id,
                    "url": url,
                    "puntuacion_relevancia": relevance_output.get("puntuacion_relevancia"),
                    "justificacion_relevancia": relevance_output.get("justificacion_relevancia"),
                    "resumen_breve": relevance_output.get("resumen_breve"),
                    "categorias_asignadas": ", ".join(relevance_output.get("categorias_asignadas", [])) # Unir lista para CSV
                })
                processed_count += 1


        except json.JSONDecodeError as e:
            logger.error(f"Error decodificando JSON en {result_filepath} o en la respuesta del LLM para {test_id}: {e}, omitiendo.")
        except Exception as e:
            logger.error(f"Error inesperado procesando {test_id}: {e}", exc_info=True)


    if not consolidated_data:
        logger.warning("No se pudieron extraer datos válidos para generar el CSV.")
        return


    # Escribir el archivo CSV final
    try:
        logger.info(f"Escribiendo {len(consolidated_data)} registros en {OUTPUT_CSV_FILE}...")
        with open(OUTPUT_CSV_FILE, 'w', newline='', encoding='utf-8') as f_csv:
            fieldnames = ["test_id", "url", "puntuacion_relevancia", "justificacion_relevancia", "resumen_breve", "categorias_asignadas"]
            writer = csv.DictWriter(f_csv, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(consolidated_data)
        logger.info(f"Archivo CSV consolidado '{OUTPUT_CSV_FILE.name}' creado con éxito.")
    except Exception as e:
        logger.error(f"Error escribiendo archivo CSV: {e}")


if __name__ == "__main__":
    main()