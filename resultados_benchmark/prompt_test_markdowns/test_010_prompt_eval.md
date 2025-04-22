# Evaluación Artículo: test_010

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.diariolibre.com/politica/general/2025/04/14/abinader-entiende-que-debe-hacerse-justicia-en-el-caso-jet-set/3074042           |
| **Título**     | Abinader sobre proceso legal Jet Set: "Nosotros vamos a respetar que se haga justicia"       |
| **Medio**      | Diario Libre         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T00:00:00+00:00 |
| **Recopilado** | 2025-04-21T00:42:36.436500+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Abinader sobre proceso legal Jet Set: "Nosotros vamos a respetar que se haga justicia"
Aseguró que los afectados no van a encontrar "ningún tipo de incidencia del Gobierno"
El mandatario entiende que debe hacerse justicia
El presidente de la República, Luis Abinader, dio garantía este lunes de que el Gobierno no va a interferir en el proceso judicial que pudiera generar la investigación que se realiza sobre el colapso del techo de la discoteca Jet Set, que dejó 231 muertos y más de 180 heridos, algunos de gravedad.
El mandatario hizo el planteamiento al contestar una pregunta durante LA Semanal con la Prensa en el Palacio Nacional.
También planteó que entiende que debe hacerse justicia con el hecho.
"Nosotros vamos a respetar que se haga justicia, como tiene que hacerse justicia, y nosotros eso lo vamos a respetar y no van a encontrar ningún tipo de incidencia del Gobierno en los aspectos de justicia", subrayó.
El jefe de Estado dijo que su Gobierno nunca ha obstaculizado un proceso judicial.
"Si hay un gobierno que ha respetado todos los procesos legales es este Gobierno", indicó.
El desplome del techo de la emblemática discoteca Jet Set ocurrió la madrugada del martes 8 de este abril cuando el merenguero Rubby Pérez amenizaba una fiesta. El artista también falleció bajos los escombros.
Ministerio Público investiga tragedia en la discoteca Jet Set
Contratista autorizó envío de escombros de Jet Set a Santiago; dice no hubo mala intención
Depositan y resguardan en la Ciudad Ganadera parte de los escombros de la discoteca Jet Set
La investigación está abierta
La investigación penal, que está "abierta", la efectúa la Dirección General de Persecución del Ministerio Público, que encabeza el procurador adjunto Wilson Camacho, y la Fiscalía del Distrito Nacional.
Paralelamente, el Gobierno nombró una comisión con expertos nacionales e internacionales para que investigue el siniestro.
El lugar de la tragedia está resguardado por efectivos de la Policía Nacional, mientras que los escombros fueron retirados y llevados a la Ciudad Ganadera para su análisis. Otra parte fue llevada a Santiago. Sobre esto, Ramón Rodríguez, encargado de equipos de una empresa contratista que trabaja en el monorriel de Santiago, dijo que el traslado se hizo "por error" a esa provincia.
"El equipo que fue desde aquí no sabía andar en la capital ni sabía dónde había un vertedero para botar eso, y nosotros le autorizamos que lo trajera para acá, para Santiago, porque aquí es que botamos los desperdicios del monorriel", explicó Rodríguez hace unos días.
Sobre el colapso del techo de la discoteca Jet Set, el mandatario haacotado que ahora hay que conocer qué pasó y por qué pasó.
La labor fue encargada a la Oficina Nacional de Evaluación Sísmica y Vulnerabilidad (Onasvie). Abinader indicó hoy que las indagatorias las encabezará el ingeniero geólogo Leonardo Reyes Madera, de quien dijo que es un gran profesional conocido por toda la sociedad.
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 0.49s | 1402.0 | 0.10 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 2.08s | 3082.0 | 0.30 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 0.73s | 2014.0 | 0.18 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 0.95s | 1876.0 | 0.16 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 1.36s | 2379.0 | 0.11 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.49s
- **Tokens prompt:** 1273.0
- **Tokens respuesta:** 129.0
- **Total tokens:** 1402.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 8,
    "justificacion_relevancia": "El presidente Abinader garantiza la independencia del proceso judicial sobre el colapso de la discoteca Jet Set",
    "categorias_asignadas": [
        "Conflicto/Seguridad",
        "Justicia/Legal"
    ],
    "explicacion_concisa": "El presidente de la República, Luis Abinader, asegura que el Gobierno no interferirá en el proceso judicial sobre el colapso de la discoteca Jet Set, que dejó 231 muertos y más de 180 heridos"
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 2.08s
- **Tokens prompt:** 2376.0
- **Tokens respuesta:** 706.0
- **Total tokens:** 3082.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "El presidente de la República, Luis Abinader, aseguró que el Gobierno no va a interferir en el proceso judicial que pudiera generar la investigación sobre el colapso del techo de la discoteca Jet Set.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "DO"
            ],
            "ubicaciones_especificas": [
                "Palacio Nacional"
            ],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "gobierno",
                "justicia",
                "investigación"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El colapso del techo de la discoteca Jet Set dejó 231 muertos y más de 180 heridos, algunos de gravedad.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-08T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "DO"
            ],
            "ubicaciones_especificas": [
                "discoteca Jet Set"
            ],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "tragedia",
                "discoteca",
                "muertes"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El Ministerio Público investiga la tragedia en la discoteca Jet Set.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-08T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "DO"
            ],
            "ubicaciones_especificas": [
                "discoteca Jet Set"
            ],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "investigación",
                "Ministerio Público"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La Oficina Nacional de Evaluación Sísmica y Vulnerabilidad (Onasvie) encabezará la investigación sobre el colapso del techo de la discoteca Jet Set.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "DO"
            ],
            "ubicaciones_especificas": [
                "Palacio Nacional"
            ],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "investigación",
                "Onasvie"
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
- **Tiempo:** 0m 0.73s
- **Tokens prompt:** 1710.0
- **Tokens respuesta:** 304.0
- **Total tokens:** 2014.0


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
            "nombre": "Jet Set",
            "tipo": "LUGAR",
            "alias": [
                "discoteca Jet Set"
            ]
        },
        {
            "nombre": "Ministerio Público",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Dirección General de Persecución",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Fiscalía del Distrito Nacional",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Policía Nacional",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Ramón Rodríguez",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Leonardo Reyes Madera",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Onasvie",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Rubby Pérez",
            "tipo": "PERSONA",
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
- **Tiempo:** 0m 0.95s
- **Tokens prompt:** 1622.0
- **Tokens respuesta:** 254.0
- **Total tokens:** 1876.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "Nosotros vamos a respetar que se haga justicia, como tiene que hacerse justicia, y nosotros eso lo vamos a respetar y no van a encontrar ningún tipo de incidencia del Gobierno en los aspectos de justicia",
            "emisor_nombre": "Luis Abinader",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "Si hay un gobierno que ha respetado todos los procesos legales es este Gobierno",
            "emisor_nombre": "Luis Abinader",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "El equipo que fue desde aquí no sabía andar en la capital ni sabía dónde había un vertedero para botar eso, y nosotros le autorizamos que lo trajera para acá, para Santiago, porque aquí es que botamos los desperdicios del monorriel",
            "emisor_nombre": "Ramón Rodríguez",
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
- **Tiempo:** 0m 1.36s
- **Tokens prompt:** 2141.0
- **Tokens respuesta:** 238.0
- **Total tokens:** 2379.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Número de muertos en el colapso de la discoteca Jet Set",
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
            "indicador": "Número de heridos en el colapso de la discoteca Jet Set",
            "categoria": "social",
            "valor_numerico": 180,
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
