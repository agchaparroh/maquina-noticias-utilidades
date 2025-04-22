# Evaluación Artículo: test_051
**Modelo Probado:** `llama-3.1-8b-instant`

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.laprensa.com.ar/Una-familia-tipo-de-CABA-necesito-en-marzo-ingresos-por-mas-de-1147000-para-no-ser-pobre-558522.note.aspx           |
| **Título**     | Una familia tipo de CABA necesitó en marzo ingresos por más de $1.147.000 para no ser pobre       |
| **Medio**      | None         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-21T00:43:40.322753+00:00 |
| **Recopilado** | 2025-04-21T00:43:40.322777+00:00 |

---

## Contenido del Artículo Analizado

<details open>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Una familia tipo de CABA necesitó en marzo ingresos por más de $1.147.000 para no ser pobre
Las familias que residen en la Ciudad Autónoma de Buenos Aires (CABA) necesitaron durante marzo ingresos de al menos $1.147.602 para no ser pobres y de aunque sea $1.804.267 para ser consideradas de clase media, de acuerdo a lo informado por el Instituto de Estadísticas y Censos porteño (IDECBA).
El comportamiento de las canastas que se utilizan para determinar la línea de la pobreza e indigencia en la Ciudad, subieron hasta 7,22%, es decir que avanzaron por encima de la inflación en el tercer mes del año, que en el territorio porteño escaló hasta el 3,2%.
La medición se realiza considerando como una familia tipo a aquella compuesta por dos adultos y dos menores, que en el mes pasado necesitó ingresos por lo menos de $1.804.267 para ser de clase media, de al menos $1.147.602 para no ser pobre y aunque sea de $621.772 para no ser catalogada como indigente.
La Canasta Básica Alimentaria (CBA), que define el umbral de indigencia, trepó 7,22% en marzo, mientras que la Canasta Básica Total (CBT), que mide la pobreza, subió 5,32% en el tercer mes del 2025. De esta manera, en el mes pasado la línea de pobreza creció un 5,36% y la de indigencia se elevó un 6,91%.
El organismo estadístico porteño precisó que en relación con un año atrás, la línea de pobreza pasó de estar en $766.146 durante marzo de 2024 a $1.147.602 en el mismo mes del actual calendario.
En tanto que la línea de indigencia avanzó de $442.239 a $621.772.
ESTRATOS SEGÚN INGRESOS
- En situación de indigencia: hogares cuyo ingreso total mensual no alcanza para cubrir la Canasta Básica Alimentaria (CBA - Línea de indigencia). Tienen ingresos totales de hasta $621.772,34.
- En situación de pobreza no indigente: hogares cuyo ingreso total mensual no alcanza para cubrir la Canasta Básica Total (CBT - Línea de pobreza) pero permite al menos adquirir la CBA. Cuentan con un total de ingresos entre $621.772,35 y $1.147.601,97.
- No pobres vulnerables: hogares cuyo ingreso total mensual es de al menos la CBT y no alcanza la Canasta Total (CT) del Sistema de Canastas de Consumo. Registran ingresos totales entre $1.147.601,98 y $1.443.413,59.
- Sector medio frágil: hogares cuyo ingreso total mensual es de al menos la Canasta Total y no alcanza 1,25 veces la CT del Sistema de Canastas de Consumo. Tienen ingresos mensuales entre $1.443.413,60 y $1.804.266,99.
- Sector medio "clase media": hogares cuyo ingreso total mensual es de al menos 1,25 veces la CT y no alcanza cuatro veces la CT del Sistema de Canastas de Consumo. Ganan desde $1.804.266,00 hasta $5.773.654,39 al mes.
- Sector acomodado: hogares cuyo ingreso mensual supera cuatro CT del Sistema de Canastas de Consumo, con ingresos al mes de $5.773.654,40 en adelante.
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
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "La información sobre la línea de pobreza en CABA tiene relevancia media.",
    "categorias_asignadas": [
        "Sociedad/Derechos",
        "Economía"
    ],
    "explicacion_concisa": "El artículo informa sobre la línea de pobreza en la Ciudad Autónoma de Buenos Aires, donde una familia tipo necesitó ingresos de al menos $1.147.602 para no ser pobre en marzo. La Canasta Básica Alimentaria y la Canasta Básica Total subieron en marzo, lo que afectó la línea de pobreza e indigencia."
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
            "contenido": "Una familia tipo de CABA necesitó en marzo ingresos por más de $1.147.000 para no ser pobre.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "mes",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [
                "CABA"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "pobreza",
                "ingresos",
                "CABA"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Las familias que residen en la Ciudad Autónoma de Buenos Aires (CABA) necesitaron durante marzo ingresos de al menos $1.804.267 para ser consideradas de clase media.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "mes",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [
                "CABA"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "clase media",
                "ingresos",
                "CABA"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La Canasta Básica Alimentaria (CBA) trepó 7,22% en marzo.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "CBA",
                "inflación",
                "marzo"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La Canasta Básica Total (CBT) subió 5,32% en el tercer mes del 2025.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "CBT",
                "inflación",
                "marzo"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La línea de pobreza creció un 5,36% en el mes pasado.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "pobreza",
                "línea de pobreza",
                "marzo"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La línea de indigencia se elevó un 6,91% en el mes pasado.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "indigencia",
                "línea de indigencia",
                "marzo"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "En relación con un año atrás, la línea de pobreza pasó de estar en $766.146 durante marzo de 2024 a $1.147.602 en el mismo mes del actual calendario.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2024-03-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "pobreza",
                "línea de pobreza",
                "2024"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "En tanto que la línea de indigencia avanzó de $442.239 a $621.772.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2024-03-01",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "indigencia",
                "línea de indigencia",
                "2024"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El comportamiento de las canastas que se utilizan para determinar la línea de la pobreza e indigencia en la Ciudad subieron hasta 7,22%, es decir que avanzaron por encima de la inflación en el tercer mes del año, que en el territorio porteño escaló hasta el 3,2%.",
            "tipo_hecho": "EXPLICACIÓN",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": null,
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [
                "CABA"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "pobreza",
                "indigencia",
                "inflación"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La medición se realiza considerando como una familia tipo a aquella compuesta por dos adultos y dos menores, que en el mes pasado necesitó ingresos por lo menos de $1.804.267 para ser de clase media, de al menos $1.147.602 para no ser pobre y aunque sea de $621.772 para no ser catalogada como indigente.",
            "tipo_hecho": "EXPLICACIÓN",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": null,
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [
                "CABA"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "familias",
                "ingresos",
                "clase media"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La Canasta Básica Alimentaria (CBA) define el umbral de indigencia.",
            "tipo_hecho": "CONCEPTO",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": null,
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "CBA",
                "indigencia",
                "concepto"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La Canasta Básica Total (CBT) mide la pobreza.",
            "tipo_hecho": "CONCEPTO",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": null,
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "CBT",
                "pobreza",
                "concepto"
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
            "nombre": "Ciudad Autónoma de Buenos Aires (CABA)",
            "tipo": "LUGAR",
            "alias": [
                "CABA"
            ]
        },
        {
            "nombre": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "tipo": "INSTITUCION",
            "alias": [
                "IDECBA"
            ]
        },
        {
            "nombre": "Canasta Básica Alimentaria (CBA)",
            "tipo": "CONCEPTO",
            "alias": [
                "CBA"
            ]
        },
        {
            "nombre": "Canasta Básica Total (CBT)",
            "tipo": "CONCEPTO",
            "alias": [
                "CBT"
            ]
        },
        {
            "nombre": "Sistema de Canastas de Consumo",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "Línea de indigencia",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "Línea de pobreza",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "Sector acomodado",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "Sector medio frágil",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "Sector medio 'clase media'",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "No pobres vulnerables",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "En situación de indigencia",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "En situación de pobreza no indigente",
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
            "cita": "hogares cuyo ingreso total mensual no alcanza para cubrir la Canasta Básica Alimentaria (CBA - Línea de indigencia). Tienen ingresos totales de hasta $621.772,34.",
            "emisor_nombre": "IDECBA",
            "contexto": "En tanto que la línea de indigencia avanzó de $442.239 a $621.772.",
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso total mensual no alcanza para cubrir la Canasta Básica Total (CBT - Línea de pobreza) pero permite al menos adquirir la CBA. Cuentan con un total de ingresos entre $621.772,35 y $1.147.601,97.",
            "emisor_nombre": "IDECBA",
            "contexto": "En tanto que la línea de indigencia avanzó de $442.239 a $621.772.",
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso total mensual es de al menos la CBT y no alcanza la Canasta Total (CT) del Sistema de Canastas de Consumo. Registran ingresos totales entre $1.147.601,98 y $1.443.413,59.",
            "emisor_nombre": "IDECBA",
            "contexto": "En tanto que la línea de indigencia avanzó de $442.239 a $621.772.",
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso total mensual es de al menos la Canasta Total y no alcanza 1,25 veces la CT del Sistema de Canastas de Consumo. Tienen ingresos mensuales entre $1.443.413,60 y $1.804.266,99.",
            "emisor_nombre": "IDECBA",
            "contexto": "En tanto que la línea de indigencia avanzó de $442.239 a $621.772.",
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso total mensual es de al menos 1,25 veces la CT y no alcanza cuatro veces la CT del Sistema de Canastas de Consumo. Ganan desde $1.804.266,00 hasta $5.773.654,39 al mes.",
            "emisor_nombre": "IDECBA",
            "contexto": "En tanto que la línea de indigencia avanzó de $442.239 a $621.772.",
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso mensual supera cuatro CT del Sistema de Canastas de Consumo, con ingresos al mes de $5.773.654,40 en adelante.",
            "emisor_nombre": "IDECBA",
            "contexto": "En tanto que la línea de indigencia avanzó de $442.239 a $621.772.",
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
            "indicador": "Ingresos mensuales necesarios para no ser pobre en CABA",
            "categoria": "económico",
            "valor_numerico": 1147602,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para ser considerados de clase media en CABA",
            "categoria": "económico",
            "valor_numerico": 1804267,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para no ser catalogado como indigente en CABA",
            "categoria": "económico",
            "valor_numerico": 621772,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Aumento porcentual de la Canasta Básica Alimentaria (CBA) en marzo",
            "categoria": "económico",
            "valor_numerico": 7.22,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Aumento porcentual de la Canasta Básica Total (CBT) en marzo",
            "categoria": "económico",
            "valor_numerico": 5.32,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Aumento porcentual de la línea de pobreza en marzo",
            "categoria": "económico",
            "valor_numerico": 5.36,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Aumento porcentual de la línea de indigencia en marzo",
            "categoria": "económico",
            "valor_numerico": 6.91,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para estar en situación de indigencia en CABA",
            "categoria": "económico",
            "valor_numerico": 621772,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para estar en situación de pobreza no indigente en CABA",
            "categoria": "económico",
            "valor_numerico": 1147602,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para estar en situación de no pobres vulnerables en CABA",
            "categoria": "económico",
            "valor_numerico": 1443414,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para estar en situación de sector medio frágil en CABA",
            "categoria": "económico",
            "valor_numerico": 1804267,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para estar en situación de sector medio 'clase media' en CABA",
            "categoria": "económico",
            "valor_numerico": 1804267,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para estar en situación de sector acomodado en CABA",
            "categoria": "económico",
            "valor_numerico": 5773654,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para estar en situación de indigencia en marzo de 2024 en CABA",
            "categoria": "económico",
            "valor_numerico": 766146,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2024-03",
            "periodo_referencia_fin": "2024-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos mensuales necesarios para estar en situación de indigencia en marzo de 2025 en CABA",
            "categoria": "económico",
            "valor_numerico": 621772,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires (CABA)"
            ],
            "periodo_referencia_inicio": "2025-03",
            "periodo_referencia_fin": "2025-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        }
    ]
}
```
</details>
