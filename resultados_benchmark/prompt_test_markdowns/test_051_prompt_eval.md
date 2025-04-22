# Evaluación Artículo: test_051

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.laprensa.com.ar/Una-familia-tipo-de-CABA-necesito-en-marzo-ingresos-por-mas-de-1147000-para-no-ser-pobre-558522.note.aspx           |
| **Título**     | Una familia tipo de CABA necesitó en marzo ingresos por más de $1.147.000 para no ser pobre       |
| **Medio**      | None         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-21T00:43:40.322753+00:00 |
| **Recopilado** | 2025-04-21T00:43:40.322777+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Una familia tipo de CABA necesitó en marzo ingresos por más de $1.147.000 para no ser pobre
Las familias que residen en la Ciudad Autónoma de Buenos Aires (CABA) necesitaron durante marzo ingresos de al menos $1.147.602 para no ser pobres y de aunque sea $1.804.267 para ser consideradas de clase media, de acuerdo a lo informado por el Instituto de Estadísticas y Censos porteño (IDECBA).
El comportamiento de las canastas que se utilizan para determinar la línea de la pobreza e indigencia en la Ciudad, subieron hasta 7,22%, es decir que avanzaron por encima de la inflación en el tercer mes del año, que en el territorio porteño escaló hasta el 3,2%.
La medición se realiza considerando como una familia tipo a aquella compuesta por dos adultos y dos menores, que en el mes pasado necesitó ingresos por lo menos de $1.804.267 para ser de clase media, de al menos $1.147.602 para no ser pobre y aunque sea de $621.772 para no ser catalogada como indigente.
La Canasta Básica Alimentaria (CBA), que define el umbral de indigencia, trepó 7,22% en marzo, mientras que la Canasta Básica Total (CBT), que mide la pobreza, subió 5,32% en el tercer mes del 2025. De esta manera, en el mes pasado la línea de pobreza creció un 5,36% y la de indigencia se elevó un 6,91%.
El organismo estadístico porteño precisó que en relación con un año atrás, la línea de pobreza pasó de estar en $766.146 durante marzo de 2024 a $1.147.602 en el mismo mes del actual calendario.
En tanto que la línea de indigencia avanzó de $442.239 a $621.772.
ESTRATOS SEGÚN INGRESOS
- En situación de indigencia: hogares cuyo ingreso total mensual no alcanza para cubrir la Canasta Básica Alimentaria (CBA - Línea de indigencia). Tienen ingresos totales de hasta $621.772,34.
- En situación de pobreza no indigente: hogares cuyo ingreso total mensual no alcanza para cubrir la Canasta Básica Total (CBT - Línea de pobreza) pero permite al menos adquirir la CBA. Cuentan con un total de ingresos entre $621.772,35 y $1.147.601,97.
- No pobres vulnerables: hogares cuyo ingreso total mensual es de al menos la CBT y no alcanza la Canasta Total (CT) del Sistema de Canastas de Consumo. Registran ingresos totales entre $1.147.601,98 y $1.443.413,59.
- Sector medio frágil: hogares cuyo ingreso total mensual es de al menos la Canasta Total y no alcanza 1,25 veces la CT del Sistema de Canastas de Consumo. Tienen ingresos mensuales entre $1.443.413,60 y $1.804.266,99.
- Sector medio "clase media": hogares cuyo ingreso total mensual es de al menos 1,25 veces la CT y no alcanza cuatro veces la CT del Sistema de Canastas de Consumo. Ganan desde $1.804.266,00 hasta $5.773.654,39 al mes.
- Sector acomodado: hogares cuyo ingreso mensual supera cuatro CT del Sistema de Canastas de Consumo, con ingresos al mes de $5.773.654,40 en adelante.
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 0.97s | 1486.0 | 0.09 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 2.47s | 3301.0 | 0.34 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 3.60s | 1997.0 | 0.11 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 3.26s | 2281.0 | 0.34 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 2.84s | 2959.0 | 0.33 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.97s
- **Tokens prompt:** 1359.0
- **Tokens respuesta:** 127.0
- **Total tokens:** 1486.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "La información sobre la pobreza y la indigencia en CABA es relevante para la economía y la sociedad hispana.",
    "categorias_asignadas": [
        "Economía",
        "Sociedad/Derechos"
    ],
    "explicacion_concisa": "El artículo informa sobre la cantidad de dinero que una familia tipo en CABA necesita para no ser pobre o indigente, según el Instituto de Estadísticas y Censos porteño (IDECBA)."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 2.47s
