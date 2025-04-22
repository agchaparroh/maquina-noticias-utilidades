# Resultados de Benchmark LLM - Abril 2025

Este directorio contiene los resultados de las pruebas de benchmark realizadas el 22 de abril de 2025 utilizando el modelo Llama 3.1 8B (llama3-8b-8192) a través de la API de Groq.

## Contenidos

- **prompt_test_markdowns/**: Contiene 72 informes en formato Markdown con la evaluación detallada de cada artículo procesado. Cada informe incluye metadatos del artículo, contenido original y resultados de las tareas de extracción.

- **prompt_test_metrics.csv**: Archivo CSV con métricas detalladas de cada tarea de extracción, incluyendo:
  - Tiempo de respuesta
  - Número de tokens utilizados
  - Tasas de éxito
  - Validación de JSON y de esquema

## Resumen de Resultados

- **Artículos procesados**: 72
- **Tareas por artículo**: 5 (relevancia, extracción de hechos, entidades, citas y datos)
- **Tasa de éxito total**: 89.17% (321 de 360 tareas completadas sin errores)
- **Tiempo promedio por artículo**: 0.22 segundos

## Tareas de Extracción

1. **Relevancia**: Evaluación de la relevancia del artículo según criterios preestablecidos
2. **Extracción de hechos**: Identificación de afirmaciones factuales clave
3. **Extracción de entidades**: Reconocimiento de personas, organizaciones, lugares y otros elementos nombrados
4. **Extracción de citas**: Identificación de declaraciones textuales y sus emisores
5. **Extracción de datos**: Recopilación de valores numéricos y métricas relevantes

## Errores Comunes

- Fallos en la validación de esquema para campos numéricos (valor_numerico = None)
- Entidades clasificadas con tipos no incluidos en el esquema
- Errores ocasionales de formato JSON en respuestas complejas

---

_Benchmark ejecutado utilizando enhanced_script.py y updated_consolidation_script.py_