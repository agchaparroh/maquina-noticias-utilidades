# Evaluación Artículo: test_044

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.eluniversal.com.co/colombia/2025/04/14/consejo-de-ministros-razones-por-las-que-no-se-transmitira-hoy/           |
| **Título**     | Consejo de Ministros: razones por las que no se transmitirá hoy       |
| **Medio**      | www.eluniversal.com.co         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-21T00:43:28.141514+00:00 |
| **Recopilado** | 2025-04-21T00:43:28.141537+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Como cada lunes, esta noche se llevará a cabo una nueva sesión del Consejo de Ministros liderado por el presidente Gustavo Petro. Sin embargo, este no se transmitirá en ningún canal televisivo o plataforma.
Según informó El Colombiano, la razón es porque se hablaría de temas que tienen reserva legal, que incluye asuntos de seguridad nacional y que además es una decisión que se estaba pensando desde antes de que el Consejo de Estado ordenara el viernes pasado no emitir ese espacio a través de los canales privados.
“La semana pasada, de hecho, el propio presidente Gustavo Petro anunció y pidió que el siguiente Consejo de Ministros, es decir, el de este lunes, estuviera dedicado a la seguridad. Esto a raíz de que los homicidios tuvieron un leve incremento en el primer trimestre de este año y que en varias zonas del país persiste la crisis de orden público. Luego se planeó que el tema sería transporte, pero no se concretó”, señaló el medio en mención. Le puede interesar: Petro insiste en reformar justicia tras fallo que limita consejos de ministros
Niegan transmitir Consejo de Ministros por televisión
El pasado viernes 11 de abril, el Consejo de Estado ordenó al presidente Gustavo Petro dejar de transmitir los Consejos de Ministros, independientemente del horario, en los canales privados, locales y regionales, al considerar que se vulnera la pluralidad informativa, por ende solo se podrán transmitir en los canales públicos como Señal Colombia y el Canal Institucional.
El Consejo de Estado tomó la decisión luego de que una mujer que interpuso una tutela alegando que le fue vulnerado el derecho fundamental a la información porque, en dos ocasiones, no tuvo acceso a la programación ordinaria de los canales privados de televisión y, en su lugar, se había transmitido un Consejo de Ministros. Le invito a leer: Consejos de ministros no volverán a ser televisados: esta es la razón
Para la corporación, esto está probado toda vez que “el derecho a la información es igualmente vulnerado, cuando la información difundida es única, sin la posibilidad de tener acceso, en paralelo y en las mismas condiciones, a otras fuentes de información, a otros enfoques o interpretaciones de la realidad y la única opción informativa es la información oficial del gobierno, difundida en todos los canales televisivos de acceso abierto”.
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 0.50s | 1368.0 | 0.11 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 1.14s | 2652.0 | 0.23 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 0.68s | 1713.0 | 0.14 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 1.11s | 1639.0 | 0.16 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 1.21s | 2054.0 | 0.06 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.50s
- **Tokens prompt:** 1238.0
- **Tokens respuesta:** 130.0
- **Total tokens:** 1368.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 7,
    "justificacion_relevancia": "Revela decisiones del Consejo de Estado y posible impacto en la transparencia gubernamental",
    "categorias_asignadas": [
        "Política Nacional",
        "Justicia/Legal"
    ],
    "explicacion_concisa": "El artículo informa sobre la decisión del Consejo de Estado de no transmitir los Consejos de Ministros en canales privados, y la razón detrás de esta decisión, que involucra la seguridad nacional y la protección de la pluralidad informativa."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.14s
- **Tokens prompt:** 2162.0
- **Tokens respuesta:** 490.0
- **Total tokens:** 2652.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "El Consejo de Ministros no se transmitirá en ningún canal televisivo o plataforma.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-21T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "gobierno",
                "Consejo de Ministros"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El presidente Gustavo Petro anunció que el próximo Consejo de Ministros se centraría en la seguridad.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-15T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "gobierno",
                "seguridad"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El Consejo de Estado ordenó al presidente Gustavo Petro dejar de transmitir los Consejos de Ministros en los canales privados.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-11T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "gobierno",
                "Consejo de Estado"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        }
    ]
}
```
</details>


### Tarea: extraccion_entidades

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.68s
- **Tokens prompt:** 1503.0
- **Tokens respuesta:** 210.0
- **Total tokens:** 1713.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Gustavo Petro",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Consejo de Ministros",
            "tipo": "EVENTO",
            "alias": []
        },
        {
            "nombre": "Consejo de Estado",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Señal Colombia",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Canal Institucional",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "El Colombiano",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Consejos de ministros",
            "tipo": "EVENTO",
            "alias": []
        }
    ]
}
```
</details>


### Tarea: extraccion_citas

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.11s
- **Tokens prompt:** 1415.0
- **Tokens respuesta:** 224.0
- **Total tokens:** 1639.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "La semana pasada, de hecho, el propio presidente Gustavo Petro anunció y pidió que el siguiente Consejo de Ministros, es decir, el de este lunes, estuviera dedicado a la seguridad.",
            "emisor_nombre": "El Colombiano",
            "contexto": "Señaló el medio en mención",
            "fecha_cita": null
        },
        {
            "cita": "el derecho a la información es igualmente vulnerado, cuando la información difundida es única, sin la posibilidad de tener acceso, en paralelo y en las mismas condiciones, a otras fuentes de información, a otros enfoques o interpretaciones de la realidad y la única opción informativa es la información oficial del gobierno, difundida en todos los canales televisivos de acceso abierto",
            "emisor_nombre": "Consejo de Estado",
            "contexto": null,
            "fecha_cita": null
        }
    ]
}
```
</details>


### Tarea: extraccion_datos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.21s
- **Tokens prompt:** 1934.0
- **Tokens respuesta:** 120.0
- **Total tokens:** 2054.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Número de ocasiones en las que se ha transmitido un Consejo de Ministros",
            "categoria": "electoral",
            "valor_numerico": 2,
            "unidad": "ocasiones",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        }
    ]
}
```
</details>
