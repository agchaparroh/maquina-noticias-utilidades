# Informe de Errores en el Experimento Pipeline (72 artículos)

## Resumen Ejecutivo

Durante la ejecución del experimento `pipeline_72_articulos_v2` usando el modelo `llama-3.1-8b-instant`, se detectaron fallos en 5 de los 72 artículos procesados (aproximadamente un 7% de tasa de error). Este informe detalla los problemas específicos encontrados, analiza sus causas y propone mejoras para futuras ejecuciones.

## Artículos Afectados y Naturaleza de los Errores

### 1. Artículo `test_002`

- **Título**: "El Polo Democrático oficializa su unión al Pacto Histórico"
- **Paso donde falló**: `prompt_1_elementos_basicos` (Extracción de elementos básicos)
- **Naturaleza del error**: Error de validación JSON
- **Causa raíz**: El modelo generó una lista excesivamente larga y repetitiva de hechos (al menos 60 hechos), con contenido casi idéntico, lo que resultó en un JSON truncado e inválido.
- **Detalles**: El modelo aparentemente entró en un bucle repetitivo generando múltiples hechos con ligeras variaciones como:
  ```
  "El Polo Democrático busca consolidar un bloque político que permita avanzar en las transformaciones necesarias para Colombia"
  ```
  seguido de:
  ```
  "El Polo Democrático busca fortalecer un bloque de izquierda capaz de influir y desarrollar el programa del actual gobierno"
  ```
  Este patrón se repitió numerosas veces.

### 2. Artículo `test_055`

- **Título**: "El Gobierno condecorará a rescatistas que participaron en la tragedia de la discoteca Jet Set"
- **Paso donde falló**: `prompt_4_json_final` (Generación del JSON final)
- **Naturaleza del error**: Error de validación JSON
- **Causa raíz**: El modelo generó un JSON aparentemente válido y completo, pero la API detectó algún problema de validación.
- **Detalles**: La respuesta era estructuralmente correcta, incluyendo secciones completas para metadatos, hechos, entidades, citas, datos cuantitativos y relaciones. Sin embargo, la API rechazó la respuesta con el error "json_validate_failed". Una posible causa podría ser la presencia de relaciones entidad-entidad duplicadas en las que la entidad de origen y destino eran la misma.

### 3. Artículo `test_070`

- **Título**: "Filtran lista de candidatos postulados por UNT: los inhabilitados Capriles y Guanipa a la cabeza"
- **Paso donde falló**: `prompt_4_json_final` (Generación del JSON final)
- **Naturaleza del error**: Error de validación JSON
- **Causa raíz**: Similar al artículo test_055, la estructura JSON era completa pero fue rechazada por la API.
- **Detalles**: La respuesta incluía correctamente todos los componentes requeridos y parecía bien formada, pero fue rechazada. No hay una causa obvia visible en la respuesta truncada disponible.

### 4. Artículo `test_071`

- **Título**: "Elecciones 2025: Jhonny asegura que están a horas de develar la dupla por UCS"
- **Paso donde falló**: `prompt_2_citas_datos` (Extracción de citas y datos cuantitativos)
- **Naturaleza del error**: Error de validación JSON
- **Causa raíz**: El modelo generó un número excesivo de citas textuales repetitivas (al menos 76).
- **Detalles**: El modelo duplicó múltiples veces las mismas citas para diferentes hechos identificados previamente. Por ejemplo, la cita "La voz del pueblo es la que manda" aparece relacionada con múltiples hechos diferentes, causando una explosión en el tamaño del JSON y posiblemente problemas de validación.

### 5. Artículo `test_072`

- **Título**: "Partidos que quedaron fuera de las Elecciones Generales aún podrían participar en las Regionales y Municipales 2026"
- **Paso donde falló**: `prompt_2_citas_datos` (Extracción de citas y datos cuantitativos)
- **Naturaleza del error**: Error de validación JSON
- **Causa raíz**: Problema con las comillas en las citas textuales.
- **Detalles**: El modelo incluyó comillas adicionales alrededor de los textos de las citas, usando `""` en lugar de `"` para delimitar las cadenas de texto, lo que resultó en un JSON inválido:
  ```json
  "cita": ""El proceso para ellos no ha quedado trunco, sigue en su curso..."",
  ```

