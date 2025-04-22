# Evaluación Artículo: test_072

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://rpp.pe/politica/elecciones/partidos-que-quedaron-fuera-de-las-elecciones-generales-aun-podrian-participar-en-las-regionales-y-municipales-2026-noticia-1628462           |
| **Título**     | Partidos que quedaron fuera de las Elecciones Generales aún podrían participar en las Regionales y Municipales 2026 | RPP Noticias       |
| **Medio**      | None         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T16:37:09-05:00 |
| **Recopilado** | 2025-04-21T00:44:22.885935+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
El presidente del JNE, Roberto Burneo, señaló que aún no están truncadas las posibilidades de estas agrupaciones políticas si cumplen con todos los requisitos de ley.
Del total de partidos políticos con intenciones de participar de las Elecciones Generales 2026, 43 cumplieron con todos los requisitos exigidos por ley al 12 de abril y finalmente estarán aptos para competir en los comicios.
Otras 29 agrupaciones aún figuran en proceso de inscripción en el Registro de Organizaciones Políticas (ROP) del Jurado Nacional de Elecciones (JNE) como son Resurgimiento Unido Nacional, Unidad Popular y Adelante Pueblo Unido, entre otros. La pregunta que surge es si las aspiraciones de inscripción de estos partidos quedaron truncadas o no. Al respecto, Roberto Burneo, presidente del JNE precisó a El Poder en tus Manos de RPP:
“El proceso para ellos no ha quedado trunco, sigue en su curso. En los próximos días o semanas van a poder o no lograr su inscripción en función del cumplimiento de los requisitos y resolver los cuestionamientos que, tengo entendido, están en proceso. Si logran inscribirse antes de octubre, que es la probable fecha de convocatoria del proceso de Elecciones Regionales y Municipales, podrán participar en esos mismos con todas las de la ley”, afirmó el magistrado.
Te recomendamos
Con este escenario, las Elecciones Regionales y Municipales de octubre de 2026 se tornarán mucho más complejas según dijo Roberto Burneo, ya que el universo de partidos y movimientos con posibilidad de competir se amplía.
“Si estos 29 partidos lograran su inscripción, se suman a los 43 que ya están inscritos y a los 98 movimientos regionales que ya cuentan con inscripción Por lo tanto, las elecciones regionales y municipales sí van a ser complejas. Si las elecciones generales de abril del próximo año son complejas, las que se nos vienen en octubre van a hacer de una complejidad aún mayor”, aseguró.
JNE pedirá presupuesto adicional
Por otro lado, Roberto Burneo señaló que el sistema electoral ha sustentado y solicitado al Ejecutivo los recursos necesarios para llevar adelante los procesos electorales hacia el 2026. Aseguró que han recibido una primera partida de 500 millones de soles, pero que será necesario solicitar un adicional, para implementar por ejemplo ley del recuento de votos, como la implementación del voto digital, leyes aprobadas en el Congreso.
"Estas nuevas disposiciones que se han emitido sí generan impacto en cuanto a la necesidad de mayores recursos. De por sí, el pedido inicial [800 millones] tampoco lo dieron completo, pero el compromiso que tiene el Ejecutivo y el Ministerio de Economía es que, en la medida que vayamos ejecutando el presupuesto, ellos nos van a seguir canalizando los recursos", comentó.
Comparte esta noticia
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 1.03s | 1405.0 | 0.10 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 1.88s | 3317.0 | 0.43 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 0.96s | 1986.0 | 0.21 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 1.69s | 1916.0 | 0.24 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 1.00s | 2546.0 | 0.23 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.03s
- **Tokens prompt:** 1273.0
- **Tokens respuesta:** 132.0
- **Total tokens:** 1405.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "Relevancia media debido a la información sobre la inscripción de partidos políticos en elecciones regionales y municipales",
    "categorias_asignadas": [
        "Elecciones",
        "Política Nacional"
    ],
    "explicacion_concisa": "El presidente del JNE, Roberto Burneo, explica que partidos que no participaron en las Elecciones Generales 2026 pueden inscribirse en las Regionales y Municipales 2026, lo que podría hacer que las elecciones sean más complejas."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.88s