- **Tokens prompt:** 2466.0
- **Tokens respuesta:** 835.0
- **Total tokens:** 3301.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "La familia tipo de CABA necesitó en marzo ingresos por más de $1.147.000 para no ser pobre.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-01T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "mes",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "economía",
                "pobreza",
                "ingresos"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La Canasta Básica Alimentaria (CBA) trepó 7,22% en marzo, mientras que la Canasta Básica Total (CBT) subió 5,32% en el tercer mes del 2025.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-01T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "mes",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "economía",
                "inflación",
                "Canasta Básica"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La línea de pobreza creció un 5,36% y la de indigencia se elevó un 6,91% en el mes pasado.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-01T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "mes",
            "paises": [
                "AR"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "economía",
                "pobreza",
                "indigencia"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La Canasta Básica Alimentaria (CBA) define el umbral de indigencia.",
            "tipo_hecho": "CONCEPTO",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "n/a",
            "paises": [],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "economía",
                "pobreza",
                "Canasta Básica"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La Canasta Básica Total (CBT) mide la pobreza.",
            "tipo_hecho": "CONCEPTO",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "n/a",
            "paises": [],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "economía",
                "pobreza",
                "Canasta Básica"
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
- **Tiempo:** 0m 3.60s
- **Tokens prompt:** 1796.0
- **Tokens respuesta:** 201.0
- **Total tokens:** 1997.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Ciudad Autónoma de Buenos Aires (CABA)",
            "tipo": "LUGAR",
            "alias": [
                "CABA"
            ]
        },
        {
            "nombre": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "tipo": "INSTITUCION",
            "alias": [
                "IDECBA"
            ]
        },
        {
            "nombre": "Canasta Básica Alimentaria (CBA)",
            "tipo": "CONCEPTO",
            "alias": [
                "CBA"
            ]
        },
        {
            "nombre": "Canasta Básica Total (CBT)",
            "tipo": "CONCEPTO",
            "alias": [
                "CBT"
            ]
        },
        {
            "nombre": "Sistema de Canastas de Consumo",
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
- **Tiempo:** 0m 3.26s
- **Tokens prompt:** 1708.0
- **Tokens respuesta:** 573.0
- **Total tokens:** 2281.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "hogares cuyo ingreso total mensual no alcanza para cubrir la Canasta Básica Alimentaria (CBA - Línea de indigencia). Tienen ingresos totales de hasta $621.772,34.",
            "emisor_nombre": "IDECBA",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso total mensual no alcanza para cubrir la Canasta Básica Total (CBT - Línea de pobreza) pero permite al menos adquirir la CBA. Cuentan con un total de ingresos entre $621.772,35 y $1.147.601,97.",
            "emisor_nombre": "IDECBA",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso total mensual es de al menos la CBT y no alcanza la Canasta Total (CT) del Sistema de Canastas de Consumo. Registran ingresos totales entre $1.147.601,98 y $1.443.413,59.",
            "emisor_nombre": "IDECBA",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso total mensual es de al menos la Canasta Total y no alcanza 1,25 veces la CT del Sistema de Canastas de Consumo. Tienen ingresos mensuales entre $1.443.413,60 y $1.804.266,99.",
            "emisor_nombre": "IDECBA",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso total mensual es de al menos 1,25 veces la CT y no alcanza cuatro veces la CT del Sistema de Canastas de Consumo. Ganan desde $1.804.266,00 hasta $5.773.654,39 al mes.",
            "emisor_nombre": "IDECBA",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "hogares cuyo ingreso mensual supera cuatro CT del Sistema de Canastas de Consumo, con ingresos al mes de $5.773.654,40 en adelante.",
            "emisor_nombre": "IDECBA",
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
- **Tiempo:** 0m 2.84s
- **Tokens prompt:** 2227.0
- **Tokens respuesta:** 732.0
- **Total tokens:** 2959.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Línea de indigencia",
            "categoria": "social",
            "valor_numerico": 621772.34,
            "unidad": "ARS",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": "puntual",
            "fuente_especifica": "IDECBA",
            "notas_contexto": null
        },
        {
            "indicador": "Línea de pobreza",
            "categoria": "social",
            "valor_numerico": 1147602.0,
            "unidad": "ARS",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": "puntual",
            "fuente_especifica": "IDECBA",
            "notas_contexto": null
        },
        {
            "indicador": "Canasta Básica Alimentaria (CBA)",
            "categoria": "social",
            "valor_numerico": 7.22,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": "puntual",
            "fuente_especifica": "IDECBA",
            "notas_contexto": null
        },
        {
            "indicador": "Canasta Básica Total (CBT)",
            "categoria": "social",
            "valor_numerico": 5.32,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": "puntual",
            "fuente_especifica": "IDECBA",
            "notas_contexto": null
        },
        {
            "indicador": "Línea de pobreza crecimiento anual",
            "categoria": "social",
            "valor_numerico": 381456.0,
            "unidad": "ARS",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": "2024-03-01",
            "periodo_referencia_fin": "2025-03-31",
            "tipo_periodo": "anual",
            "fuente_especifica": "IDECBA",
            "notas_contexto": null
        },
        {
            "indicador": "Línea de indigencia crecimiento anual",
            "categoria": "social",
            "valor_numerico": 179533.0,
            "unidad": "ARS",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": "2024-03-01",
            "periodo_referencia_fin": "2025-03-31",
            "tipo_periodo": "anual",
            "fuente_especifica": "IDECBA",
            "notas_contexto": null
        }
    ]
}
```
</details>
