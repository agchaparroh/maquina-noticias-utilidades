# Evaluación Artículo: test_063
**Modelo Probado:** `llama-3.1-8b-instant`

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

## Resultados de las Tareas (llama-3.1-8b-instant)

### Tarea: relevancia

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "Contiene información útil sobre la seguridad social de mexicanos en el extranjero",
    "categorias_asignadas": [
        "Política Nacional",
        "Economía",
        "Sociedad/Derechos"
    ],
    "explicacion_concisa": "El IMSS afilió a 13 mil 169 mexicanos que residen y trabajan en el extranjero, proporcionándoles acceso a la seguridad social y beneficios para sus familiares. El salario promedio de aseguramiento diario es de 388.25 pesos, equivalente a 19 dólares diarios."
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
                "salud",
                "seguridad social",
                "IMSS"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "De los beneficiarios titulares, el 38 por ciento son mujeres y el 62 por ciento son hombres.",
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
                "demografía",
                "género",
                "IMSS"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "7 mil 504 beneficiarios extendieron los beneficios a sus familiares.",
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
                "familia",
                "beneficios",
                "IMSS"
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
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "salario",
                "IMSS",
                "seguridad social"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El 47 por ciento de las personas mexicanas afiliadas al Instituto que radican en el extranjero se encuentran en el rango de edad de 51 a 60 años.",
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
                "edad",
                "demografía",
                "IMSS"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El 23 por ciento de las afiliaciones de mexicanos en el extranjero es por 12 meses.",
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
                "afiliación",
                "seguridad social",
                "IMSS"
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
            "nombre": "Ciudad de México",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS",
            "tipo": "NORMATIVA",
            "alias": []
        },
        {
            "nombre": "Instituto Mexicano del Seguro Social (IMSS)",
            "tipo": "INSTITUCION",
            "alias": [
                "IMSS"
            ]
        },
        {
            "nombre": "13ª edición de la Semana de Educación Financiera Integral para Mexicanas y Mexicanos en el Exterior (SEFIMME 2025)",
            "tipo": "EVENTO",
            "alias": [
                "SEFIMME 2025"
            ]
        },
        {
            "nombre": "Instituto de Mexicanas y Mexicanos en el Exterior (IMME)",
            "tipo": "INSTITUCION",
            "alias": [
                "IMME"
            ]
        },
        {
            "nombre": "Carolina Griselda Cisneros Prado",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Unidad de Medicina Familiar (UMF)",
            "tipo": "INSTITUCION",
            "alias": [
                "UMF"
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
        },
        {
            "nombre": "Seguro Social",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "México",
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
            "cita": "El 23 por ciento de las afiliaciones de mexicanos en el extranjero es por 12 meses. El 16 por ciento lo hace o decide pagar por 6 meses. En su mayoría, que son 7 mil 361 personas, lo hacen de manera mensual, y esto tiene que ver por los ingresos de una persona trabajadora independiente, que son variables",
            "emisor_nombre": "funcionaria del Seguro Social",
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
            "indicador": "Número de connacionales afiliados al Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS",
            "categoria": "demográfico",
            "valor_numerico": 13169,
            "unidad": "personas",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de connacionales afiliados al Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS con familiares afiliados",
            "categoria": "demográfico",
            "valor_numerico": 25960,
            "unidad": "personas",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de connacionales afiliados al Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS que son mujeres",
            "categoria": "demográfico",
            "valor_numerico": 38,
            "unidad": "%",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de trabajadoras afiliadas al Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS",
            "categoria": "demográfico",
            "valor_numerico": 5004,
            "unidad": "personas",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de empleados afiliados al Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS",
            "categoria": "demográfico",
            "valor_numerico": 8165,
            "unidad": "personas",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de connacionales afiliados al Programa de Trabajadores Independientes para Mexicanos en el Extranjero del IMSS que aseguraron su vigencia a partir de abril",
            "categoria": "demográfico",
            "valor_numerico": 13169,
            "unidad": "personas",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": "abril",
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de familiares registrados en una Unidad de Medicina Familiar (UMF) asociados a un titular que labora en Estados Unidos",
            "categoria": "demográfico",
            "valor_numerico": null,
            "unidad": "personas",
            "ambito_geografico": [
                "Chihuahua",
                "Jalisco",
                "Nuevo León"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de mexicanos en el extranjero que cuentan con una pensión",
            "categoria": "demográfico",
            "valor_numerico": 699,
            "unidad": "personas",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de personas mexicanas afiliadas al Instituto que radican en el extranjero en el rango de edad de 51 a 60 años",
            "categoria": "demográfico",
            "valor_numerico": 47,
            "unidad": "%",
            "ambito_geografico": [
                "México"
            ],
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
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Salario promedio de aseguramiento diario en dólares",
            "categoria": "económico",
            "valor_numerico": 19,
            "unidad": "dólares",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de aumento del salario promedio de aseguramiento diario",
            "categoria": "económico",
            "valor_numerico": 18,
            "unidad": "%",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas que han decidido continuar con su aseguramiento de manera continua por más de un año",
            "categoria": "demográfico",
            "valor_numerico": 2623,
            "unidad": "personas",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de afiliaciones de mexicanos en el extranjero por 12 meses",
            "categoria": "demográfico",
            "valor_numerico": 23,
            "unidad": "%",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje de afiliaciones de mexicanos en el extranjero por 6 meses",
            "categoria": "demográfico",
            "valor_numerico": 16,
            "unidad": "%",
            "ambito_geografico": [
                "México"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "IMSS",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas que afilian de manera mensual",
            "categoria": "demográfico",
            "valor_numerico": 7361,
            "unidad": "personas",
            "ambito_geografico": [
                "México"
            ],
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
