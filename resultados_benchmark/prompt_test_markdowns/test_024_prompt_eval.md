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
| relevancia | ✅ | `llama3-8b-8192` | 0m 3.77s | 847.0 | 0.10 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 6.06s | 1771.0 | 0.09 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 3.64s | 1068.0 | 0.09 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 3.50s | 896.0 | 0.01 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 6.03s | 1415.0 | 0.00 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 3.77s
- **Tokens prompt:** 769.0
- **Tokens respuesta:** 78.0
- **Total tokens:** 847.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 2,
    "justificacion_relevancia": "No contiene información política o social relevante",
    "categorias_asignadas": [
        "Análisis/Contexto"
    ],
    "explicacion_concisa": "El artículo es la política de privacidad y seguridad de YouTube, sin contenido político o social relevante"
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 6.06s
- **Tokens prompt:** 1622.0
- **Tokens respuesta:** 149.0
- **Total tokens:** 1771.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "YouTube es un servicio de video en línea propiedad de Google LLC.",
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
                "Google",
                "video",
                "servicio"
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
- **Tiempo:** 0m 3.64s
- **Tokens prompt:** 977.0
- **Tokens respuesta:** 91.0
- **Total tokens:** 1068.0


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
            "alias": []
        },
        {
            "nombre": "Policy & Safety",
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
- **Tiempo:** 0m 3.50s
- **Tokens prompt:** 889.0
- **Tokens respuesta:** 7.0
- **Total tokens:** 896.0


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
- **Tiempo:** 0m 6.03s
- **Tokens prompt:** 1408.0
- **Tokens respuesta:** 7.0
- **Total tokens:** 1415.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": []
}
```
</details>
