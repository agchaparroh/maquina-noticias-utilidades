# Resultados de Experimentos con Prompts Corregidos

Este directorio contiene los resultados de las pruebas realizadas con las plantillas de prompts corregidas (con placeholders para contenido y resultados previos).

## Estructura de Archivos

- `RESUMEN_COMPARATIVO_PROMPTS_CORREGIDOS.md`: Análisis comparativo de los resultados de todos los modelos
- `llama3-8b-8192/`: Resultados detallados del modelo llama3-8b-8192
  - `informe_exp_fixed_llama3-8b-8192.md`: Informe completo con todos los detalles
  - `metricas_exp_fixed_llama3-8b-8192.csv`: Métricas en formato CSV
- `llama-3-3-70b-versatile/`: Resultados detallados del modelo llama-3.3-70b-versatile
  - `metricas_exp_fixed_llama-3-3-70b-versatile.csv`: Métricas en formato CSV

## Conclusiones Principales

1. **Mejora Sustancial**: La inclusión de placeholders en las plantillas ha mejorado drásticamente el rendimiento.
2. **Modelo más efectivo**: `llama-3.3-70b-versatile` logró completar 4 de 5 artículos.
3. **Eficiencia**: `llama3-8b-8192` completó 3 de 5 artículos con mayor velocidad.
4. **Errores restantes**: Principalmente en el último paso (generación de JSON final).

*Para más detalles, consulta el archivo `RESUMEN_COMPARATIVO_PROMPTS_CORREGIDOS.md`.*
