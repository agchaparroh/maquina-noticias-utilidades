# Evaluación Artículo: test_063
**Modelo Probado:** `llama3-8b-8192`

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.jornada.com.mx/noticia/2025/04/14/politica/afilio-imss-a-13-mil-169-connacionales-que-residen-y-trabajan-en-el-extranjero           |
| **Título**     | Afilió IMSS a 13 mil 169 mexicanos que residen y trabajan en el extranjero       |
| **Medio**      | La Jornada         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T16:33:00-06:00 |
| **Recopilado** | 2025-04-21T00:44:05.983909+00:00 |

---

## Contenido del Artículo Analizado

<details open>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Ciudad de México. A través del Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS, el Instituto afilió a 13 mil 169 connacionales que residen y trabajan fuera del país. De ellos, 7 mil 504 extendieron los beneficios a sus familiares (principalmente hijos), 12 mil 791 personas, lo cual suma un total de 25 mil 960 personas con acceso a la seguridad social.
En el Instituto Mexicano del Seguro Social (IMSS), en un comunicado informó que de los beneficiarios titulares, el 38 por ciento son mujeres, 5 mil 004 trabajadoras, y el 62 por ciento son hombres, 8 mil 165 empleados.
En el marco de la 13ª edición de la Semana de Educación Financiera Integral para Mexicanas y Mexicanos en el Exterior (SEFIMME 2025), iniciativa del Instituto de Mexicanas y Mexicanos en el Exterior (IMME), la titular de la Coordinación de Afiliación, adscrita a la Unidad de Incorporación al Seguro Social, Carolina Griselda Cisneros Prado, indicó que los afiliados a este programa han asegurado su vigencia a partir de abril.
Indicó que las familiares registradas en una Unidad de Medicina Familiar (UMF) asociados a un titular que labora en Estados Unidos se encuentran en Chihuahua, Jalisco y Nuevo León.
La funcionaria del Seguro Social expuso que, en cuanto a las pensiones, 699 mexicanos en el extranjero cuentan con una. El 47 por ciento de las personas mexicanas afiliadas al Instituto que radican en el extranjero se encuentran en el rango de edad de 51 a 60 años.
Añadió que el salario promedio de aseguramiento diario es de 388.25 pesos, equivalente a 19 dólares diarios, es decir, un 18 por ciento superior al salario promedio registrado para trabajadores independientes en México.
2 mil 623 personas que han decidido continuar con su aseguramiento de manera continua por más de un año. “El 23 por ciento de las afiliaciones de mexicanos en el extranjero es por 12 meses. El 16 por ciento lo hace o decide pagar por 6 meses. En su mayoría, que son 7 mil 361 personas, lo hacen de manera mensual, y esto tiene que ver por los ingresos de una persona trabajadora independiente, que son variables”, dijo.
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
    "justificacion_relevancia": "Afiliación de mexicanos en el extranjero al IMSS, con impacto en la seguridad social y pensiones.",
    "categorias_asignadas": [
        "Economía",
        "Justicia/Legal"
    ],
    "explicacion_concisa": "El IMSS afilió a 13,169 mexicanos que trabajan y residen en el extranjero, con acceso a seguridad social y pensiones. El 38% son mujeres y el 62% son hombres, con un salario promedio diario de 388.25 pesos."
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
            "contenido": "El IMSS afilió a 13 mil 169 mexicanos que residen y trabajan en el extranjero.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "MX"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "IMSS",
                "seguridad social",
                "trabajadores extranjeros"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "7 mil 504 mexicanos extendieron los beneficios a sus familiares.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "MX"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "IMSS",
                "seguridad social",
                "familiares"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El 38 por ciento de los beneficiarios titulares son mujeres y el 62 por ciento son hombres.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "MX"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "IMSS",
                "seguridad social",
                "genero"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Las familiares registradas en una Unidad de Medicina Familiar (UMF) asociados a un titular que labora en Estados Unidos se encuentran en Chihuahua, Jalisco y Nuevo León.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "MX",
                "US"
            ],
            "ubicaciones_especificas": [
                "Chihuahua",
                "Jalisco",
                "Nuevo León"
            ],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "IMSS",
                "seguridad social",
                "UMF",
                "Estados Unidos"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El salario promedio de aseguramiento diario es de 388.25 pesos, equivalente a 19 dólares diarios.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "MX"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "IMSS",
                "seguridad social",
                "salario"
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
            "nombre": "Instituto Mexicano del Seguro Social (IMSS)",
            "tipo": "ORGANIZACION",
            "alias": [
                "IMSS"
            ]
        },
        {
            "nombre": "Ciudad de México",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS",
            "tipo": "PROGRAMA",
            "alias": []
        },
        {
            "nombre": "Carolina Griselda Cisneros Prado",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Unidad de Medicina Familiar (UMF)",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Instituto de Mexicanas y Mexicanos en el Exterior (IMME)",
            "tipo": "ORGANIZACION",
            "alias": [
                "IMME"
            ]
        },
        {
            "nombre": "Semana de Educación Financiera Integral para Mexicanas y Mexicanos en el Exterior (SEFIMME 2025)",
            "tipo": "EVENTO",
            "alias": [
                "SEFIMME 2025"
            ]
        },
        {
            "nombre": "Estados Unidos",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Chihuahua",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Jalisco",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Nuevo León",
            "tipo": "LUGAR",
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
            "cita": "\"El 23 por ciento de las afiliaciones de mexicanos en el extranjero es por 12 meses. El 16 por ciento lo hace o decide pagar por 6 meses. En su mayoría, que son 7 mil 361 personas, lo hacen de manera mensual, y esto tiene que ver por los ingresos de una persona trabajadora independiente, que son variables\"",
            "emisor_nombre": "Carolina Griselda Cisneros Prado",
            "contexto": "Durante la 13ª edición de la Semana de Educación Financiera Integral para Mexicanas y Mexicanos en el Exterior (SEFIMME 2025)",
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
            "indicador": "Número de connacionales afiliados al Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS",
            "categoria": "demográfico",
            "valor_numerico": 13169,
            "unidad": "personas",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de beneficiarios titulares con acceso a la seguridad social",
            "categoria": "demográfico",
            "valor_numerico": 25960,
            "unidad": "personas",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de beneficiarios titulares mujeres",
            "categoria": "demográfico",
            "valor_numerico": 0.38,
            "unidad": "%",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de trabajadoras afiliadas",
            "categoria": "demográfico",
            "valor_numerico": 5004,
            "unidad": "personas",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de empleados afiliados",
            "categoria": "demográfico",
            "valor_numerico": 8165,
            "unidad": "personas",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas con pensiones",
            "categoria": "demográfico",
            "valor_numerico": 699,
            "unidad": "personas",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de personas mexicanas afiliadas en el rango de edad de 51 a 60 años",
            "categoria": "demográfico",
            "valor_numerico": 0.47,
            "unidad": "%",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Salario promedio de aseguramiento diario",
            "categoria": "económico",
            "valor_numerico": 388.25,
            "unidad": "pesos",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Salario promedio en dólares diarios",
            "categoria": "económico",
            "valor_numerico": 19,
            "unidad": "dólares",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de aumento del salario promedio",
            "categoria": "económico",
            "valor_numerico": 0.18,
            "unidad": "%",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas que han decidido continuar con su aseguramiento de manera continua",
            "categoria": "demográfico",
            "valor_numerico": 2623,
            "unidad": "personas",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de afiliaciones de mexicanos en el extranjero por 12 meses",
            "categoria": "demográfico",
            "valor_numerico": 0.23,
            "unidad": "%",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de afiliaciones de mexicanos en el extranjero por 6 meses",
            "categoria": "demográfico",
            "valor_numerico": 0.16,
            "unidad": "%",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas que pagan su aseguramiento mensualmente",
            "categoria": "demográfico",
            "valor_numerico": 7361,
            "unidad": "personas",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        }
    ]
}
```
</details>
