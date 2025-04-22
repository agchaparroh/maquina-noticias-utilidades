#!/usr/bin/env python3
import re

def main():
    # Leer el archivo original
    with open('run_prompt_test.py', 'r') as f:
        content = f.read()
    
    # 1. Modificar CONCURRENCY_LIMIT (ya hecho)
    # content = re.sub(r'CONCURRENCY_LIMIT = 5 # Mantener concurrencia razonable', 
    #                 'CONCURRENCY_LIMIT = 2 # Bajar de 5 a 2', 
    #                 content)

    # 2. Modificar @retry (ya hecho)
    # content = re.sub(r'@retry\(\s+stop=stop_after_attempt\(3\),\s+wait=wait_exponential\(multiplier=1, min=2, max=10\),',
    #                 '@retry(\n    stop=stop_after_attempt(5),  # Aumentar de 3 a 5\n    wait=wait_exponential(multiplier=2, min=5, max=60),  # Esperas más largas (5s a 60s)',
    #                 content)

    # 3. Añadir ejemplo para prompt extraccion_hechos
    content = re.sub(r'Artículo a analizar:\s+Título: \{titulo\}\s+Fecha Pub: \{fecha_pub\}\s+País Pub: \{pais\}\s+Contenido:\s+\{contenido\}\s+\s+Respuesta \(objeto JSON con clave "resultados"\):',
                     r"""Artículo a analizar:
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

	Respuesta (objeto JSON con clave "resultados"):""",
                     content)

    # 4. Añadir ejemplo para prompt extraccion_entidades
    content = re.sub(r'Texto a analizar:\s+\{contenido\}\s+\s+Respuesta \(objeto JSON con clave "resultados"\):',
                     r"""Texto a analizar:
	{contenido}

EJEMPLO DE FORMATO ESPERADO:
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
    }},
    {{
      "nombre": "Elecciones Generales España 2023",
      "tipo": "EVENTO",
      "alias": ["elecciones generales", "comicios"]
    }}
  ]
}}

	Respuesta (objeto JSON con clave "resultados"):""",
                     content)
    
    # 5. Añadir ejemplo para prompt extraccion_citas
    content = re.sub(r'INSTRUCCIONES ADICIONALES IMPORTANTES:.*?Texto a analizar:\s+\{contenido\}\s+\s+Respuesta \(objeto JSON con clave "resultados"\):',
                     r"""INSTRUCCIONES ADICIONALES IMPORTANTES:
	- **Literalidad:** Extrae ÚNICAMENTE citas textuales directas.
	- **Atribución:** Identifica claramente al emisor en 'emisor_nombre'.
	- **Valores Nulos:** Usa `null` explícitamente para 'contexto' y 'fecha_cita' cuando no aplique o no se encuentre la información.
	- **JSON Final:** La respuesta COMPLETA debe ser un ÚNICO objeto JSON que contenga UNA sola clave llamada "resultados". El valor de "resultados" DEBE ser la lista JSON de los objetos de citas extraídos. Ejemplo: {{"resultados": [ {{cita1}}, {{cita2}}, ... ]}}. NO incluyas NINGÚN texto antes o después de este objeto JSON principal. Verifica la validez del JSON.
	
	Texto a analizar:
	{contenido}

EJEMPLO DE FORMATO ESPERADO:
{{
  "resultados": [
    {{
      "cita": "El gobierno tomará medidas contundentes.",
      "emisor_nombre": "Ministro de Economía",
      "contexto": "Durante la rueda de prensa semanal.",
      "fecha_cita": "2025-04-14"
    }},
    {{
      "cita": "Es fundamental mantener la calma.",
      "emisor_nombre": "Presidente de la República",
      "contexto": null,
      "fecha_cita": null
    }}
  ]
}}

	Respuesta (objeto JSON con clave "resultados"):""",
                     content, flags=re.DOTALL)

    # 6. Añadir ejemplo para prompt extraccion_datos
    content = re.sub(r'INSTRUCCIONES ADICIONALES IMPORTANTES:.*?Texto a analizar:\s+\{contenido\}\s+\s+Respuesta \(objeto JSON con clave "resultados"\):',
                     r"""INSTRUCCIONES ADICIONALES IMPORTANTES:
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

	Respuesta (objeto JSON con clave "resultados"):""",
                     content, flags=re.DOTALL)
    
    # Escribir el archivo modificado
    with open('run_prompt_test.py', 'w') as f:
        f.write(content)
    
    print("Modificaciones completadas con éxito.")

if __name__ == "__main__":
    main()