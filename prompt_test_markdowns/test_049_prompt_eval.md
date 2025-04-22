# Evaluación Artículo: test_049
**Modelo Probado:** `llama3-8b-8192`

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

<details open>
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

## Resultados de las Tareas (llama3-8b-8192)

### Tarea: relevancia

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "La disputa en el Centro Democrático y el gasto de Uribe en eventos y publicidad en redes sociales",
    "categorias_asignadas": [
        "Política Nacional"
    ],
    "explicacion_concisa": "El artículo analiza la carrera política de Miguel Uribe y su relación con el uribismo, destacando la importancia del dinero en la disputa electoral en Colombia."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "Miguel Uribe gastó $300 millones en eventos y pauta en redes",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-05",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "dia",
            "paises": [
                "CO"
            ],
            "ubicaciones_especificas": [
                "Medellín"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "Miguel Uribe",
                "Uribismo",
                "Centro Democrático"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El uribismo comienza a consolidar fuerza electoral",
            "tipo_hecho": "CONCEPTO",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": null,
            "paises": [
                "CO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "Uribismo",
                "Elecciones"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La disputa en las huestes del Centro Democrático sigue generando fricciones",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": null,
            "paises": [
                "CO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "Centro Democrático",
                "Fricciones"
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
            "alias": []
        },
        {
            "nombre": "Medellín",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "uribismo",
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


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "El pasado 5 de abril",
            "emisor_nombre": "Miguel Uribe",
            "contexto": "en su carrera por hacerse a la bendición del uribismo con miras a 2026",
            "fecha_cita": null
        }
    ]
}
```
</details>


### Tarea: extraccion_datos

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Número de votos obtenidos por el senador Miguel Uribe",
            "categoria": "electoral",
            "valor_numerico": null,
            "unidad": null,
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
