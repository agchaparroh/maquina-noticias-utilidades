# Evaluación Artículo: test_024

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.youtube.com/watch?v=8yHLLmZ8OB4           |
| **Título**     | - YouTube       |
| **Medio**      | None         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-21T00:42:50.273586+00:00 |
| **Recopilado** | 2025-04-21T00:42:50.274130+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
About
Press
Copyright
Contact us
Creator
Advertise
Developers
Terms
Privacy
Policy & Safety
How YouTube works
Test new features
© 2025 Google LLC
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 0.48s | 854.0 | 0.11 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 0.56s | 1797.0 | 0.09 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 0.47s | 1154.0 | 0.17 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 0.34s | 861.0 | 0.01 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 0.42s | 1448.0 | 0.00 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.48s
- **Tokens prompt:** 769.0
- **Tokens respuesta:** 85.0
- **Total tokens:** 854.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 2,
    "justificacion_relevancia": "No contiene información política o social relevante",
    "categorias_asignadas": [
        "Análisis/Contexto"
    ],
    "explicacion_concisa": "El artículo es la página de información general de YouTube, no contiene contenido político o social relevante para la esfera hispana"
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.56s
- **Tokens prompt:** 1653.0
- **Tokens respuesta:** 144.0
- **Total tokens:** 1797.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "YouTube es un servicio de video en línea propiedad de Google.",
            "tipo_hecho": "CONCEPTO",
            "fecha_ocurrencia_inicio": "2005-02-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "año",
            "paises": [],
            "ubicaciones_especificas": [],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "YouTube",
                "video",
                "Google"
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
- **Tiempo:** 0m 0.47s
- **Tokens prompt:** 986.0
- **Tokens respuesta:** 168.0
- **Total tokens:** 1154.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Google LLC",
            "tipo": "ORGANIZACION",
            "alias": [
                "Google"
            ]
        },
        {
            "nombre": "YouTube",
            "tipo": "ORGANIZACION",
            "alias": [
                "YouTube"
            ]
        },
        {
            "nombre": "Copyright",
            "tipo": "NORMATIVA",
            "alias": []
        },
        {
            "nombre": "Policy & Safety",
            "tipo": "NORMATIVA",
            "alias": []
        },
        {
            "nombre": "Terms",
            "tipo": "NORMATIVA",
            "alias": []
        },
        {
            "nombre": "Privacy",
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
- **Tiempo:** 0m 0.34s
- **Tokens prompt:** 854.0
- **Tokens respuesta:** 7.0
- **Total tokens:** 861.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": []
}
```
</details>


### Tarea: extraccion_datos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.42s
- **Tokens prompt:** 1441.0
- **Tokens respuesta:** 7.0
- **Total tokens:** 1448.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": []
}
```
</details>
