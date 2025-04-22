# Evaluación Artículo: test_038

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://eldeber.com.bo/pais/tuto-firma-alianza-con-democratas-y-fri_510611/           |
| **Título**     | Tuto propone autonomía total; pasar salud, educación y seguridad a las regiones       |
| **Medio**      | El Deber         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T23:27:07+00:00 |
| **Recopilado** | 2025-04-21T00:43:20.879676+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Tuto propone autonomía total; pasar salud, educación y seguridad a las regiones
La noche de este lunes 14, Tuto firmó una alianza con Demócratas y el Frente Revolucionario de Izquierda
La firma de la alianza Libre entre Demócratas y el Frente Revolucionario de Izquierda (FRI) se produjo la noche de este lunes 14, en la ciudad de Santa Cruz, donde Jorge, 'Tuto', Quiroga esbozó otra parte de su plan de Gobierno; adelantó que la autonomía será total, pasando las responsabilidades de educación, salud y seguridad a manos de las gobernaciones y municipios.
“Lo dijimos una y otra vez, la autonomía solo va a funcionar si empieza a implementarse de forma total; es con salud, educación y seguridad descentralizadas (y entregadas) a las regiones y a los municipios, para que tú sepas quién le brinda salud, quién educa a tus hijos(...) que no adoctrinen, que eduquen a los niños”, manifestó Quiroga
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
| relevancia | ✅ | `llama3-8b-8192` | 0m 0.67s | 1435.0 | 0.13 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 5.72s | 2985.0 | 0.37 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 5.05s | 1755.0 | 0.16 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 4.92s | 1733.0 | 0.22 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 3.66s | 2053.0 | 0.06 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.67s
- **Tokens prompt:** 1272.0
- **Tokens respuesta:** 163.0
- **Total tokens:** 1435.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 8,
    "justificacion_relevancia": "La propuesta de autonomía total y descentralización de responsabilidades en Bolivia es un tema relevante en la esfera política hispana.",
    "categorias_asignadas": [
        "Política Nacional",
        "Conflicto/Seguridad",
        "Justicia/Legal"
    ],
    "explicacion_concisa": "El exmandatario boliviano Tuto propone una alianza política que busca otorgar autonomía total a las regiones, transfiriendo responsabilidades en salud, educación y seguridad a las gobernaciones y municipios. La propuesta también incluye la presentación de declaraciones juradas anticipadas por los candidatos."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 5.72s
- **Tokens prompt:** 2173.0
- **Tokens respuesta:** 812.0
- **Total tokens:** 2985.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "Tuto firma alianza con Demócratas y el Frente Revolucionario de Izquierda.",
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
            "contenido": "Tuto propone autonomía total, pasando salud, educación y seguridad a las regiones.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "autonomía",
                "gobierno"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La alianza debe presentarse ante el Tribunal Supremo Electoral (TSE) durante esta semana.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "elecciones",
                "TSE"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Quiroga planteó que los candidatos realicen su declaración jurada de bienes y rentas de forma anticipada.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
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
            "contenido": "Quiroga propone que solo un debate público de todos los candidatos permitirá a la población ver y escuchar las propuestas.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "debate",
                "candidatos"
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
- **Tiempo:** 0m 5.05s
- **Tokens prompt:** 1511.0
- **Tokens respuesta:** 244.0
- **Total tokens:** 1755.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Tuto Quiroga",
            "tipo": "PERSONA",
            "alias": [
                "Tuto",
                "Quiroga"
            ]
        },
        {
            "nombre": "Demócratas",
            "tipo": "ORGANIZACION",
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
            "nombre": "Santa Cruz",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Tribunal Supremo Electoral (TSE)",
            "tipo": "INSTITUCION",
            "alias": [
                "TSE"
            ]
        },
        {
            "nombre": "Calendario Electoral",
            "tipo": "NORMATIVA",
            "alias": []
        },
        {
            "nombre": "Ley 2027 Estatuto del Funcionario Público",
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
- **Tiempo:** 0m 4.92s
- **Tokens prompt:** 1423.0
- **Tokens respuesta:** 310.0
- **Total tokens:** 1733.0


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
            "contexto": "dijo también",
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
- **Tiempo:** 0m 3.66s
- **Tokens prompt:** 1942.0
- **Tokens respuesta:** 111.0
- **Total tokens:** 2053.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Tres títulos universitarios",
            "categoria": "otro",
            "valor_numerico": 3,
            "unidad": "títulos",
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