- **Tokens prompt:** 2314.0
- **Tokens respuesta:** 1003.0
- **Total tokens:** 3317.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "El presidente del JNE, Roberto Burneo, señaló que aún no están truncadas las posibilidades de las agrupaciones políticas si cumplen con todos los requisitos de ley.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "PE"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "partidos políticos",
                "JNE"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "43 partidos políticos cumplieron con todos los requisitos exigidos por ley al 12 de abril y finalmente estarán aptos para competir en los comicios.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-12",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "PE"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "partidos políticos",
                "Elecciones Generales"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "29 agrupaciones políticas aún figuran en proceso de inscripción en el Registro de Organizaciones Políticas (ROP) del Jurado Nacional de Elecciones (JNE).",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "PE"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "partidos políticos",
                "JNE"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El proceso para inscribirse en el Registro de Organizaciones Políticas (ROP) del Jurado Nacional de Elecciones (JNE) sigue en curso.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "PE"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "partidos políticos",
                "JNE"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Las Elecciones Regionales y Municipales de octubre de 2026 se tornarán mucho más complejas según dijo Roberto Burneo.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "PE"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "Elecciones Regionales y Municipales"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El sistema electoral ha sustentado y solicitado al Ejecutivo los recursos necesarios para llevar adelante los procesos electorales hacia el 2026.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "PE"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "política",
                "sistema electoral",
                "Ejecutivo"
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
- **Tiempo:** 0m 0.96s
- **Tokens prompt:** 1639.0
- **Tokens respuesta:** 347.0
- **Total tokens:** 1986.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Roberto Burneo",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "JNE",
            "tipo": "INSTITUCION",
            "alias": [
                "Jurado Nacional de Elecciones"
            ]
        },
        {
            "nombre": "Resurgimiento Unido Nacional",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Unidad Popular",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Adelante Pueblo Unido",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Elecciones Generales 2026",
            "tipo": "EVENTO",
            "alias": []
        },
        {
            "nombre": "Elecciones Regionales y Municipales 2026",
            "tipo": "EVENTO",
            "alias": []
        },
        {
            "nombre": "Congreso",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Ministerio de Economía",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "RPP",
            "tipo": "ORGANIZACION",
            "alias": [
                "Radio Programas del Perú"
            ]
        },
        {
            "nombre": "El Poder en tus Manos",
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
- **Tiempo:** 0m 1.69s
- **Tokens prompt:** 1551.0
- **Tokens respuesta:** 365.0
- **Total tokens:** 1916.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "El proceso para ellos no ha quedado trunco, sigue en su curso. En los próximos días o semanas van a poder o no lograr su inscripción en función del cumplimiento de los requisitos y resolver los cuestionamientos que, tengo entendido, están en proceso.",
            "emisor_nombre": "Roberto Burneo",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "Si estos 29 partidos lograran su inscripción, se suman a los 43 que ya están inscritos y a los 98 movimientos regionales que ya cuentan con inscripción Por lo tanto, las elecciones regionales y municipales sí van a ser complejas. Si las elecciones generales de abril del próximo año son complejas, las que se nos vienen en octubre van a hacer de una complejidad aún mayor",
            "emisor_nombre": "Roberto Burneo",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "Estas nuevas disposiciones que se han emitido sí generan impacto en cuanto a la necesidad de mayores recursos. De por sí, el pedido inicial [800 millones] tampoco lo dieron completo, pero el compromiso que tiene el Ejecutivo y el Ministerio de Economía es que, en la medida que vayamos ejecutando el presupuesto, ellos nos van a seguir canalizando los recursos",
            "emisor_nombre": "Roberto Burneo",
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
- **Tiempo:** 0m 1.00s
- **Tokens prompt:** 2070.0
- **Tokens respuesta:** 476.0
- **Total tokens:** 2546.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Número de partidos políticos con intenciones de participar de las Elecciones Generales 2026",
            "categoria": "electoral",
            "valor_numerico": 43,
            "unidad": "partidos",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Número de agrupaciones políticas en proceso de inscripción en el Registro de Organizaciones Políticas (ROP) del Jurado Nacional de Elecciones (JNE)",
            "categoria": "electoral",
            "valor_numerico": 29,
            "unidad": "partidos",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Presupuesto solicitado por el JNE para llevar adelante los procesos electorales hacia el 2026",
            "categoria": "presupuestario",
            "valor_numerico": 800000000,
            "unidad": "soles",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Presupuesto inicial recibido por el JNE",
            "categoria": "presupuestario",
            "valor_numerico": 500000000,
            "unidad": "soles",
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
