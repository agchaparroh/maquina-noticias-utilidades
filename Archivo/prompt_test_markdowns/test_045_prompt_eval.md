# Evaluación Artículo: test_045
**Modelo Probado:** `llama-3.1-8b-instant`

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

## Resultados de las Tareas (llama-3.1-8b-instant)

### Tarea: relevancia

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 7,
    "justificacion_relevancia": "Relevancia alta debido a la decisión judicial contra un ministro boliviano",
    "categorias_asignadas": [
        "Política Nacional",
        "Justicia/Legal"
    ],
    "explicacion_concisa": "La justicia boliviana ordenó apremiar al ministro Edgar Montaño por deuda a extrabajadores de Sabsa, con un monto de más de Bs 55 millones. La medida busca ejecutar el pago de beneficios laborales a los trabajadores que llevan 14 años de espera."
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
            "contenido": "La justicia ordenó apremio del ministro Edgar Montaño por deuda a extrabajadores de Sabsa.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "justicia",
                "ministro",
                "deuda",
                "extrabajadores"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El juez Marcelo Cortez Candia emitió un mandamiento de apremio contra el ministro de Obras Públicas, Edgar Montaño Rojas.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "juez",
                "mandamiento",
                "apremio",
                "ministro"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La medida busca ejecutar el pago de más de Bs 55 millones en beneficios laborales a extrabajadores de la empresa aeroportuaria, quienes llevan 14 años de espera.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "pago",
                "beneficios",
                "extrabajadores",
                "empresa"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La decisión judicial responde a una larga lucha legal por parte de 320 extrabajadores de Sabsa, quienes desde hace 14 años exigen el cumplimiento de sus derechos laborales tras el cierre de la empresa estatal.",
            "tipo_hecho": "BIOGRAFIA",
            "fecha_ocurrencia_inicio": "2011-01-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "año",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 4,
            "etiquetas": [
                "extrabajadores",
                "Sabsa",
                "derechos laborales"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El ministro Montaño prometió pagar la deuda en 15 días después de la sentencia de la justicia.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-01-10",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 5,
            "confiabilidad": 3,
            "etiquetas": [
                "ministro",
                "promesa",
                "pago"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El mandamiento de apremio busca precisamente presionar al ministro para ejecutar la sentencia, que ordena que se paguen la diferencial salarial a los extrabajadores de Sabsa.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "mandamiento",
                "apremio",
                "sentencia"
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
            "alias": [
                "Edgar Montaño"
            ]
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
            "nombre": "Policía Boliviana",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Ministerio de Obras Públicas",
            "tipo": "INSTITUCION",
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
            "nombre": "Yapacaní",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Justicia",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Extrabajadores de Sabsa",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Elección de la sentencia",
            "tipo": "EVENTO",
            "alias": []
        },
        {
            "nombre": "Protesta frente al Ministerio de Obras Públicas",
            "tipo": "EVENTO",
            "alias": []
        },
        {
            "nombre": "Crisis laboral en Sabsa",
            "tipo": "CONCEPTO",
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
            "cita": "Nos dijo públicamente que, en 15 días, con la sentencia de la justicia, se realizaría el pago, e incluso se comprometió a colaborar para agilizar el juicio.",
            "emisor_nombre": "uno de los afectados",
            "contexto": "Durante una protesta frente al Ministerio de Obras Públicas el 10 de enero.",
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
            "indicador": "Diferencia salarial a pagar a extrabajadores de SABSA",
            "categoria": "presupuestario",
            "valor_numerico": 55189880,
            "unidad": "Bolivianos (Bs)",
            "ambito_geografico": [
                "Bolivia"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de extrabajadores de SABSA que demandan el pago de sus derechos laborales",
            "categoria": "demográfico",
            "valor_numerico": 320,
            "unidad": "personas",
            "ambito_geografico": [
                "Bolivia"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de años que llevan los extrabajadores de SABSA esperando el pago de sus derechos laborales",
            "categoria": "demográfico",
            "valor_numerico": 14,
            "unidad": "años",
            "ambito_geografico": [
                "Bolivia"
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
