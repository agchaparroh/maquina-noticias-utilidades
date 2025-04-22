# Evaluación Artículo: test_060

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

<details>
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

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 1.72s | 1403.0 | 0.10 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 1.16s | 3026.0 | 0.28 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 1.23s | 2079.0 | 0.23 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 1.52s | 1916.0 | 0.19 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 0.89s | 2462.0 | 0.16 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.72s
- **Tokens prompt:** 1274.0
- **Tokens respuesta:** 129.0
- **Total tokens:** 1403.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "La investigación sobre la compra de la casa de Allende tiene relevancia política y legal en Chile.",
    "categorias_asignadas": [
        "Justicia/Legal",
        "Política Nacional"
    ],
    "explicacion_concisa": "La comisión investigadora sobre la fallida compra de la casa del expresidente Salvador Allende se vio obstaculizada por la ausencia de funcionarios del Ministerio de Bienes Nacionales, lo que generó críticas y amenazas de sanciones."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.16s
- **Tokens prompt:** 2364.0
- **Tokens respuesta:** 662.0
- **Total tokens:** 3026.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "Funcionarios de BBNN no se presentan en comisión investigadora por fallida compra de casa de Allende",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [
                "Chile"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "corrupción",
                "investigación"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Presidente de la comisión, Andrés Longton, enviará antecedentes a Contraloría por inasistencia de funcionarios de Bienes Nacionales",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [
                "Chile"
            ],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "corrupción",
                "Contraloría"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Diputada Paula Labra critica duramente a funcionarios ausentes en comisión investigadora",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [
                "Chile"
            ],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "corrupción",
                "investigación"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Se enviará cuestionario al Presidente Gabriel Boric",
            "tipo_hecho": "ANUNCIO",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "CL"
            ],
            "ubicaciones_especificas": [
                "Chile"
            ],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "presidente",
                "investigación"
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
- **Tiempo:** 0m 1.23s
- **Tokens prompt:** 1697.0
- **Tokens respuesta:** 382.0
- **Total tokens:** 2079.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Andrés Longton",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Paula Labra",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Francisco Figueroa",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Salvador Allende",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Gabriel Boric",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Manuel Monsalve",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Macarena Díez",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Marcela Sandoval",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Bienes Nacionales",
            "tipo": "ORGANIZACION",
            "alias": [
                "BB.NN"
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
            "alias": []
        },
        {
            "nombre": "Comisión Investigadora",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Elecciones Generales España 2023",
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
- **Tiempo:** 0m 1.52s
- **Tokens prompt:** 1609.0
- **Tokens respuesta:** 307.0
- **Total tokens:** 1916.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "Los funcionarios citados que participaron en esta operación no tenían ninguna excusa, porque no pueden andar guiados, coachings o dirigidos por otra persona",
            "emisor_nombre": "Andrés Longton",
            "contexto": "Argumento del diputado Longton sobre la ausencia de los funcionarios de Bienes Nacionales",
            "fecha_cita": null
        },
        {
            "cita": "esto no es una citación institucional. Ya no estamos en el jardín infantil y no se necesita la supervisión del ministro que tenía, por supuesto, una excusa muy atendible",
            "emisor_nombre": "Paula Labra",
            "contexto": "Crítica de la diputada Labra a los funcionarios ausentes",
            "fecha_cita": null
        },
        {
            "cita": "no teniendo la obligación, manifestó su disposición. Lo mismo la exministra Marcela Sandoval, que está invitada y ya confirmó para el próximo día lunes",
            "emisor_nombre": "Andrés Longton",
            "contexto": "Comentario del diputado Longton sobre la confirmación de Macarena Díez y Marcela Sandoval para la próxima sesión",
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
- **Tiempo:** 0m 0.89s
- **Tokens prompt:** 2128.0
- **Tokens respuesta:** 334.0
- **Total tokens:** 2462.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Número de funcionarios de Bienes Nacionales ausentes en la comisión investigadora",
            "categoria": "demográfico",
            "valor_numerico": 1,
            "unidad": "personas",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de funcionarios de Bienes Nacionales que participaron en la operación",
            "categoria": "demográfico",
            "valor_numerico": 1,
            "unidad": "personas",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de próximas sesiones de la comisión investigadora",
            "categoria": "otro",
            "valor_numerico": 1,
            "unidad": "sesiones",
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
