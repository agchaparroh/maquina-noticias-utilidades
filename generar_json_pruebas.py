import csv
import requests
import json
import os
from bs4 import BeautifulSoup
import trafilatura # Para extraer contenido principal
from datetime import datetime, timezone
from tqdm import tqdm # Barra de progreso
import logging

# Configuración --- ¡AJUSTA ESTOS SI ES NECESARIO! ---
CSV_FILE = 'benchmark_urls.csv' # Nombre de tu archivo CSV
OUTPUT_DIR = 'data/benchmark_test_set' # Carpeta donde se guardarán los JSON
URL_COLUMN_INDEX = 0 # Índice de la columna con URLs en tu CSV (0 es la primera)
HAS_HEADER = True # ¿Tu CSV tiene una fila de encabezado? (True o False)
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" # Para simular un navegador
# -----------------------------------------------------

# Configurar logging básico
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def extract_metadata(soup):
    """Intenta extraer metadatos comunes usando BeautifulSoup."""
    metadata = {
        'fecha_publicacion': None,
        'autor': None,
        'seccion': None,
        'etiquetas_fuente': [],
        'medio': None, # Placeholder
        'pais_publicacion': None, # Placeholder
        'tipo_medio': None, # Placeholder
        'es_opinion': False, # Placeholder
        'es_oficial': False, # Placeholder
        'storage_path': None, # Placeholder
        'spider_name': 'script_generador' # Placeholder
    }
    try:
        # Fecha (busca en varios lugares comunes)
        time_tag = soup.find('time')
        if time_tag and time_tag.get('datetime'):
            metadata['fecha_publicacion'] = time_tag['datetime']
        else:
            # Buscar metatags comunes (OpenGraph, article)
            og_date = soup.find('meta', property='og:article:published_time')
            article_date = soup.find('meta', property='article:published_time')
            if og_date and og_date.get('content'):
                 metadata['fecha_publicacion'] = og_date['content']
            elif article_date and article_date.get('content'):
                 metadata['fecha_publicacion'] = article_date['content']
            # Añadir más búsquedas específicas si conoces patrones

        # Autor (busca metatags comunes)
        author_meta = soup.find('meta', {'name': 'author'})
        og_author = soup.find('meta', property='og:article:author') # Menos común
        article_author = soup.find('meta', property='article:author')
        if author_meta and author_meta.get('content'):
            metadata['autor'] = author_meta['content'].strip()
        elif article_author and article_author.get('content'):
             metadata['autor'] = article_author['content'].strip()
        elif og_author and og_author.get('content'):
             metadata['autor'] = og_author['content'].strip()

        # Sección (meta tag article:section)
        section_meta = soup.find('meta', property='article:section')
        if section_meta and section_meta.get('content'):
            metadata['seccion'] = section_meta['content'].strip()

        # Etiquetas (meta tag article:tag o keywords)
        tags = soup.find_all('meta', property='article:tag')
        if tags:
            metadata['etiquetas_fuente'] = [tag.get('content').strip() for tag in tags if tag.get('content')]
        else:
            keywords_meta = soup.find('meta', {'name': 'keywords'})
            if keywords_meta and keywords_meta.get('content'):
                metadata['etiquetas_fuente'] = [k.strip() for k in keywords_meta['content'].split(',')]

        # Medio (OpenGraph site_name)
        site_name_meta = soup.find('meta', property='og:site_name')
        if site_name_meta and site_name_meta.get('content'):
            metadata['medio'] = site_name_meta['content'].strip()

    except Exception as e:
        logging.warning(f"Error extrayendo metadatos básicos con BS4: {e}")

    # Intenta parsear la fecha si la encontró
    if isinstance(metadata['fecha_publicacion'], str):
         try:
             # Intenta parsear fecha ISO 8601. Añadir más formatos si es necesario
             parsed_date = datetime.fromisoformat(metadata['fecha_publicacion'].replace('Z', '+00:00'))
             # Asegurar que tenga zona horaria
             if parsed_date.tzinfo is None:
                 # Asumir UTC si no hay zona horaria - ¡PRECAUCIÓN! Esto puede ser incorrecto
                 # Sería mejor encontrar fechas con zona horaria o añadir lógica específica por sitio
                 parsed_date = parsed_date.replace(tzinfo=timezone.utc)
             metadata['fecha_publicacion'] = parsed_date.isoformat()
         except ValueError:
             logging.warning(f"No se pudo parsear la fecha encontrada: {metadata['fecha_publicacion']}")
             metadata['fecha_publicacion'] = None # O dejar como string si falló el parseo
    # Si no encontró fecha, usar fecha actual como fallback MUY BÁSICO
    if not metadata['fecha_publicacion']:
         metadata['fecha_publicacion'] = datetime.now(timezone.utc).isoformat()


    return metadata