## Patrones y Tendencias Identificados

1. **Generación excesiva y repetitiva**: Dos de los fallos (test_002 y test_071) se debieron a que el modelo generó cantidades excesivas de elementos repetitivos.

2. **Problemas con formato de citas**: El error en test_072 muestra problemas con el manejo de comillas en las citas textuales.

3. **Fallos en la etapa final**: Dos artículos (test_055 y test_070) fallaron en la última etapa (`prompt_4_json_final`), posiblemente debido a la complejidad acumulada.

4. **Distribución de tipos de errores**:
   - 2 fallos en `prompt_1_elementos_basicos` y `prompt_2_citas_datos` (etapas tempranas)
   - 2 fallos en `prompt_4_json_final` (etapa final)

## Impacto en el Experimento

- **Tasa de éxito**: 67 de 72 artículos completados correctamente (93.1%)
- **Artículos completamente procesados**: 67
- **Artículos parcialmente procesados**: 3 (con algunos pasos completados satisfactoriamente)
- **Artículos con fallos tempranos**: 2 (con pocos o ningún paso completado)

## Recomendaciones para Mejoras

1. **Limitación de elementos generados**:
   - Modificar los prompts para establecer límites claros en la cantidad de hechos, citas o relaciones que se deben extraer.
   - Incluir instrucciones explícitas para evitar repeticiones y elementos redundantes.

2. **Manejo de comillas en citas**:
   - Especificar con mayor claridad el formato exacto para las citas textuales.
   - Incluir ejemplos adicionales que muestren el manejo correcto de comillas.

3. **Validación intermedia**:
   - Implementar un paso adicional de validación JSON antes de pasar al siguiente paso del pipeline.
   - Añadir instrucciones para simplificar o consolidar elementos si el resultado es demasiado extenso.

4. **Ajustes para etapas finales**:
   - Optimizar la instrucción `prompt_4_json_final` para reducir la complejidad del proceso de consolidación.
   - Considerar dividir el paso final en sub-pasos para reducir la carga cognitiva del modelo.

5. **Detección de duplicados**:
   - Añadir una instrucción específica para detectar y eliminar elementos duplicados o muy similares.

## Ejemplos Específicos para Mejoras

### Modificación para evitar repeticiones (prompt_1_elementos_basicos):

```
IMPORTANTE: Extrae un máximo de 10 hechos principales no redundantes. Si identificas más de 10, selecciona solo los más relevantes y diversos. Evita crear hechos que sean reformulaciones de otros ya identificados.
```

### Instrucción para el manejo de citas (prompt_2_citas_datos):

```
Al extraer citas textuales, asegúrate de copiarlas exactamente como aparecen en el texto, sin añadir comillas adicionales. Cada cita debe ser asignada a un solo hecho, incluso si parece relacionarse con varios. Extrae un máximo de 10 citas más relevantes.
```

### Mejora para la consolidación (prompt_4_json_final):

```
Antes de generar el JSON final, revisa que no existan relaciones redundantes o contradictorias. Para entidades relacionadas consigo mismas, omite estas relaciones. Limita el número de relaciones hecho-entidad y entidad-entidad a un máximo de 20 en total.
```

## Conclusión

Los errores identificados en este experimento revelan áreas de mejora específicas en los prompts y en la estructura del pipeline. La mayoría de los problemas están relacionados con la tendencia del modelo a generar contenido repetitivo o a manejar incorrectamente ciertos formatos. 

A pesar de estos errores, el índice de éxito del 93.1% demuestra que el enfoque pipeline con el modelo llama-3.1-8b-instant es viable y efectivo para la mayoría de los artículos. Las mejoras propuestas deberían aumentar aún más esta tasa de éxito en futuros experimentos.