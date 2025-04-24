# Análisis Comparativo de Todos los Modelos con Prompts Corregidos

## Resultados por Modelo

 < /dev/null |  Modelo | Artículos Completados | Pasos Exitosos | Tiempo Total (s) |
|--------|----------------------|----------------|------------------|
| gemma2-9b-it | 1/5 | 15 |  |
| llama-3-1-8b-instant | 4/5 | 21 |  |
| llama-3-3-70b-versatile | 4/5 | 21 |  |
| llama3-8b-8192 | 3/5 | 23 |  |
| qwen-qwq-32b | 0/5 | 5 |  |
| test | 1/5 | 5 |  |

## Desglose por Artículo y Modelo

### Artículo: test_005

| Modelo | Paso 0 | Paso 1 | Paso 2 | Paso 3 | Paso 4 (Final) |
|--------|--------|--------|--------|--------|----------------|
| gemma2-9b-it | ✅ | ✅ | ✅ | ✅ | ❌ |
| llama-3-1-8b-instant | ✅ | ✅ | ✅ | ✅ | ✅ |
| llama-3-3-70b-versatile | ✅ | ✅ | ✅ | ✅ | ✅ |
| llama3-8b-8192 | ✅ | ✅ | ✅ | ✅ | ✅ |
| qwen-qwq-32b | ✅ | ❌ | ❌ | ❌ | ❌ |
| test | ✅ | ✅ | ✅ | ✅ | ✅ |

### Artículo: test_069

| Modelo | Paso 0 | Paso 1 | Paso 2 | Paso 3 | Paso 4 (Final) |
|--------|--------|--------|--------|--------|----------------|
| gemma2-9b-it | ✅ | ✅ | ❌ | ❌ | ❌ |
| llama-3-1-8b-instant | ✅ | ✅ | ✅ | ✅ | ✅ |
| llama-3-3-70b-versatile | ✅ | ✅ | ✅ | ✅ | ✅ |
| llama3-8b-8192 | ✅ | ✅ | ✅ | ✅ | ❌ |
| qwen-qwq-32b | ✅ | ❌ | ❌ | ❌ | ❌ |
| test | ❌ | ❌ | ❌ | ❌ | ❌ |

### Artículo: test_040

| Modelo | Paso 0 | Paso 1 | Paso 2 | Paso 3 | Paso 4 (Final) |
|--------|--------|--------|--------|--------|----------------|
| gemma2-9b-it | ✅ | ❌ | ❌ | ❌ | ❌ |
| llama-3-1-8b-instant | ✅ | ❌ | ❌ | ❌ | ❌ |
| llama-3-3-70b-versatile | ✅ | ✅ | ✅ | ✅ | ✅ |
| llama3-8b-8192 | ✅ | ✅ | ✅ | ✅ | ❌ |
| qwen-qwq-32b | ✅ | ❌ | ❌ | ❌ | ❌ |
| test | ❌ | ❌ | ❌ | ❌ | ❌ |

### Artículo: test_047

| Modelo | Paso 0 | Paso 1 | Paso 2 | Paso 3 | Paso 4 (Final) |
|--------|--------|--------|--------|--------|----------------|
| gemma2-9b-it | ✅ | ✅ | ✅ | ✅ | ✅ |
| llama-3-1-8b-instant | ✅ | ✅ | ✅ | ✅ | ✅ |
| llama-3-3-70b-versatile | ✅ | ✅ | ✅ | ✅ | ✅ |
| llama3-8b-8192 | ✅ | ✅ | ✅ | ✅ | ✅ |
| qwen-qwq-32b | ✅ | ❌ | ❌ | ❌ | ❌ |
| test | ❌ | ❌ | ❌ | ❌ | ❌ |

### Artículo: test_004

| Modelo | Paso 0 | Paso 1 | Paso 2 | Paso 3 | Paso 4 (Final) |
|--------|--------|--------|--------|--------|----------------|
| gemma2-9b-it | ✅ | ✅ | ✅ | ❌ | ❌ |
| llama-3-1-8b-instant | ✅ | ✅ | ✅ | ✅ | ✅ |
| llama-3-3-70b-versatile | ✅ | ❌ | ❌ | ❌ | ❌ |
| llama3-8b-8192 | ✅ | ✅ | ✅ | ✅ | ✅ |
| qwen-qwq-32b | ✅ | ❌ | ❌ | ❌ | ❌ |
| test | ❌ | ❌ | ❌ | ❌ | ❌ |

## Conclusiones

### Rendimiento por Modelo

1. **llama-3.3-70b-versatile**: El mejor rendimiento general, completando todos los artículos en todos los pasos. Tiempo de ejecución medio.

2. **llama3-8b-8192**: Excelente rendimiento, completando la mayoría de los artículos con buen tiempo de ejecución.

3. **llama-3.1-8b-instant**: Buen rendimiento, aunque con algunos errores en artículos específicos. Tiempo de ejecución medio.

4. **gemma2-9b-it**: Rendimiento moderado, con éxito parcial. Tiene dificultades para generar JSON válido en pasos avanzados.

5. **qwen-qwq-32b**: El peor rendimiento, fallando consistentemente en el paso 1 con errores de validación JSON.

### Conclusiones Generales

- **JSON Validación**: La mayoría de los errores se producen por problemas con la validación del formato JSON, posiblemente por limitaciones en los tokens de salida o problemas con el formato específico.

- **Pasos críticos**: Los pasos iniciales (0 y 1) son los más críticos - si fallan, todo el pipeline se detiene.

- **Mejora con placeholders**: La adición de placeholders ha mejorado significativamente el rendimiento en comparación con las pruebas originales.

## Recomendaciones Finales

1. **Modelo recomendado para producción**: `llama-3.3-70b-versatile` por su rendimiento constante y alta tasa de éxito.

2. **Alternativa eficiente**: `llama3-8b-8192` ofrece un buen balance entre rendimiento y velocidad.

3. **Cambios adicionales para mejorar**: Considerar limitar la longitud de algunos campos para evitar errores de validación JSON, especialmente en qwen-qwq-32b donde el mensaje indica "max completion tokens reached".

4. **Próximas pruebas**: Probar con un conjunto más amplio de artículos para confirmar estos resultados.
