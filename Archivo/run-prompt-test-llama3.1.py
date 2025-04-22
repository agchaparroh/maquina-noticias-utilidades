#!/usr/bin/env python3
"""
Script para modificar run_prompt_test.py para usar Llama 3.1 8B con contexto ampliado
y corregir problemas de formato JSON, especialmente con comillas en citas.

Realiza los cambios mínimos necesarios para una evaluación comparativa efectiva.
"""
import re
import os
import sys
import shutil
from pathlib import Path

# Colores para terminal
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def main():
    """Función principal para procesar el archivo."""
    input_file = "run_prompt_test.py"
    output_file = "run_prompt_test_llama31.py"
    
    # Crear backup
    backup_file = "run_prompt_test_original.py"
    print(f"{YELLOW}Creando backup en {backup_file}...{RESET}")
    shutil.copy2(input_file, backup_file)
    
    # Leer el archivo original
    print(f"{YELLOW}Leyendo archivo {input_file}...{RESET}")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Aplicar las modificaciones
    print(f"{YELLOW}Aplicando modificaciones...{RESET}")
    content = change_model(content)
    content = fix_extraction_citas_prompt(content)
    content = fix_extraction_entidades_prompt(content)
    content = fix_clean_json_function(content)
    content = improve_retry_logic(content)
    
    # Escribir el archivo modificado
    print(f"{YELLOW}Escribiendo archivo modificado a {output_file}...{RESET}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"{GREEN}Modificaciones completadas con éxito. Archivo guardado como {output_file}{RESET}")
    return 0

def change_model(content):
    """Cambia el modelo a llama-3.1-8b-128k."""
    print(f"{YELLOW}Cambiando modelo a llama-3.1-8b-128k...{RESET}")
    # Modificar la definición del modelo
    content = re.sub(
        r'MODEL_TO_TEST = "llama3-8b-8192"',
        'MODEL_TO_TEST = "llama-3.1-8b-128k"  # Modelo con ventana de contexto de 128K tokens',
        content
    )
    return content

def fix_extraction_citas_prompt(content):
    """Mejora el prompt de extracción de citas para manejar correctamente las comillas."""
    print(f"{YELLOW}Mejorando prompt de extracción de citas...{RESET}")
    
    # Buscar el prompt de citas
    citas_prompt_pattern = r'elif tarea == "extraccion_citas":.*?return prompt\.strip\(\)'
    citas_match = re.search(citas_prompt_pattern, content, re.DOTALL)
    
    if not citas_match:
        print(f"{RED}No se pudo encontrar el prompt de extracción de citas{RESET}")
        return content
    
    # Nuevo prompt mejorado con instrucciones explícitas para comillas
    new_citas_prompt = '''elif tarea == "extraccion_citas":
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
        return prompt.strip()'''
    
    content = content.replace(citas_match.group(0), new_citas_prompt)
    return content

def fix_extraction_entidades_prompt(content):
    """Mejora el prompt de extracción de entidades para evitar problemas estructurales."""
    print(f"{YELLOW}Mejorando prompt de extracción de entidades...{RESET}")
    
    # Buscar el prompt de entidades
    entidades_prompt_pattern = r'elif tarea == "extraccion_entidades":.*?return prompt\.strip\(\)'
    entidades_match = re.search(entidades_prompt_pattern, content, re.DOTALL)
    
    if not entidades_match:
        print(f"{RED}No se pudo encontrar el prompt de extracción de entidades{RESET}")
        return content
    
    # Nuevo prompt con instrucciones mejoradas
    new_entidades_prompt = '''elif tarea == "extraccion_entidades":
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
        return prompt.strip()'''
    
    content = content.replace(entidades_match.group(0), new_entidades_prompt)
    return content

def fix_clean_json_function(content):
    """Mejora la función _clean_json_string para manejar mejor los problemas de JSON."""
    print(f"{YELLOW}Mejorando función de limpieza JSON...{RESET}")
    
    # Buscar la función _clean_json_string
    clean_json_pattern = r'def _clean_json_string\(raw_string: Optional\[str\]\) -> Optional\[str\]:.*?return None'
    clean_json_match = re.search(clean_json_pattern, content, re.DOTALL)
    
    if not clean_json_match:
        print(f"{RED}No se pudo encontrar la función _clean_json_string{RESET}")
        return content
    
    # Nueva función mejorada
    new_clean_json_function = '''def _clean_json_string(raw_string: Optional[str]) -> Optional[str]:
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
    fixed_string = re.sub(r",\s*(\}|\])", r"\\1", fixed_string)

    # 3. Intentar parsear el string reparado
    try:
        json.loads(fixed_string)
        logger.info("JSON reparado exitosamente.")
        return fixed_string
    except json.JSONDecodeError as e:
        logger.error(f"Falló la reparación del JSON: {e}. Devolviendo None.")
        return None'''
    
    content = content.replace(clean_json_match.group(0), new_clean_json_function)
    return content

def improve_retry_logic(content):
    """Mejora la lógica de reintentos para manejar mejor los rate limits."""
    print(f"{YELLOW}Mejorando lógica de reintentos...{RESET}")
    
    # Buscar la configuración de retry
    retry_pattern = r'@retry\(\s+stop=stop_after_attempt\(5\),\s+wait=wait_exponential\(multiplier=2, min=5, max=60\),\s+retry=retry_if_exception_type\(RETRYABLE_ERRORS\),\s+reraise=True # Re-lanza la excepción si todos los reintentos fallan\s+\)'
    
    # Nueva configuración
    new_retry = '''@retry(
    stop=stop_after_attempt(7),  # Aumentado a 7 reintentos
    wait=wait_exponential(multiplier=2, min=10, max=120),  # Esperas más largas
    retry=retry_if_exception_type(RETRYABLE_ERRORS),
    reraise=True # Re-lanza la excepción si todos los reintentos fallan
)'''
    
    content = re.sub(retry_pattern, new_retry, content)
    return content

if __name__ == "__main__":
    sys.exit(main())
