# Resumen Comparativo de Experimentos de Pipeline

## Resultados por Modelo

 < /dev/null |  Modelo | Tiempo Total (s) | Artículos Procesados Completos | Tiempo promedio por artículo (s) |
|--------|------------------|--------------------------------|----------------------------------|
| gemma2-9b-it | 24.40 | 3/5 | 4.88 |
| llama-3.1-8b-instant | 49.87 | 5/5 | 9.97 |
| llama-3.3-70b-versatile | 32.73 | 5/5 | 6.55 |
| llama3-70b-8192 | 25.51 | 5/5 | 5.10 |
| llama3-8b-8192 | 30.66 | 5/5 | 6.13 |
| qwen-qwq-32b | 101.88 | 2/5 | 50.94 |

## Observaciones por Modelo

### gemma2-9b-it
- Filtró 2 artículos en la fase inicial (test_069 y test_040)
- Procesó completamente 3 artículos (test_005, test_047, test_004)
- Tiempo de respuesta rápido (24.40 s en total)

### llama-3.1-8b-instant
- Procesó todos los artículos completamente (5/5)
- Tiempo medio (49.87 s en total)

### llama-3.3-70b-versatile
- Procesó todos los artículos completamente (5/5)
- Tiempo más rápido que el modelo de 8B (32.73 s en total)

### llama3-70b-8192
- Procesó todos los artículos completamente (5/5)
- El segundo más rápido (25.51 s en total)

### llama3-8b-8192
- Procesó todos los artículos completamente (5/5)
- Tiempo medio (30.66 s en total)

### qwen-qwq-32b
- El más lento por amplio margen (101.88 s en total)
- Filtró 1 artículo en la fase inicial (test_069)
- Tuvo errores en 2 artículos durante el paso 2 (test_047 y test_004)
- Solo procesó 2 artículos completamente (test_005 y test_040)

## Conclusiones

1. **Mejor rendimiento general**: llama3-70b-8192 - Procesó todos los artículos con el segundo tiempo más rápido
2. **Más rápido pero menos completo**: gemma2-9b-it - El más rápido pero filtró 2 artículos
3. **Peor rendimiento**: qwen-qwq-32b - El más lento y con errores en 3 de 5 artículos
4. **Balance velocidad/completitud**: llama-3.3-70b-versatile - Procesó todos los artículos con buen tiempo

## Recomendaciones:
- Para uso general, el modelo **llama3-70b-8192** ofrece el mejor balance entre velocidad y efectividad
- Si se prioriza velocidad, **gemma2-9b-it** puede ser una opción aunque no procese todos los artículos
- Evitar **qwen-qwq-32b** por su bajo rendimiento y alta tasa de errores

## Detalles de la Prueba
- Fecha: 24 de abril de 2025
- Conjunto de prueba: 5 artículos (test_005, test_069, test_040, test_047, test_004)
- Pipeline: 5 pasos (filtrado, elementos básicos, citas/datos, relaciones, JSON final)
- Parámetros: timeout=300s, max_wait_retry=180s, max_retries=7
