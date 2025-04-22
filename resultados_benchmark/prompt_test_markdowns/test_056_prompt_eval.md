# Evaluación Artículo: test_056

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.diariolibre.com/politica/gobierno/2025/04/14/el-gobierno-brindara-apoyo-a-victimas-en-discoteca-jet-set/3073906           |
| **Título**     | "A nadie vamos a dejar solo", dice Abinader a víctimas del Jet Set       |
| **Medio**      | Diario Libre         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T00:00:00+00:00 |
| **Recopilado** | 2025-04-21T00:43:44.396316+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
"A nadie vamos a dejar solo", dice Abinader a víctimas del Jet Set
El mandatario informó que el programa Supérate trabaja en la identificación de todas las víctimas y sus familiares para darles seguimiento en su salud mental y otras ayudas que ameriten
El presidente Luis Abinader aseguró este lunes que las víctimas de la tragedia en la discoteca Jet Set, la cual ha cobrado más de 231 vidas, recibirán acompañamiento por parte del Gobierno en el aspecto de salud mental y en otras áreas que ameriten.
"A nadie vamos a dejar solo. El Gobierno va a estar con ellos", tranquilizó el mandatario al ser cuestionado sobre las iniciativas para ayudar a los afectados por la tragedia.
Dijo que Supérate es el organismo del Gobierno que les dará el seguimiento correspondiente.
Indicó que ha dado instrucciones para brindar un seguimiento integral, tanto para la salud mental de las víctimas como de los rescatistas. "Incluso los rescatistas también, porque su impacto fue muy fuerte", añadió.
Durante LA Semanal con la Prensa, el presidente explicó que se está trabajando en la identificación de todas las víctimas y sus familiares. Para ello, ha instruido al programa Supérate a que realice este proceso y se encargue de darles seguimiento y acompañamiento, tanto en su salud física como mental.
- En el caso de los huérfanos en situación de vulnerabilidad, Abinader sostuvo que también recibirán apoyo, incluyendo asistencia económica.
Tragedia en Jet Set
En la madrugada del martes 8 de abril, se desplomó el techo de la discoteca Jet Set sobre centenares de personas, mientras el merenguero Rubby Pérez amenizaba una fiesta en el lugar. El artista falleció en el siniestro.
Según las autoridades, 221 personas murieron en el lugar, en su mayoría de forma instantánea, mientras que otras 10 fallecieron en los centros médicos a los que fueron trasladadas.
"Me cubrió con su cuerpo y por eso estoy viva": Maribel Espaillat, sobreviviente del Jet Set
Investigación en curso
El Gobierno ha solicitado una investigación independiente para esclarecer los hechos. La Oficina Nacional de Evaluación Sísmica y Vulnerabilidad de Infraestructura y Edificaciones (Onesvie), junto con el Ministerio Público, encabezan las pesquisas.
- El Ministerio Público ha abierto una investigación penal para determinar las causas del colapso. Esta tragedia ha enlutado a toda la nación, siendo considerada la mayor catástrofe civil del siglo XXI en la República Dominicana.
La investigación técnica la encabeza la Onesvie, mientras que la penal está a cargo de la Dirección de Persecución de la Procuraduría General, encabezada por el procurador adjunto Wilson Camacho, en coordinación con la Fiscalía del Distrito Nacional.
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 3.38s | 1424.0 | 0.12 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 4.28s | 2994.0 | 0.30 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 1.05s | 2017.0 | 0.23 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 1.09s | 1760.0 | 0.14 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 3.28s | 2415.0 | 0.17 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 3.38s
- **Tokens prompt:** 1274.0
- **Tokens respuesta:** 150.0
- **Total tokens:** 1424.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 7,
    "justificacion_relevancia": "El presidente Abinader anuncia apoyo al Gobierno para las víctimas y rescatistas de la tragedia en la discoteca Jet Set",
    "categorias_asignadas": [
        "Política Nacional",
        "Sociedad/Derechos"
    ],
    "explicacion_concisa": "El presidente de la República Dominicana, Luis Abinader, anuncia que el Gobierno brindará apoyo a las víctimas y rescatistas de la tragedia en la discoteca Jet Set, incluyendo ayuda psicológica y económica a los huérfanos en situación de vulnerabilidad."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 4.28s
