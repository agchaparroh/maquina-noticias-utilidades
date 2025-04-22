# Evaluación Artículo: test_063

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

<details>
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

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 0.58s | 1435.0 | 0.10 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 1.29s | 2793.0 | 0.28 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 1.53s | 1949.0 | 0.29 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 1.71s | 1553.0 | 0.09 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 2.90s | 3343.0 | 0.72 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.58s
- **Tokens prompt:** 1301.0
- **Tokens respuesta:** 134.0
- **Total tokens:** 1435.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "Afecta a la seguridad social de mexicanos en el extranjero y su acceso a beneficios",
    "categorias_asignadas": [
        "Economía",
        "Justicia/Legal"
    ],
    "explicacion_concisa": "El IMSS afilió a 13,169 mexicanos que trabajan y residen en el extranjero, extendiendo beneficios a sus familiares y ofreciendo acceso a la seguridad social. El 38% de los beneficiarios son mujeres y el 62% son hombres."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.29s
- **Tokens prompt:** 2176.0
- **Tokens respuesta:** 617.0
- **Total tokens:** 2793.0


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
                "seguridad social",
                "trabajadores extranjeros",
                "IMSS"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "7 mil 504 personas extendieron los beneficios a sus familiares.",
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
                "seguridad social",
                "beneficios familiares",
                "IMSS"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El 38 por ciento de los beneficiarios titulares son mujeres.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "MX"
            ],
            "ubicaciones_especificas": [],
            "importancia": 5,
            "confiabilidad": 4,
            "etiquetas": [
                "demografía",
                "seguridad social",
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
            "importancia": 6,
            "confiabilidad": 4,
            "etiquetas": [
                "salario",
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

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.53s
- **Tokens prompt:** 1508.0
- **Tokens respuesta:** 441.0
- **Total tokens:** 1949.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Instituto Mexicano del Seguro Social (IMSS)",
            "tipo": "INSTITUCION",
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
            "nombre": "Programa de Trabajadores Independientes para Mexicanos en el Extranjero",
            "tipo": "PROGRAMA",
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
            "nombre": "Semana de Educación Financiera Integral para Mexicanas y Mexicanos en el Exterior (SEFIMME 2025)",
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
        }
    ]
}
```
</details>


### Tarea: extraccion_citas

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.71s
- **Tokens prompt:** 1420.0
- **Tokens respuesta:** 133.0
- **Total tokens:** 1553.0


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

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 2.90s
- **Tokens prompt:** 1939.0
- **Tokens respuesta:** 1404.0
- **Total tokens:** 3343.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Número de mexicanos afiliados al IMSS en el extranjero",
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
            "indicador": "Número de familiares de mexicanos afiliados al IMSS en el extranjero",
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
            "indicador": "Porcentaje de mujeres afiliadas al IMSS en el extranjero",
            "categoria": "demográfico",
            "valor_numerico": 0.38,
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
            "indicador": "Número de trabajadoras mexicanas afiliadas al IMSS en el extranjero",
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
            "indicador": "Número de empleados mexicanos afiliados al IMSS en el extranjero",
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
            "indicador": "Número de mexicanos en el extranjero con pensiones",
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
            "indicador": "Porcentaje de mexicanos en el extranjero con edad entre 51 y 60 años",
            "categoria": "demográfico",
            "valor_numerico": 0.47,
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
            "indicador": "Salario promedio diario de aseguramiento",
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
            "indicador": "Porcentaje de aumento del salario promedio diario de aseguramiento",
            "categoria": "económico",
            "valor_numerico": 0.18,
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
            "indicador": "Número de personas que han decidido continuar con su aseguramiento de manera continua",
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
            "valor_numerico": 0.23,
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
            "valor_numerico": 0.16,
            "unidad": "%",
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
