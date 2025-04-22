# Evaluación Artículo: test_054
**Modelo Probado:** `llama-3.1-8b-instant`

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://eldeber.com.bo/pais/justicia-ordena-aprehension-del-ministro-edgar-montano-por-deuda-extrabajadores-de-sabsa_510601/           |
| **Título**     | Justicia ordena apremio del ministro Edgar Montaño por deuda a extrabajadores de Sabsa       |
| **Medio**      | El Deber         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T22:01:30+00:00 |
| **Recopilado** | 2025-04-21T00:43:41.030310+00:00 |

---

## Contenido del Artículo Analizado

<details open>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Justicia ordena apremio del ministro Edgar Montaño por deuda a extrabajadores de Sabsa
La medida busca ejecutar el pago de más de Bs 55 millones en beneficios laborales a extrabajadores de la extinta empresa aeroportuaria, quienes llevan tres años de espera
El juez Marcelo Cortez Candia, del Juzgado Público Civil, Comercial, de Partido del Trabajo y Seguridad Social de Yapacaní, emitió un mandamiento de apremio contra el ministro de Obras Públicas, Edgar Montaño Rojas, en el marco de un proceso judicial iniciado por extrabajadores del extinto Servicio de Aeropuertos Bolivianos S. A. (SABSA).
La disposición instruye a la Policía Boliviana aprehender a Montaño y trasladarlo a la carceleta de Buena Vista, hasta que se concrete el pago de Bs 55.189.880, por concepto de finiquitos pendientes a los extrabajadores que lo demandaron.
La decisión judicial responde a una larga lucha legal por parte de más de 600 extrabajadores a nivel nacional —190 de ellos en Santa Cruz— quienes desde hace tres años exigen el cumplimiento de sus derechos laborales tras el cierre de la empresa estatal.
La molestia del sector afectado se hizo visible el pasado 10 de enero, cuando realizaron una masiva protesta frente al Ministerio de Obras Públicas. En esa ocasión, denunciaron que, pese a las promesas públicas del ministro Montaño, el desembolso nunca se concretó.
“Nos dijo públicamente que, en 15 días, con la sentencia de la justicia, se realizaría el pago, e incluso se comprometió a colaborar para agilizar el juicio. Sin embargo, todas las instancias han fallado a nuestro favor y ellos siguen apelando”, lamentó uno de los afectados.
Los exempleados denuncian que las acciones del ministerio han sido dilatorias y que, aunque han recibido pagos parciales que suman apenas Bs 50.000 en tres años, la deuda total continúa pendiente. “Nos sentimos desamparados, pese a que la justicia nos ha respaldado en todas las instancias”, afirmaron durante la movilización.
El mandamiento de apremio busca precisamente presionar al ministro para ejecutar la sentencia, que ordena que se paguen los beneficios sociales a los extrabajadores de Sabsa.
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
    "justificacion_relevancia": "Relevancia alta debido a la decisión judicial contra un ministro y la deuda laboral pendiente",
    "categorias_asignadas": [
        "Justicia/Legal",
        "Política Nacional"
    ],
    "explicacion_concisa": "La justicia boliviana ordenó apremiar al ministro de Obras Públicas, Edgar Montaño, por una deuda laboral de más de Bs 55 millones a favor de ex trabajadores de SABSA. La medida busca ejecutar el pago de beneficios laborales pendientes a más de 600 extrabajadores que llevan tres años de espera."
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
            "contenido": "Justicia ordena apremio del ministro Edgar Montaño por deuda a extrabajadores de Sabsa.",
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
            "tipo_hecho": "DECLARACION",
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
                "ministro",
                "apremio"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La medida busca ejecutar el pago de más de Bs 55 millones en beneficios laborales a extrabajadores de la extinta empresa aeroportuaria, Sabsa.",
            "tipo_hecho": "ANUNCIO",
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
                "extrabajadores"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La decisión judicial responde a una larga lucha legal por parte de más de 600 extrabajadores a nivel nacional —190 de ellos en Santa Cruz— quienes desde hace tres años exigen el cumplimiento de sus derechos laborales tras el cierre de la empresa estatal.",
            "tipo_hecho": "BIOGRAFIA",
            "fecha_ocurrencia_inicio": "2022-01-01",
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
                "derechos laborales",
                "empresa estatal"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El mandamiento de apremio busca precisamente presionar al ministro para ejecutar la sentencia, que ordena que se paguen los beneficios sociales a los extrabajadores de Sabsa.",
            "tipo_hecho": "DECLARACION",
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
                "beneficios sociales"
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
            "nombre": "Sabsa",
            "tipo": "ORGANIZACION",
            "alias": [
                "Servicio de Aeropuertos Bolivianos S. A."
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
            "nombre": "Buena Vista",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Santa Cruz",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Juzgado Público Civil, Comercial, de Partido del Trabajo y Seguridad Social de Yapacaní",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Justicia",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Elecciones Generales Bolivia 2023",
            "tipo": "EVENTO",
            "alias": []
        },
        {
            "nombre": "Crisis Migratoria",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "Caso Gürtel",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "Protesta frente al Ministerio de Obras Públicas",
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
            "cita": "Nos dijo públicamente que, en 15 días, con la sentencia de la justicia, se realizaría el pago, e incluso se comprometió a colaborar para agilizar el juicio.",
            "emisor_nombre": "uno de los afectados",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "Nos sentimos desamparados, pese a que la justicia nos ha respaldado en todas las instancias",
            "emisor_nombre": "exempleados",
            "contexto": null,
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
            "indicador": "Monto total de la deuda pendiente de pago a extrabajadores de SABSA",
            "categoria": "presupuestario",
            "valor_numerico": 55189880,
            "unidad": "Bolivianos",
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
            "indicador": "Monto total de pagos parciales recibidos por los extrabajadores de SABSA",
            "categoria": "presupuestario",
            "valor_numerico": 50000,
            "unidad": "Bolivianos",
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
            "indicador": "Número de extrabajadores de SABSA que exigen el cumplimiento de sus derechos laborales",
            "categoria": "demográfico",
            "valor_numerico": 600,
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
            "indicador": "Número de extrabajadores de SABSA en Santa Cruz",
            "categoria": "demográfico",
            "valor_numerico": 190,
            "unidad": "personas",
            "ambito_geografico": [
                "Santa Cruz"
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
