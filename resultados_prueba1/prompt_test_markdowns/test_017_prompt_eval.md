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
| relevancia | ✅ | `llama3-8b-8192` | 0m 0.50s | 1400.0 | 0.10 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 1.25s | 2976.0 | 0.35 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 0.62s | 1742.0 | 0.15 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 0.86s | 1686.0 | 0.22 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 0.88s | 2331.0 | 0.19 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.50s
- **Tokens prompt:** 1275.0
- **Tokens respuesta:** 125.0
- **Total tokens:** 1400.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 8,
    "justificacion_relevancia": "La alianza entre Tuto y Demócratas y FRI puede tener impacto en la política boliviana y electoral",
    "categorias_asignadas": [
        "Política Nacional",
        "Elecciones"
    ],
    "explicacion_concisa": "El expresidente boliviano Tuto Quiroga firma alianza con Demócratas y FRI y presentará plan de gobierno, incluyendo autonomía total y descentralización de educación, salud y seguridad"
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.25s
- **Tokens prompt:** 2198.0
- **Tokens respuesta:** 778.0
- **Total tokens:** 2976.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "Tuto firma alianza con FRI y Demócratas; la presentará ante el TSE",
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
            "contenido": "Quiroga habla sobre plan de Gobierno y autonomía total",
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
            "contenido": "Quiroga propone que candidatos presenten declaración jurada anticipada",
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
            "contenido": "Quiroga propone debates públicos entre candidatos",
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
                "debates"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La alianza debe presentarse ante el TSE durante esta semana",
            "tipo_hecho": "ANUNCIO",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 5,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "alianza",
                "TSE"
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
- **Tiempo:** 0m 0.62s
- **Tokens prompt:** 1509.0
- **Tokens respuesta:** 233.0
- **Total tokens:** 1742.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Jorge Quiroga",
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
            "nombre": "Debate público",
            "tipo": "CONCEPTO",
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
- **Tiempo:** 0m 0.86s
- **Tokens prompt:** 1377.0
- **Tokens respuesta:** 309.0
- **Total tokens:** 1686.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "“Lo dijimos una y otra vez, la autonomía solo va a funcionar si empieza a implementarse de forma total; es con salud, educación y seguridad descentralizadas (y entregadas) a las regiones y a los municipios, para que tú sepas quién le brinda salud, quién educa a tus hijos(...) que no adoctrinen, que eduquen a los niños”",
            "emisor_nombre": "Quiroga",
            "contexto": "En su discurso",
            "fecha_cita": null
        },
        {
            "cita": "“yo no soy millonario, pero soy rico, tengo tres títulos universitarios, esa es mi riqueza”",
            "emisor_nombre": "Quiroga",
            "contexto": "En su discurso",
            "fecha_cita": null
        },
        {
            "cita": "“solo un debate público de todos los candidatos permitirá a la población ver y escuchar las propuestas que tienen para el caso de que sean gobierno, y por eso insistirá en que se realicen esos encuentros públicos entre postulantes a la presidencia”",
            "emisor_nombre": "Quiroga",
            "contexto": "En su discurso",
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
- **Tiempo:** 0m 0.88s
- **Tokens prompt:** 1964.0
- **Tokens respuesta:** 367.0
- **Total tokens:** 2331.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Autonomía total en educación, salud y seguridad",
            "categoria": "presupuestario",
            "valor_numerico": null,
            "unidad": null,
            "ambito_geografico": [
                "Bolivia"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": "Descentralización de responsabilidades a las regiones y municipios"
        },
        {
            "indicador": "Declaración jurada de bienes y rentas anticipada",
            "categoria": "electoral",
            "valor_numerico": null,
            "unidad": null,
            "ambito_geografico": [
                "Bolivia"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": "Requisito para los candidatos a la presidencia"
        },
        {
            "indicador": "Debates públicos entre candidatos",
            "categoria": "electoral",
            "valor_numerico": null,
            "unidad": null,
            "ambito_geografico": [
                "Bolivia"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": "Requisito para la población ver y escuchar las propuestas de los candidatos"
        }
    ]
}
```
</details>