- **Tokens prompt:** 2298.0
- **Tokens respuesta:** 696.0
- **Total tokens:** 2994.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "El presidente Luis Abinader aseguró que las víctimas de la tragedia en la discoteca Jet Set recibirán acompañamiento por parte del Gobierno en el aspecto de salud mental y en otras áreas que ameriten.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "DO"
            ],
            "ubicaciones_especificas": [
                "República Dominicana"
            ],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "gobierno",
                "tragedia",
                "Jet Set",
                "victimas"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El programa Supérate trabaja en la identificación de todas las víctimas y sus familiares para darles seguimiento en su salud mental y otras ayudas que ameriten.",
            "tipo_hecho": "ANUNCIO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "DO"
            ],
            "ubicaciones_especificas": [
                "República Dominicana"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "gobierno",
                "programa",
                "Supérate",
                "victimas"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La tragedia en la discoteca Jet Set ha cobrado más de 231 vidas.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-08",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "DO"
            ],
            "ubicaciones_especificas": [
                "República Dominicana"
            ],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "tragedia",
                "Jet Set",
                "muertes"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El Ministerio Público ha abierto una investigación penal para determinar las causas del colapso de la discoteca Jet Set.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "DO"
            ],
            "ubicaciones_especificas": [
                "República Dominicana"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "Ministerio Público",
                "investigación",
                "colapso",
                "Jet Set"
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
- **Tokens prompt:** 1635.0
- **Tokens respuesta:** 382.0
- **Total tokens:** 2017.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Luis Abinader",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Supérate",
            "tipo": "ORGANIZACION",
            "alias": [
                "Supérate"
            ]
        },
        {
            "nombre": "Jet Set",
            "tipo": "LUGAR",
            "alias": [
                "Jet Set"
            ]
        },
        {
            "nombre": "Rubén Pérez",
            "tipo": "PERSONA",
            "alias": [
                "Rubby Pérez"
            ]
        },
        {
            "nombre": "Maribel Espaillat",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Oficina Nacional de Evaluación Sísmica y Vulnerabilidad de Infraestructura y Edificaciones (Onesvie)",
            "tipo": "INSTITUCION",
            "alias": [
                "Onesvie"
            ]
        },
        {
            "nombre": "Ministerio Público",
            "tipo": "ORGANIZACION",
            "alias": [
                "Ministerio Público"
            ]
        },
        {
            "nombre": "Dirección de Persecución de la Procuraduría General",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Procuraduría General",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Fiscalía del Distrito Nacional",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "República Dominicana",
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
- **Tiempo:** 0m 1.09s
- **Tokens prompt:** 1547.0
- **Tokens respuesta:** 213.0
- **Total tokens:** 1760.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "A nadie vamos a dejar solo",
            "emisor_nombre": "Abinader",
            "contexto": "Al ser cuestionado sobre las iniciativas para ayudar a los afectados por la tragedia",
            "fecha_cita": null
        },
        {
            "cita": "El Gobierno va a estar con ellos",
            "emisor_nombre": "Abinader",
            "contexto": "Al ser cuestionado sobre las iniciativas para ayudar a los afectados por la tragedia",
            "fecha_cita": null
        },
        {
            "cita": "Incluso los rescatistas también, porque su impacto fue muy fuerte",
            "emisor_nombre": "Abinader",
            "contexto": "Al explicar que se está trabajando en la identificación de todas las víctimas y sus familiares",
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
- **Tiempo:** 0m 3.28s
- **Tokens prompt:** 2066.0
- **Tokens respuesta:** 349.0
- **Total tokens:** 2415.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Número de víctimas fatales en la tragedia en la discoteca Jet Set",
            "categoria": "social",
            "valor_numerico": 231,
            "unidad": "personas",
            "ambito_geografico": [
                "República Dominicana"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": "puntual",
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de víctimas fatales en el lugar",
            "categoria": "social",
            "valor_numerico": 221,
            "unidad": "personas",
            "ambito_geografico": [
                "República Dominicana"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": "puntual",
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de víctimas fatales en centros médicos",
            "categoria": "social",
            "valor_numerico": 10,
            "unidad": "personas",
            "ambito_geografico": [
                "República Dominicana"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": "puntual",
            "fuente_especifica": null,
            "notas_contexto": null
        }
    ]
}
```
</details>
