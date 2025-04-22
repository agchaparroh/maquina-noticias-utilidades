# Evaluación Artículo: test_054

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://eldeber.com.bo/pais/justicia-ordena-aprehension-del-ministro-edgar-montano-por-deuda-extrabajadores-de-sabsa_510601/           |
| **Título**     | Justicia ordena apremio del ministro Edgar Montaño por deuda a extrabajadores de Sabsa       |
| **Medio**      | El Deber         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T22:01:30+00:00 |
| **Recopilado** | 2025-04-21T00:43:41.030310+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Justicia ordena apremio del ministro Edgar Montaño por deuda a extrabajadores de Sabsa
La medida busca ejecutar el pago de más de Bs 55 millones en beneficios laborales a extrabajadores de la extinta empresa aeroportuaria, quienes llevan tres años de espera
El juez Marcelo Cortez Candia, del Juzgado Público Civil, Comercial, de Partido del Trabajo y Seguridad Social de Yapacaní, emitió un mandamiento de apremio contra el ministro de Obras Públicas, Edgar Montaño Rojas, en el marco de un proceso judicial iniciado por extrabajadores del extinto Servicio de Aeropuertos Bolivianos S. A. (SABSA).
La disposición instruye a la Policía Boliviana aprehender a Montaño y trasladarlo a la carceleta de Buena Vista, hasta que se concrete el pago de Bs 55.189.880, por concepto de finiquitos pendientes a los extrabajadores que lo demandaron.
La decisión judicial responde a una larga lucha legal por parte de más de 600 extrabajadores a nivel nacional —190 de ellos en Santa Cruz— quienes desde hace tres años exigen el cumplimiento de sus derechos laborales tras el cierre de la empresa estatal.
La molestia del sector afectado se hizo visible el pasado 10 de enero, cuando realizaron una masiva protesta frente al Ministerio de Obras Públicas. En esa ocasión, denunciaron que, pese a las promesas públicas del ministro Montaño, el desembolso nunca se concretó.
“Nos dijo públicamente que, en 15 días, con la sentencia de la justicia, se realizaría el pago, e incluso se comprometió a colaborar para agilizar el juicio. Sin embargo, todas las instancias han fallado a nuestro favor y ellos siguen apelando”, lamentó uno de los afectados.
Los exempleados denuncian que las acciones del ministerio han sido dilatorias y que, aunque han recibido pagos parciales que suman apenas Bs 50.000 en tres años, la deuda total continúa pendiente. “Nos sentimos desamparados, pese a que la justicia nos ha respaldado en todas las instancias”, afirmaron durante la movilización.
El mandamiento de apremio busca precisamente presionar al ministro para ejecutar la sentencia, que ordena que se paguen los beneficios sociales a los extrabajadores de Sabsa.
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 3.92s | 1428.0 | 0.10 |
| extraccion_hechos | ❌ | `llama3-8b-8192` | 0m 3.69s |  | N/A |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 5.14s | 1821.0 | 0.20 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 1.05s | 1619.0 | 0.14 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 1.09s | 2069.0 | 0.06 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 3.92s
- **Tokens prompt:** 1295.0
- **Tokens respuesta:** 133.0
- **Total tokens:** 1428.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 7,
    "justificacion_relevancia": "La medida busca ejecutar el pago de una deuda laboral importante",
    "categorias_asignadas": [
        "Justicia/Legal",
        "Economía",
        "Sociedad/Derechos"
    ],
    "explicacion_concisa": "La justicia ordena apremiar al ministro Edgar Montaño para que pague una deuda de más de 55 millones de bolivianos a ex-trabajadores de Sabsa, que llevan tres años esperando el pago de sus finiquitos laborales"
}
```
</details>


### Tarea: extraccion_hechos

❌ **Estado:** Fallo (Error API)

   **Mensaje Error:** `API_Error: RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama3-8b-8192` in organization `org_01jsay2bafeeht06zsq8qv9mct` service tier `on_demand` on tokens per minute (TPM): Limit 100000, Used 98613, Requested 1890. Please try again in 301.8ms. Need more tokens? Visit https://groq.com/self-serve-support/ to request higher limits.', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}`

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 3.69s
- **Tokens prompt:** 
- **Tokens respuesta:** 
- **Total tokens:** 


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

_(Respuesta no es JSON válido o estructura incorrecta, mostrando raw):_
```
Error: No content received or generated
```
</details>


### Tarea: extraccion_entidades

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 5.14s
- **Tokens prompt:** 1512.0
- **Tokens respuesta:** 309.0
- **Total tokens:** 1821.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Edgar Montaño Rojas",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Marcelo Cortez Candia",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Sabsa",
            "tipo": "ORGANIZACION",
            "alias": [
                "Servicio de Aeropuertos Bolivianos S. A."
            ]
        },
        {
            "nombre": "Ministerio de Obras Públicas",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Policía Boliviana",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Buena Vista",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Santa Cruz",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Justicia",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Juzgado Público Civil, Comercial, de Partido del Trabajo y Seguridad Social de Yapacaní",
            "tipo": "INSTITUCION",
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
- **Tiempo:** 0m 1.05s
- **Tokens prompt:** 1424.0
- **Tokens respuesta:** 195.0
- **Total tokens:** 1619.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "\"Nos dijo públicamente que, en 15 días, con la sentencia de la justicia, se realizaría el pago, e incluso se comprometió a colaborar para agilizar el juicio. Sin embargo, todas las instancias han fallado a nuestro favor y ellos siguen apelando\"",
            "emisor_nombre": "uno de los afectados",
            "contexto": "Durante una protesta frente al Ministerio de Obras Públicas",
            "fecha_cita": null
        },
        {
            "cita": "\"Nos sentimos desamparados, pese a que la justicia nos ha respaldado en todas las instancias\"",
            "emisor_nombre": "los exempleados",
            "contexto": "Durante la movilización",
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
- **Tiempo:** 0m 1.09s
- **Tokens prompt:** 1943.0
- **Tokens respuesta:** 126.0
- **Total tokens:** 2069.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Monto de deuda pendiente a extrabajadores de Sabsa",
            "categoria": "presupuestario",
            "valor_numerico": 55189880.0,
            "unidad": "Bs",
            "ambito_geografico": [
                "Bolivia"
            ],
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
