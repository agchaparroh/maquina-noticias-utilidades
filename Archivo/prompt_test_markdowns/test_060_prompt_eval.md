# Evaluación Artículo: test_060
**Modelo Probado:** `llama-3.1-8b-instant`

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.elmostrador.cl/noticias/pais/2025/04/14/funcionarios-de-bbnn-no-se-presentan-en-comision-investigadora-por-fallida-compra-de-casa-de-allende/           |
| **Título**     | Funcionarios de BBNN no se presentan en comisión investigadora por fallida compra de casa de Allende       |
| **Medio**      | El Mostrador         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T00:00:00+00:00 |
| **Recopilado** | 2025-04-21T00:43:53.909018+00:00 |

---

## Contenido del Artículo Analizado

<details open>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Funcionarios de BBNN no se presentan en comisión investigadora por fallida compra de casa de Allende
El presidente de la comisión, Andrés Longton (RN), anunció que enviarán los antecedentes a Contraloría por la inasistencia de los funcionarios de Bienes Nacionales. Mientras, la diputada Paula Labra (IND-RN) criticó duramente a los ausentes. Se anunció envío de un cuestionario al Presidente Boric.
Por casi 50 minutos sesionó la Comsión Investigadora por la fallida compra de la casa del expresidente Salvador Allende. Pero la tónica estuvo marcada por la ausencia de los funcionarios del Ministerio de Bienes Nacionales. El ministro Francisco Figueroa se había excusado de la instancia por motivos personales. Está pronto a ser padre. Sin embargo, el resto de los convocados no se presentó.
El presidente de la instancia, Andrés Longton (RN) -a solicitud de la diputada Paula Labra (Ind-RN)- enviará los antecedentes a la Contraloría “para que sean sancionados en razón de su inasistencia”. “Los funcionarios citados que participaron en esta operación no tenían ninguna excusa, porque no pueden andar guiados, coachings o dirigidos por otra persona”, argumentó el diputado Longton.
Su ausencia, aseguró, termina “obstruyendo las investigaciones, sobre todo a raíz de las inaceptables declaraciones de la Jefa Jurídica (de la Segpres) que sorprendentemente sigue en funciones, la señora Francisca Moya”. En la misma línea, el parlamentario insistió que “eran determinantes las declaraciones que podían dar los funcionarios citados acá en la comisión investigadora y que lamentablemente terminan retrasando esta investigación”.
La diputada Labra arremetió contra los funcionarios afirmando que “esto no es una citación institucional. Ya no estamos en el jardín infantil y no se necesita la supervisión del ministro que tenía, por supuesto, una excusa muy atendible”. Para la parlamentaria “los funcionarios públicos tenían la responsabilidad y el deber de asistir”.
Labra aseguró que seguirán trabajando “hasta determinar las últimas responsabilidades políticas del escándalo político más grande del último tiempo”.
Respecto de las próximas sesiones, el presidente de la comisión, el diputado Longton, adelantó que la exjefa jurídica de BB.NN que participó en el proceso de la fallida compra de la casa del expresidente Allende, Macarena Díez, “ya confirmó que va a venir. Tenemos que reagendar la fecha porque también tuvo un problema de salud”. Aseguró que “no teniendo la obligación, manifestó su disposición. Lo mismo la exministra Marcela Sandoval, que está invitada y ya confirmó para el próximo día lunes”, el referencia a la próximas semana.
Finalmente, el diputado afirmó que se enviará un cuestionario al Presidente Gabriel Boric, como lo hizo en su momento la comisión Investigadora sobre el exsubsecretario Manuel Monsalve, y que los diputados integrantes tendrán hasta el lunes próximo para enviar sus preguntas.
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
    "justificacion_relevancia": "La ausencia de funcionarios de Bienes Nacionales obstaculiza la investigación sobre la fallida compra de la casa de Allende.",
    "categorias_asignadas": [
        "Política Nacional",
        "Justicia/Legal"
    ],
    "explicacion_concisa": "La comisión investigadora por la fallida compra de la casa de Salvador Allende se vio obstaculizada por la ausencia de funcionarios de Bienes Nacionales, lo que generó críticas de la diputada Paula Labra. La comisión decidió enviar los antecedentes a la Contraloría para que sean sancionados."
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
            "contenido": "Funcionarios de BBNN no se presentan en comisión investigadora por fallida compra de casa de Allende.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "compra",
                "Allende"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Presidente de la comisión, Andrés Longton, envía antecedentes a Contraloría por inasistencia de funcionarios de Bienes Nacionales.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "comisión",
                "Contraloría"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Diputada Paula Labra critica duramente a funcionarios ausentes en comisión investigadora.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "comisión",
                "Labra"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Se enviará un cuestionario al Presidente Gabriel Boric.",
            "tipo_hecho": "ANUNCIO",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "Boric",
                "cuestionario"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Exjefa jurídica de BB.NN, Macarena Díez, confirmó que va a venir a la comisión investigadora.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "comisión",
                "Díez"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Exministra Marcela Sandoval confirmó para el próximo día lunes.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "comisión",
                "Sandoval"
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
            "nombre": "Bienes Nacionales (BBNN)",
            "tipo": "ORGANIZACION",
            "alias": [
                "BBNN"
            ]
        },
        {
            "nombre": "Andrés Longton",
            "tipo": "PERSONA",
            "alias": [
                "Longton"
            ]
        },
        {
            "nombre": "Paula Labra",
            "tipo": "PERSONA",
            "alias": [
                "Labra"
            ]
        },
        {
            "nombre": "Gabriel Boric",
            "tipo": "PERSONA",
            "alias": [
                "Boric"
            ]
        },
        {
            "nombre": "Francisco Figueroa",
            "tipo": "PERSONA",
            "alias": [
                "Figueroa"
            ]
        },
        {
            "nombre": "Francisca Moya",
            "tipo": "PERSONA",
            "alias": [
                "Moya"
            ]
        },
        {
            "nombre": "Macarena Díez",
            "tipo": "PERSONA",
            "alias": [
                "Díez"
            ]
        },
        {
            "nombre": "Marcela Sandoval",
            "tipo": "PERSONA",
            "alias": [
                "Sandoval"
            ]
        },
        {
            "nombre": "Manuel Monsalve",
            "tipo": "PERSONA",
            "alias": [
                "Monsalve"
            ]
        },
        {
            "nombre": "Salvador Allende",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Comisión Investigadora",
            "tipo": "INSTITUCION",
            "alias": [
                "Comisión"
            ]
        },
        {
            "nombre": "Contraloría",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Segpres",
            "tipo": "ORGANIZACION",
            "alias": [
                "Segpres"
            ]
        },
        {
            "nombre": "RN",
            "tipo": "ORGANIZACION",
            "alias": [
                "RN"
            ]
        },
        {
            "nombre": "IND-RN",
            "tipo": "ORGANIZACION",
            "alias": [
                "IND-RN"
            ]
        },
        {
            "nombre": "Chile",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Casa de Allende",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Elección",
            "tipo": "EVENTO",
            "alias": []
        },
        {
            "nombre": "Crisis Migratoria",
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
            "cita": "Los funcionarios citados que participaron en esta operación no tenían ninguna excusa, porque no pueden andar guiados, coachings o dirigidos por otra persona",
            "emisor_nombre": "Andrés Longton",
            "contexto": "Argumentó que los funcionarios citados no tenían excusa para no asistir a la comisión investigadora",
            "fecha_cita": null
        },
        {
            "cita": "eran determinantes las declaraciones que podían dar los funcionarios citados acá en la comisión investigadora y que lamentablemente terminan retrasando esta investigación",
            "emisor_nombre": "Andrés Longton",
            "contexto": "Insistió en que las declaraciones de los funcionarios citados eran determinantes para la investigación",
            "fecha_cita": null
        },
        {
            "cita": "esto no es una citación institucional. Ya no estamos en el jardín infantil y no se necesita la supervisión del ministro que tenía, por supuesto, una excusa muy atendible",
            "emisor_nombre": "Paula Labra",
            "contexto": "Arremetió contra los funcionarios afirmando que no necesitaban supervisión",
            "fecha_cita": null
        },
        {
            "cita": "los funcionarios públicos tenían la responsabilidad y el deber de asistir",
            "emisor_nombre": "Paula Labra",
            "contexto": "Afirmó que los funcionarios públicos tenían la responsabilidad de asistir a la comisión investigadora",
            "fecha_cita": null
        },
        {
            "cita": "ya confirmó que va a venir. Tenemos que reagendar la fecha porque también tuvo un problema de salud",
            "emisor_nombre": "Andrés Longton",
            "contexto": "Anunció que la exjefa jurídica de BB.NN, Macarena Díez, confirmó su asistencia a la comisión investigadora",
            "fecha_cita": null
        },
        {
            "cita": "no teniendo la obligación, manifestó su disposición. Lo mismo la exministra Marcela Sandoval, que está invitada y ya confirmó para el próximo día lunes",
            "emisor_nombre": "Andrés Longton",
            "contexto": "Afirmó que la exministra Marcela Sandoval confirmó su asistencia a la comisión investigadora",
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
            "indicador": "Número de funcionarios de Bienes Nacionales que no se presentaron en la comisión investigadora",
            "categoria": "electoral",
            "valor_numerico": 50,
            "unidad": "minutos",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de funcionarios de Bienes Nacionales que participaron en la operación",
            "categoria": "electoral",
            "valor_numerico": 1,
            "unidad": "persona",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de sesiones de la comisión investigadora",
            "categoria": "electoral",
            "valor_numerico": 1,
            "unidad": "sesión",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de días que el ministro Francisco Figueroa se excusó de la instancia",
            "categoria": "electoral",
            "valor_numerico": 1,
            "unidad": "día",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de días que la exjefa jurídica Macarena Díez se excusó de la instancia",
            "categoria": "electoral",
            "valor_numerico": 1,
            "unidad": "día",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de días que la exministra Marcela Sandoval se excusó de la instancia",
            "categoria": "electoral",
            "valor_numerico": 1,
            "unidad": "día",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de días que el Presidente Gabriel Boric tendrá para responder al cuestionario",
            "categoria": "electoral",
            "valor_numerico": 7,
            "unidad": "días",
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