def get_article_data(url):
    """Descarga y extrae datos de un artículo."""
    headers = {'User-Agent': USER_AGENT}
    downloaded = None
    soup = None
    try:
        # 1. Descargar con requests para BeautifulSoup (para metadatos)
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status() # Lanza error si no es 2xx
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')

        # 2. Descargar con Trafilatura (optimizado para contenido)
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            logging.warning(f"Trafilatura no pudo descargar: {url}")
            return None

        # 3. Extraer contenido principal con Trafilatura
        main_text = trafilatura.extract(
            downloaded,
            output_format='txt',
            include_comments=False,
            include_tables=False,
            no_fallback=True # Para que no devuelva toda la página si falla
        )
        if not main_text:
            logging.warning(f"Trafilatura no pudo extraer texto principal: {url}")
            # Intentar fallback muy básico con BeautifulSoup (puede ser ruidoso)
            body_tag = soup.find('body')
            if body_tag:
               main_text = body_tag.get_text(separator='\n\n', strip=True)
            else:
               return None # Realmente no hay contenido

        # 4. Extraer título y otros metadatos con Trafilatura o BS4
        title = trafilatura.extract_metadata(downloaded, default="").title
        if not title and soup: # Fallback con BS4
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text().strip()
        if not title: # Fallback final
             title = "Título no encontrado"


        # 5. Extraer metadatos adicionales con BeautifulSoup
        metadata_bs4 = extract_metadata(soup)

        # 6. Construir el diccionario ArticuloIn
        articulo_data = {
            "url": url,
            "storage_path": metadata_bs4.get('storage_path'), # Placeholder
            "medio": metadata_bs4.get('medio', "Medio Desconocido"), # Usa lo que encontró BS4 o default
            "pais_publicacion": metadata_bs4.get('pais_publicacion'), # Placeholder
            "tipo_medio": metadata_bs4.get('tipo_medio'), # Placeholder
            "titular": title,
            "fecha_publicacion": metadata_bs4.get('fecha_publicacion'), # Usa lo que encontró BS4
            "autor": metadata_bs4.get('autor'), # Usa lo que encontró BS4
            "contenido_texto": main_text,
            "idioma": "es", # Asumimos español por ahora
            "seccion": metadata_bs4.get('seccion'), # Usa lo que encontró BS4
            "etiquetas_fuente": metadata_bs4.get('etiquetas_fuente', []), # Usa lo que encontró BS4
            "es_opinion": metadata_bs4.get('es_opinion'), # Placeholder
            "es_oficial": metadata_bs4.get('es_oficial'), # Placeholder
            "timestamp_recopilacion": datetime.now(timezone.utc).isoformat(),
            "spider_name": metadata_bs4.get('spider_name') # Placeholder
        }
        return articulo_data

    except requests.exceptions.RequestException as e:
        logging.error(f"Error de red descargando {url}: {e}")
        return None
    except Exception as e:
        logging.error(f"Error procesando {url}: {e}")
        return None

# --- Lógica Principal ---
if __name__ == "__main__":
    # Crear directorio de salida si no existe
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    logging.info(f"Directorio de salida: {os.path.abspath(OUTPUT_DIR)}")

    urls_a_procesar = []
    try:
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            if HAS_HEADER:
                next(reader) # Saltar encabezado
            urls_a_procesar = [row[URL_COLUMN_INDEX].strip() for row in reader if row and row[URL_COLUMN_INDEX].strip().startswith('http')]
            logging.info(f"Encontradas {len(urls_a_procesar)} URLs válidas en {CSV_FILE}")
    except FileNotFoundError:
        logging.error(f"Error: No se encontró el archivo CSV: {CSV_FILE}")
        exit()
    except Exception as e:
         logging.error(f"Error leyendo el archivo CSV: {e}")
         exit()

    if not urls_a_procesar:
        logging.warning("No hay URLs para procesar. Saliendo.")
        exit()

    contador_exito = 0
    # Usar tqdm para mostrar barra de progreso
    for i, url in enumerate(tqdm(urls_a_procesar, desc="Procesando URLs")):
        logging.info(f"Procesando URL {i+1}/{len(urls_a_procesar)}: {url}")
        data = get_article_data(url)

        if data:
            # Generar nombre de archivo tipo test_001.json, test_002.json, etc.
            output_filename = f"test_{contador_exito + 1:03d}.json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    # Guardar con indentación para que sea legible y sin escapar caracteres no ASCII
                    json.dump(data, f, indent=4, ensure_ascii=False)
                logging.info(f"Guardado: {output_filename}")
                contador_exito += 1
            except Exception as e:
                logging.error(f"Error guardando JSON para {url}: {e}")
        else:
            logging.warning(f"No se pudieron extraer datos para: {url}")

    logging.info(f"\n--- Proceso Completado ---")
    logging.info(f"URLs procesadas: {len(urls_a_procesar)}")
    logging.info(f"Archivos JSON creados: {contador_exito} en '{OUTPUT_DIR}'")
    logging.info(f"Errores/Omitidos: {len(urls_a_procesar) - contador_exito}")