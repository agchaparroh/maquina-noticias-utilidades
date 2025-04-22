# Evaluación Artículo: test_017

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://eldeber.com.bo/pais/tuto-firma-su-alianza-con-el-fri-y-democratas-la-presentara-ante-el-tse_510611/           |
| **Título**     | Tuto firma su alianza con el FRI y Demócratas; la presentará ante el TSE       |
| **Medio**      | El Deber         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T23:27:07+00:00 |
| **Recopilado** | 2025-04-21T00:42:44.634405+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Tuto firma su alianza con el FRI y Demócratas; la presentará ante el TSE
El expresidente aprovechó la oportunidad para hablar sobre su plan de Gobierno
La firma de la alianza Libre entre Demócratas y el Frente Revolucionario de Izquierda (FRI) se produjo la noche de este lunes 14, en la ciudad de Santa Cruz, donde Jorge, 'Tuto', Quiroga esbozó parte de su plan de Gobierno; adelantó que la autonomía será total, pasando las responsabilidades de educación, salud y seguridad a manos de las gobernaciones y municipios.
“Lo dijimos una y otra vez, la autonomía solo va a funcionar si empieza a implementarse de forma total; es con salud, educación y seguridad descentralizadas (y entregadas) a las regiones y a los municipios, para que tú sepas quién le brinda salud, quién educa a tus hijos(...) que no adoctrinen, que eduquen a los niños”, manifestó Quiroga.
De ese modo, quedó plasmada la alianza que debe presentarse durante esta semana ante el Tribunal Supremo Electoral (TSE), de acuerdo con el Calendario Electoral vigente. Según esta norma las alianzas deben presentarse entre el 14 de abril y el viernes 18 de abril; aunque ese día es feriado en Bolivia, las autoridades electorales informaron que habrá personal recibiendo las alianzas.
En su discurso Quiroga también planteó que después de presentar las candidaturas oficialmente todos los candidatos realicen su declaración jurada de bienes y rentas, de forma anticipada para saber qué patrimonio tienen antes de ser candidatos; “yo no soy millonario, pero soy rico, tengo tres títulos universitarios, esa es mi riqueza” matizó el exmandatario boliviano.
No obstante, la ley 2027 Estatuto del Funcionario Público establece la presentación de declaración jurada solo para los funcionarios públicos, no regula a las personas particulares, tendría que modificarse esta norma para que los candidatos presenten una declaración jurada anticipada.
Quiroga dijo también que solo un debate público de todos los candidatos permitirá a la población ver y escuchar las propuestas que tienen para el caso de que sean gobierno, y por eso insistirá en que se realicen esos encuentros públicos entre postulantes a la presidencia.
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 0.51s | 1398.0 | 0.10 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 1.99s | 3277.0 | 0.51 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 1.05s | 1768.0 | 0.18 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 0.74s | 1742.0 | 0.23 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 1.36s | 2135.0 | 0.11 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.51s
- **Tokens prompt:** 1275.0
- **Tokens respuesta:** 123.0
- **Total tokens:** 1398.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 8,
    "justificacion_relevancia": "La alianza política y el plan de gobierno de Tuto Quiroga tienen impacto en la política boliviana y la sociedad",
    "categorias_asignadas": [
        "Política Nacional",
        "Elecciones"
    ],
    "explicacion_concisa": "El expresidente boliviano Tuto Quiroga firma alianza con el FRI y Demócratas y presenta plan de gobierno, incluyendo autonomía total y descentralización de responsabilidades"
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.99s
- **Tokens prompt:** 2167.0
- **Tokens respuesta:** 1110.0
- **Total tokens:** 3277.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "Tuto firma alianza con el FRI y Demócratas; la presentará ante el TSE",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Santa Cruz"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "alianza",
                "gobierno"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Quiroga habla sobre su plan de Gobierno",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Santa Cruz"
            ],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "gobierno",
                "plan"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La autonomía será total, pasando responsabilidades a las gobernaciones y municipios",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Santa Cruz"
            ],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "gobierno",
                "autonomía"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La alianza debe presentarse ante el TSE durante esta semana",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "alianza",
                "TSE"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Quiroga plantea que los candidatos realicen su declaración jurada de bienes y rentas anticipada",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Santa Cruz"
            ],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "candidatos",
                "declaración jurada"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La ley 2027 Estatuto del Funcionario Público no regula la presentación de declaración jurada para los particulares",
            "tipo_hecho": "CONCEPTO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "dia",
            "paises": [],
            "ubicaciones_especificas": [],
            "importancia": 5,
            "confiabilidad": 4,
            "etiquetas": [
                "política",
                "ley",
                "declaración jurada"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Quiroga insiste en que se realicen debates públicos entre postulantes a la presidencia",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [
                "Santa Cruz"
            ],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "debates",
                "presidencia"
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
- **Tiempo:** 0m 1.05s
- **Tokens prompt:** 1500.0
- **Tokens respuesta:** 268.0
- **Total tokens:** 1768.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Tuto Quiroga",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Frente Revolucionario de Izquierda (FRI)",
            "tipo": "ORGANIZACION",
            "alias": [
                "FRI"
            ]
        },
        {
            "nombre": "Demócratas",
            "tipo": "ORGANIZACION",
            "alias": [
                "Demócratas"
            ]
        },
        {
            "nombre": "Tribunal Supremo Electoral (TSE)",
            "tipo": "INSTITUCION",
            "alias": [
                "TSE"
            ]
        },
        {
            "nombre": "Santa Cruz",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Bolivia",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Ley 2027 Estatuto del Funcionario Público",
            "tipo": "NORMATIVA",
            "alias": []
        },
        {
            "nombre": "Calendario Electoral",
            "tipo": "NORMATIVA",
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
- **Tiempo:** 0m 0.74s
- **Tokens prompt:** 1412.0
- **Tokens respuesta:** 330.0
- **Total tokens:** 1742.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "Lo dijimos una y otra vez, la autonomía solo va a funcionar si empieza a implementarse de forma total; es con salud, educación y seguridad descentralizadas (y entregadas) a las regiones y a los municipios, para que tú sepas quién le brinda salud, quién educa a tus hijos(...) que no adoctrinen, que eduquen a los niños",
            "emisor_nombre": "Quiroga",
            "contexto": "manifestó Quiroga",
            "fecha_cita": null
        },
        {
            "cita": "yo no soy millonario, pero soy rico, tengo tres títulos universitarios, esa es mi riqueza",
            "emisor_nombre": "Quiroga",
            "contexto": "matizó el exmandatario boliviano",
            "fecha_cita": null
        },
        {
            "cita": "solo un debate público de todos los candidatos permitirá a la población ver y escuchar las propuestas que tienen para el caso de que sean gobierno, y por eso insistirá en que se realicen esos encuentros públicos entre postulantes a la presidencia",
            "emisor_nombre": "Quiroga",
            "contexto": "insistirá en que se realicen esos encuentros públicos entre postulantes a la presidencia",
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
- **Tiempo:** 0m 1.36s
- **Tokens prompt:** 1931.0
- **Tokens respuesta:** 204.0
- **Total tokens:** 2135.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Título universitarios",
            "categoria": "demográfico",
            "valor_numerico": 3,
            "unidad": "títulos",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Patrimonio",
            "categoria": "económico",
            "valor_numerico": null,
            "unidad": "USD",
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
