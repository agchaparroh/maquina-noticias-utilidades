# Evaluación Artículo: test_066

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://eldeber.com.bo/pais/fiscalia-llamara-al-gabinete-civil-de-zuniga-declarar-en-calidad-de-testigos_510602/           |
| **Título**     | Fiscalía llamará al ‘gabinete civil’ de Zúñiga a declarar en calidad de testigos       |
| **Medio**      | El Deber         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-14T22:34:00+00:00 |
| **Recopilado** | 2025-04-21T00:44:13.163271+00:00 |

---

## Contenido del Artículo Analizado

<details>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
Fiscalía llamará al ‘gabinete civil’ de Zúñiga a declarar en calidad de testigos
El fiscal Torrez dijo que las órdenes de aprehensión y el documental fueron una ‘coincidencia’
Las siete personas que supuestamente iban a conformar el ‘gabinete civil’ de Juan José Zúñiga serán convocadas a declarar, en calidad de testigos, porque deben aportar a las investigaciones, adelantó este lunes el fiscal departamental de La Paz, Luis Carlos Torrez, quien también defendió el trabajo de la Fiscalía y dijo que las ordenes de aprehensión estaban listas antes de la emisión del documental.
“Sobre la conformación de un gabinete de ministros, vuelvo a aclarar a la opinión pública de que no existen más órdenes de aprehensión ni ampliaciones; pero sí nosotros vamos, a fin de poder llegar a la verdad histórica del hecho, los vamos a convocar exclusivamente para que presten su declaración, pero en calidad de testigos”, dijo en conferencia de prensa.
El jueves pasado, el Gobierno presentó su documental ‘Qué pasó el 26-J’, en el cual acusa abiertamente de la participación de civiles y militares y también menciona a analistas y dirigentes que irían a integrar el ‘gabinete civil’, y se señala a los analistas: Gonzalo Chávez, Joshua Bellot, Paul Antonio Coca, Ana María Maldonado y Jaime Dunn; además de los dirigentes José Luis Álvarez, César González y el abogado Jorge Valda, quien fue aprehendido y liberado el fin de semana.
El fiscal Torrez reiteró una y otra vez que no existe ninguna otra orden de aprehensión y dijo que la anterior semana se liberaron cinco órdenes de las cuales se ejecutaron cuatro: contra Valda, Bismarck Imaña, Marco Antonio Bracamonte y Mario Tanaka. No se ejecutó la orden de aprehensión contra el diputado Andrés Ribera Salas, precisó el fiscal.
Frente a las acusaciones de activar el caso solo cuando apareció el documental, Torrez dijo que los fiscales ya tenían las ordenes de aprehensión, pero no supo explicar cómo obtuvo e Gobierno los datos, nombres, lugares, fechas, mensajes, grabaciones exhibidas en el polémico video.
“La proyección del documental, el suscrito desconocía en relación a la presentación; vamos a suponer, posiblemente, que ha sido ya un hecho netamente de ministerio de Gobierno la publicación, pero nosotros días antes ya habíamos solicitado la emisión de esas órdenes”, justificó el fiscal.
Más adelante dijo que solicitaron la ampliación de las investigaciones, dado que ese plazo vence a finales de abril; evalúan pedir una nueva ampliación. De acuerdo con la Ley, el caso puede ser ampliado por otros seis meses después de la última aprehensión, de tal modo, que ampliarían hasta septiembre.
```
</details>

---

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 1.26s | 1431.0 | 0.10 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 1.65s | 3200.0 | 0.38 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 1.95s | 2162.0 | 0.31 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 1.12s | 1801.0 | 0.15 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 1.67s | 2556.0 | 0.23 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.26s
- **Tokens prompt:** 1300.0
- **Tokens respuesta:** 131.0
- **Total tokens:** 1431.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "Relevancia media por involucrar a figuras políticas y fiscales en un caso de investigación",
    "categorias_asignadas": [
        "Justicia/Legal",
        "Política Nacional"
    ],
    "explicacion_concisa": "La Fiscalía llama a declarar a miembros del 'gabinete civil' de Juan José Zúñiga como testigos en un caso de investigación, relacionado con el documental 'Qué pasó el 26-J' y órdenes de aprehensión"
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 1.65s
- **Tokens prompt:** 2318.0
- **Tokens respuesta:** 882.0
- **Total tokens:** 3200.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "La Fiscalía llamará al 'gabinete civil' de Zúñiga a declarar en calidad de testigos.",
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
                "justicia",
                "investigación",
                "Fiscalía"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El fiscal Torrez dijo que las órdenes de aprehensión y el documental fueron una 'coincidencia'.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "justicia",
                "investigación",
                "Fiscalía"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Se convocarán a declarar a las siete personas que supuestamente iban a conformar el 'gabinete civil' de Juan José Zúñiga.",
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
                "justicia",
                "investigación",
                "Fiscalía"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El Gobierno presentó su documental 'Qué pasó el 26-J', en el cual acusa abiertamente de la participación de civiles y militares y también menciona a analistas y dirigentes que irían a integrar el 'gabinete civil'.",
            "tipo_hecho": "ANUNCIO",
            "fecha_ocurrencia_inicio": "2025-04-10T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 4,
            "etiquetas": [
                "política",
                "gobierno",
                "documental"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El fiscal Torrez reiteró que no existe ninguna otra orden de aprehensión y dijo que la anterior semana se liberaron cinco órdenes de las cuales se ejecutó cuatro.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14T00:00:00Z",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "BO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "justicia",
                "investigación",
                "Fiscalía"
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
- **Tiempo:** 0m 1.95s
- **Tokens prompt:** 1650.0
- **Tokens respuesta:** 512.0
- **Total tokens:** 2162.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Juan José Zúñiga",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Luis Carlos Torrez",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Gonzalo Chávez",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Joshua Bellot",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Paul Antonio Coca",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Ana María Maldonado",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Jaime Dunn",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "José Luis Álvarez",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "César González",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Jorge Valda",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Andrés Ribera Salas",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Bismarck Imaña",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Marco Antonio Bracamonte",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Mario Tanaka",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Fiscalía",
            "tipo": "INSTITUCION",
            "alias": [
                "Gobierno"
            ]
        },
        {
            "nombre": "Gabinete civil",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "La Paz",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "26-J",
            "tipo": "EVENTO",
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
- **Tiempo:** 0m 1.12s
- **Tokens prompt:** 1562.0
- **Tokens respuesta:** 239.0
- **Total tokens:** 1801.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "Sobre la conformación de un gabinete de ministros, vuelvo a aclarar a la opinión pública de que no existen más órdenes de aprehensión ni ampliaciones; pero sí nosotros vamos, a fin de poder llegar a la verdad histórica del hecho, los vamos a convocar exclusivamente para que presten su declaración, pero en calidad de testigos",
            "emisor_nombre": "Luis Carlos Torrez",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "La proyección del documental, el suscrito desconocía en relación a la presentación; vamos a suponer, posiblemente, que ha sido ya un hecho netamente de ministerio de Gobierno la publicación, pero nosotros días antes ya habíamos solicitado la emisión de esas órdenes",
            "emisor_nombre": "Luis Carlos Torrez",
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
- **Tiempo:** 0m 1.67s
- **Tokens prompt:** 2081.0
- **Tokens respuesta:** 475.0
- **Total tokens:** 2556.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Número de órdenes de aprehensión",
            "categoria": "presupuestario",
            "valor_numerico": 5,
            "unidad": "órdenes",
            "ambito_geografico": [
                "Bolivia"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Fiscalía",
            "notas_contexto": null
        },
        {
            "indicador": "Número de órdenes de aprehensión ejecutadas",
            "categoria": "presupuestario",
            "valor_numerico": 4,
            "unidad": "órdenes",
            "ambito_geografico": [
                "Bolivia"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Fiscalía",
            "notas_contexto": null
        },
        {
            "indicador": "Número de órdenes de aprehensión no ejecutadas",
            "categoria": "presupuestario",
            "valor_numerico": 1,
            "unidad": "órdenes",
            "ambito_geografico": [
                "Bolivia"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Fiscalía",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas que conformarían el 'gabinete civil' de Zúñiga",
            "categoria": "demográfico",
            "valor_numerico": 7,
            "unidad": "personas",
            "ambito_geografico": [
                "Bolivia"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Fiscalía",
            "notas_contexto": null
        }
    ]
}
```
</details>
