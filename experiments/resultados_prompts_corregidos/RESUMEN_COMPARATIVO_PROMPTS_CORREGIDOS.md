# Análisis de Experimentos con Prompts Corregidos

## Resultados por Modelo

 < /dev/null |  Modelo | Artículos Procesados | Pasos Completados | Tasa de Éxito |
|--------|---------------------|-------------------|---------------|
| llama-3.3-70b-versatile | 4/5 | 21 | 100.0% |
| llama3-8b-8192 | 3/5 | 23 | 90.0% |
| test | 1/5 | 5 | 100.0% |

## Desglose por Artículo (llama3-8b-8192)

| Artículo | Paso 0 | Paso 1 | Paso 2 | Paso 3 | Paso 4 (Final) | Tiempo Total (s) |
|----------|--------|--------|--------|--------|----------------|------------------|
| test_005 | ✅ | ✅ | ✅ | ✅ | ✅ | 8.73 |
| test_069 | ✅ | ✅ | ✅ | ✅ | ❌ | 6.10 |
| test_040 | ✅ | ✅ | ✅ | ✅ | ❌ | 6.31 |
| test_047 | ✅ | ✅ | ✅ | ✅ | ✅ | 6.10 |
| test_004 | ✅ | ✅ | ✅ | ✅ | ✅ | 9.76 |

## Conclusiones

- **Mejora Sustancial**: La inclusión de placeholders en las plantillas de prompts ha permitido que los modelos reciban correctamente el contenido del artículo y los resultados de pasos anteriores, mejorando drásticamente el rendimiento.

- **Modelo más efectivo**: `llama-3.3-70b-versatile` logró completar el pipeline para 4 de 5 artículos, aunque requiere más tiempo por su mayor tamaño.

- **Eficiencia**: El modelo `llama3-8b-8192` completó 3 de 5 artículos con una velocidad mayor, representando un buen balance entre rendimiento y tiempo.

- **Errores restantes**: Los errores que aún persisten principalmente ocurren en el último paso (generación de JSON final), y están relacionados con la validación del formato JSON.

## Recomendaciones

1. **Para uso prioritario**: Usar `llama-3.3-70b-versatile` cuando la precisión es la máxima prioridad.

2. **Para uso equilibrado**: Usar `llama3-8b-8192` cuando se requiere un balance entre velocidad y precisión.

3. **Optimización continua**: Seguir refinando el prompt del paso 4 (JSON final) para aumentar la tasa de éxito.

4. **Pruebas adicionales**: Ampliar el conjunto de prueba para verificar el rendimiento con artículos más diversos.
