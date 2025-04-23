# Resultados de Prueba 1 - Evaluación de Prompts

Este directorio contiene los resultados consolidados de las pruebas de evaluación de prompts utilizando modelos LLM para análisis de artículos de noticias.

## Estructura de Directorios

- `prompt_test_results/`: Contiene los resultados brutos (archivos JSON) de las ejecuciones de las pruebas
  - Incluye el archivo de métricas `prompt_test_metrics.csv` con datos de rendimiento
  - Subdirectorios `test_XXX/` con resultados por artículo y tarea

- `prompt_test_markdowns/`: Contiene los archivos Markdown consolidados
  - Documentos `test_XXX_prompt_eval.md` con resultados formateados para fácil revisión

## Tareas Evaluadas

- Relevancia: Evaluación de relevancia del artículo
- Extracción de hechos: Identificación de hechos noticiosos principales
- Extracción de entidades: Identificación de personas, organizaciones y lugares
- Extracción de citas: Identificación de declaraciones textuales
- Extracción de datos: Identificación de datos y estadísticas

## Métricas Recopiladas

- Tasa de éxito por tarea
- Tiempo de procesamiento
- Consumo de tokens
- Validez del formato de respuesta

Fecha de generación: Abril 2025