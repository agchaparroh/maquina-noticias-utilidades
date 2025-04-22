# Evaluación Artículo: test_051
**Modelo Probado:** `llama3-8b-8192`

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

<details open>
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

## Resultados de las Tareas (llama3-8b-8192)

### Tarea: relevancia

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "Relevancia media debido a la información sobre la pobreza y la indigencia en la Ciudad Autónoma de Buenos Aires",
    "categorias_asignadas": [
        "Economía",
        "Sociedad/Derechos"
    ],
    "explicacion_concisa": "El artículo informa sobre la cantidad de dinero que una familia tipo en CABA necesita para no ser pobre o indigente, según el Instituto de Estadísticas y Censos porteño (IDECBA)."
}
```
</details>


### Tarea: extraccion_hechos

❌ **Estado:** Fallo (Error API)

   **Mensaje Error:** `API_Error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama3-8b-8192` in organization `org_01jsay2bafeeht06zsq8qv9mct` service tier `on_demand` on tokens per minute (TPM): Limit 100000, Used 104203, Requested 2058. Please try again in 3.757s. Need more tokens? Visit https://groq.com/self-serve-support/ to request higher limits.', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}`


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

_(Respuesta no es JSON válido o estructura incorrecta, mostrando raw):_
```
Error: No content received or generated
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
            "nombre": "Ciudad Autónoma de Buenos Aires",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Instituto de Estadísticas y Censos porteño",
            "tipo": "INSTITUCION",
            "alias": [
                "IDECBA"
            ]
        },
        {
            "nombre": "Canasta Básica Alimentaria",
            "tipo": "CONCEPTO",
            "alias": [
                "CBA"
            ]
        },
        {
            "nombre": "Canasta Básica Total",
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


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "Las familias que residen en la Ciudad Autónoma de Buenos Aires (CABA) necesitaron durante marzo ingresos de al menos $1.147.602 para no ser pobres y de aunque sea $1.804.267 para ser consideradas de clase media, de acuerdo a lo informado por el Instituto de Estadísticas y Censos porteño (IDECBA).",
            "emisor_nombre": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "contexto": "Se refiere a la cantidad de dinero que una familia necesita para no ser pobre o ser considerada de clase media en la Ciudad Autónoma de Buenos Aires.",
            "fecha_cita": null
        },
        {
            "cita": "La medición se realiza considerando como una familia tipo a aquella compuesta por dos adultos y dos menores, que en el mes pasado necesitó ingresos por lo menos de $1.804.267 para ser de clase media, de al menos $1.147.602 para no ser pobre y aunque sea de $621.772 para no ser catalogada como indigente.",
            "emisor_nombre": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "contexto": "Se describe el tipo de familia que se utiliza para medir la pobreza e indigencia en la Ciudad Autónoma de Buenos Aires.",
            "fecha_cita": null
        },
        {
            "cita": "La Canasta Básica Alimentaria (CBA), que define el umbral de indigencia, trepó 7,22% en marzo, mientras que la Canasta Básica Total (CBT), que mide la pobreza, subió 5,32% en el tercer mes del 2025.",
            "emisor_nombre": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "contexto": "Se informa sobre el aumento en la Canasta Básica Alimentaria y la Canasta Básica Total en marzo de 2025.",
            "fecha_cita": "2025-03-00"
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
            "indicador": "Ingresos necesarios para no ser pobres en la Ciudad Autónoma de Buenos Aires",
            "categoria": "económico",
            "valor_numerico": 1147602,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": "2025-03-01",
            "periodo_referencia_fin": "2025-03-31",
            "tipo_periodo": "mensual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos necesarios para ser consideradas de clase media en la Ciudad Autónoma de Buenos Aires",
            "categoria": "económico",
            "valor_numerico": 1804267,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": "2025-03-01",
            "periodo_referencia_fin": "2025-03-31",
            "tipo_periodo": "mensual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Incremento en la Canasta Básica Alimentaria (CBA) en la Ciudad Autónoma de Buenos Aires",
            "categoria": "económico",
            "valor_numerico": 7.22,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": "2025-03-01",
            "periodo_referencia_fin": "2025-03-31",
            "tipo_periodo": "mensual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Incremento en la Canasta Básica Total (CBT) en la Ciudad Autónoma de Buenos Aires",
            "categoria": "económico",
            "valor_numerico": 5.32,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": "2025-03-01",
            "periodo_referencia_fin": "2025-03-31",
            "tipo_periodo": "mensual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Incremento en la línea de pobreza en la Ciudad Autónoma de Buenos Aires",
            "categoria": "económico",
            "valor_numerico": 5.36,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": "2025-03-01",
            "periodo_referencia_fin": "2025-03-31",
            "tipo_periodo": "mensual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Incremento en la línea de indigencia en la Ciudad Autónoma de Buenos Aires",
            "categoria": "económico",
            "valor_numerico": 6.91,
            "unidad": "%",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": "2025-03-01",
            "periodo_referencia_fin": "2025-03-31",
            "tipo_periodo": "mensual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        },
        {
            "indicador": "Ingresos necesarios para no ser indigentes en la Ciudad Autónoma de Buenos Aires",
            "categoria": "económico",
            "valor_numerico": 621772,
            "unidad": "USD",
            "ambito_geografico": [
                "Ciudad Autónoma de Buenos Aires"
            ],
            "periodo_referencia_inicio": "2025-03-01",
            "periodo_referencia_fin": "2025-03-31",
            "tipo_periodo": "mensual",
            "fuente_especifica": "Instituto de Estadísticas y Censos porteño (IDECBA)",
            "notas_contexto": null
        }
    ]
}
```
</details>
