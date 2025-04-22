# Evaluación Artículo: test_049

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.elcolombiano.com/colombia/miguel-uribe-ha-gastado-300-millones-en-eventos-y-pauta-en-redes-MF27118455           |
| **Título**     | ¿Tensión en el uribismo? Revelan que Miguel Uribe ha gastado $300 millones en eventos y pauta en redes       |
| **Medio**      | El Colombiano         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-21T00:43:38.205728+00:00 |
| **Recopilado** | 2025-04-21T00:43:38.205752+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
El evento que lideró el pasado 5 de abril en Medellín corroboró la fuerza electoral que comienza a consolidar el senador Miguel Uribe en su carrera por hacerse a la bendición del uribismo con miras a 2026. Sin embargo, evidenció también que la disputa en las huestes del Centro Democrático sigue generando fricciones y que el factor dinero marca la diferencia.
Pico y Placa Medellín
viernes
0 y 6
0 y 6
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 3.93s | 975.0 | 0.12 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 4.10s | 2219.0 | 0.29 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 4.54s | 1236.0 | 0.18 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 0.78s | 1063.0 | 0.11 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 0.80s | 1599.0 | 0.08 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 3.93s
- **Tokens prompt:** 871.0
- **Tokens respuesta:** 104.0
- **Total tokens:** 975.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "La información sobre la financiación de eventos y pauta en redes de Uribe es relevante para la política colombiana.",
    "categorias_asignadas": [
        "Política Nacional"
    ],
    "explicacion_concisa": "El artículo analiza la carrera política de Miguel Uribe y su relación con el uribismo, destacando la importancia del dinero en su campaña electoral."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 4.10s
- **Tokens prompt:** 1722.0
- **Tokens respuesta:** 497.0
- **Total tokens:** 2219.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "El evento que lideró el pasado 5 de abril en Medellín corroboró la fuerza electoral que comienza a consolidar el senador Miguel Uribe en su carrera por hacerse a la bendición del uribismo con miras a 2026.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-05T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [],
            "ubicaciones_especificas": [
                "Medellín"
            ],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "elecciones",
                "uribismo"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La disputa en las huestes del Centro Democrático sigue generando fricciones y que el factor dinero marca la diferencia.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "n/a",
            "paises": [],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 4,
            "etiquetas": [
                "política",
                "partidos políticos",
                "disputa"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Miguel Uribe ha gastado $300 millones en eventos y pauta en redes.",
            "tipo_hecho": "BIOGRAFIA",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "n/a",
            "paises": [],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "finanzas",
                "Miguel Uribe"
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
- **Tiempo:** 0m 4.54s
- **Tokens prompt:** 1049.0
- **Tokens respuesta:** 187.0
- **Total tokens:** 1236.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Miguel Uribe",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Centro Democrático",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Pico y Placa Medellín",
            "tipo": "EVENTO",
            "alias": [
                "Pico y Placa Medellín"
            ]
        },
        {
            "nombre": "Medellín",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Uríbismo",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "2026",
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
- **Tiempo:** 0m 0.78s
- **Tokens prompt:** 961.0
- **Tokens respuesta:** 102.0
- **Total tokens:** 1063.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "El evento que lideró el pasado 5 de abril en Medellín corroboró la fuerza electoral que comienza a consolidar el senador Miguel Uribe en su carrera por hacerse a la bendición del uribismo con miras a 2026.",
            "emisor_nombre": "senador Miguel Uribe",
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
- **Tiempo:** 0m 0.80s
- **Tokens prompt:** 1480.0
- **Tokens respuesta:** 119.0
- **Total tokens:** 1599.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Número de votos obtenidos por el senador Miguel Uribe",
            "categoria": "electoral",
            "valor_numerico": 0,
            "unidad": "votos",
            "ambito_geografico": [
                "Medellín"
            ],
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
