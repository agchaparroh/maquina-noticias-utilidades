# Evaluación Artículo: test_045
**Modelo Probado:** `llama3-8b-8192`

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://eldeber.com.bo/pais/justicia-ordena-apremio-del-ministro-edgar-montano-por-deuda-extrabajadores-de-sabsa_510601/           |
| **Título**     | Justicia ordena apremio del ministro Edgar Montaño por deuda a extrabajadores de Sabsa       |
| **Medio**      | El Deber         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T22:01:30+00:00 |
| **Recopilado** | 2025-04-21T00:43:28.281494+00:00 |

---

## Contenido del Artículo Analizado

<details open>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Justicia ordena apremio del ministro Edgar Montaño por deuda a extrabajadores de Sabsa
La medida busca ejecutar el pago de más de Bs 55 millones en beneficios laborales a extrabajadores de la empresa aeroportuaria, quienes llevan 14 años de espera
El juez Marcelo Cortez Candia, del Juzgado Público Civil, Comercial, de Partido del Trabajo y Seguridad Social de Yapacaní, emitió un mandamiento de apremio contra el ministro de Obras Públicas, Edgar Montaño Rojas, en el marco de un proceso judicial iniciado por extrabajadores del Servicio de Aeropuertos Bolivianos S. A. (SABSA).
La disposición instruye a la Policía Boliviana aprehender a Montaño y trasladarlo a la carceleta de Buena Vista, hasta que se concrete el pago de Bs 55.189.880, por concepto diferencia salarial a los extrabajadores que lo demandaron.
La decisión judicial responde a una larga lucha legal por parte de 320 extrabajadores de Sabsa, quienes desde hace 14 años exigen el cumplimiento de sus derechos laborales tras el cierre de la empresa estatal.
La molestia del sector afectado se hizo visible el pasado 10 de enero, cuando realizaron una masiva protesta frente al Ministerio de Obras Públicas. En esa ocasión, denunciaron que, pese a las promesas públicas del ministro Montaño, el desembolso nunca se concretó.
“Nos dijo públicamente que, en 15 días, con la sentencia de la justicia, se realizaría el pago, e incluso se comprometió a colaborar para agilizar el juicio. Sin embargo, todas las instancias han fallado a nuestro favor y ellos siguen apelando”, lamentó uno de los afectados.
El mandamiento de apremio busca precisamente presionar al ministro para ejecutar la sentencia, que ordena que se paguen la diferencial salarial a los extrabajadores de Sabsa.
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
    "puntuacion_relevancia": 8,
    "justificacion_relevancia": "Relevancia media debido a la importancia del tema laboral y la figura del ministro involucrado",
    "categorias_asignadas": [
        "Justicia/Legal",
        "Política Nacional"
    ],
    "explicacion_concisa": "La justicia ordena apremio al ministro Edgar Montaño para ejecutar el pago de más de 55 millones de bolivianos a extrabajadores de Sabsa, que llevan 14 años de espera"
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
            "contenido": "Justicia ordena apremio del ministro Edgar Montaño por deuda a extrabajadores de Sabsa",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Yapacaní"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "justicia",
                "trabajo",
                "deuda"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La medida busca ejecutar el pago de más de Bs 55 millones en beneficios laborales a extrabajadores de la empresa aeroportuaria, quienes llevan 14 años de espera",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Yapacaní"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "trabajo",
                "deuda",
                "pago"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El juez Marcelo Cortez Candia, del Juzgado Público Civil, Comercial, de Partido del Trabajo y Seguridad Social de Yapacaní, emitió un mandamiento de apremio contra el ministro de Obras Públicas, Edgar Montaño Rojas, en el marco de un proceso judicial iniciado por extrabajadores del Servicio de Aeropuertos Bolivianos S. A. (SABSA)",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Yapacaní"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "justicia",
                "trabajo",
                "ministro"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La disposición instruye a la Policía Boliviana aprehender a Montaño y trasladarlo a la carceleta de Buena Vista, hasta que se concrete el pago de Bs 55.189.880, por concepto diferencia salarial a los extrabajadores que lo demandaron",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Yapacaní"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "justicia",
                "trabajo",
                "pago"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La decisión judicial responde a una larga lucha legal por parte de 320 extrabajadores de Sabsa, quienes desde hace 14 años exigen el cumplimiento de sus derechos laborales tras el cierre de la empresa estatal",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2011-01-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "año",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Yapacaní"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "trabajo",
                "empresa",
                "cierre"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La molestia del sector afectado se hizo visible el pasado 10 de enero, cuando realizaron una masiva protesta frente al Ministerio de Obras Públicas",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-01-10",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Yapacaní"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "trabajo",
                "protesta",
                "ministerio"
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
            "nombre": "Edgar Montaño Rojas",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Marcelo Cortez Candia",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Servicio de Aeropuertos Bolivianos S. A. (SABSA)",
            "tipo": "ORGANIZACION",
            "alias": [
                "SABSA"
            ]
        },
        {
            "nombre": "Ministerio de Obras Públicas",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Policía Boliviana",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Juzgado Público Civil, Comercial, de Partido del Trabajo y Seguridad Social de Yapacaní",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Buena Vista",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Justicia",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Elecciones",
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
            "cita": "\"Nos dijo públicamente que, en 15 días, con la sentencia de la justicia, se realizaría el pago, e incluso se comprometió a colaborar para agilizar el juicio. Sin embargo, todas las instancias han fallado a nuestro favor y ellos siguen apelando\"",
            "emisor_nombre": "Uno de los afectados",
            "contexto": "En una entrevista sobre la protesta realizada el 10 de enero",
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
            "indicador": "Diferencia salarial a pagar a extrabajadores de Sabsa",
            "categoria": "presupuestario",
            "valor_numerico": 55189880,
            "unidad": "Bs",
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
