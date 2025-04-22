# Evaluación Artículo: test_024
**Modelo Probado:** `llama3-8b-8192`

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

<details open>
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

## Resultados de las Tareas (llama3-8b-8192)

### Tarea: relevancia

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 2,
    "justificacion_relevancia": "No contiene información política o social relevante",
    "categorias_asignadas": [
        "Análisis/Contexto"
    ],
    "explicacion_concisa": "El artículo es la página de información general de YouTube, sin contenido político o social relevante"
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "YouTube es una plataforma de video en línea propiedad de Google LLC.",
            "tipo_hecho": "BIOGRAFIA",
            "fecha_ocurrencia_inicio": "2005-02-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "US"
            ],
            "ubicaciones_especificas": [],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "YouTube",
                "Google",
                "plataforma de video"
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
    "resultados": []
}
```
</details>


### Tarea: extraccion_datos

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": []
}
```
</details>
