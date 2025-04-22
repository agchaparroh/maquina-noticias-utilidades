# Evaluación Artículo: test_065
**Modelo Probado:** `llama3-8b-8192`

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://lahora.gt/nacionales/jmaldonado/2025/04/14/salud-analiza-aumentar-a-q1-mil-800-el-bono-a-salubristas-y-cumplir-con-articulo-140-del-presupuesto-general/           |
| **Título**     | Finanzas analiza aumentar a Q1 mil 800 el bono a salubristas y cumplir con artículo 140 del Presupuesto General       |
| **Medio**      | La Hora         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-20T17:40:42-06:00 |
| **Recopilado** | 2025-04-21T00:44:12.667165+00:00 |

---

## Contenido del Artículo Analizado

<details open>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
El Ministerio de Salud Pública continúa analizando propuestas financieras y poder otorgarle un bono a los trabajadores de varios renglones de esa dependencia. Anteriormente, el viceministro Administrativo de esa dependencia, Juan Carlos Oxom, comentó que la propuesta era de Q1 mil, pero ese monto puede aumentar.
Durante una citación este 14 de abril del diputado José Chic, el viceministro de Finanzas, Walter Figueroa, indicó que una de las propuestas que se presentará es que el bono sea de Q1 mil 800, como una cifra promedio, pues una de las peticiones es de hasta Q4 mil.
Figueroa agregó que entre los análisis que han realizado cuentan entre Q150 millones y Q200 millones, más el fondo de Q600 millones disponible que tiene la cartera de Salud.
«Hablamos de un punto medio, se requeriría de cinco números gruesos, de Q463 millones adicionales. Estamos partiendo de eso, la búsqueda de ese monto, que está más o menos por ese rango de Q1 mil 800 de bono. Hay que hacer avisos, por ahí los tenemos detectados, lo tenemos que soportar», respondió el funcionario de Finanzas.
El bono mensual se prevé que sea para personal de los renglones 011, 021, 022 y 031, mientras que para trabajadores del renglón 0029 y subgrupo 018 se contempla un bono único de Q2 mil, pero de este no se abordó en la citación.
Chic abogó porque se cuenten con los recursos para el personal de salud, pero sin desatender la red hospitalaria.
SALUD EVALUARÁ INFORMES
El viceministro Financiero de Salud, Juan Carlos Oxom, respondió que la propuesta se basa en un punto medio, pero no es definitiva, ya que puede variar por los análisis de la información de los dos ministerios.
«Se continúa el análisis técnico de la propuesta de los distintos sindicatos del sector de salud, como parte de este proceso. Se trabajará en la construcción de una propuesta que sea viable y sostenible, con el objetivo de no afectar la prestación de los servicios de salud a la población», respondió el Ministerio.
El artículo 140 del presupuesto general 2025, contempla que el Ministerio de Salud en su presupuesto realice las readecuaciones para financiar el proceso de incorporación de contratistas al renglón 011 «personal permanente», privilegiando la antigüedad en la prestación interrumpida de los servicios.
Asimismo, que las becas para estudiantes de Medicina, Ciencias de la Salud y Ciencias Médicas en Ejercicio Profesional Supervisado, en servicios de atención en salud de ese ministerio sea equivalente a la de un salario mínimo de actividades no agrícolas.
Proveer servicios de salud de calidad, dignos, humanos y con pertinencia cultural, es un factor vital para Santiago Atitlán, Sololá. 🏥🤝
En un espacio de diálogo y compromiso, se efectuó una reunión de seguimiento para verificar las áreas funcionales del Centro de Atención… pic.twitter.com/KCoUYRzvq3
— Ministerio de Salud Pública (@MinSaludGuate) April 14, 2025
En tendencia:
El significado detrás de la elaboración de la alfombra de verduras de Antigua Guatemala
Caso Odebrecht: Curruchiche hace nuevos señalamientos, pero no dice nada de otros implicados
Video: pastor y miembros de iglesia evangélica en Quetzaltenango se van a los golpes
VIDEO: Así fue el momento en que personas se llevan las verduras de alfombra en Antigua Guatemala
Video: hombre se lanza a una poza en Honduras y muere al impactar contra una piedra
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
    "justificacion_relevancia": "La propuesta de bono a salubristas puede tener impacto en la gestión de recursos del Ministerio de Salud",
    "categorias_asignadas": [
        "Salud",
        "Economía"
    ],
    "explicacion_concisa": "El Ministerio de Salud analiza propuestas financieras para otorgar un bono a trabajadores de varios renglones, con un posible monto de Q1 mil 800, para cumplir con el artículo 140 del Presupuesto General"
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
            "contenido": "El Ministerio de Salud Pública analiza propuestas financieras para otorgar un bono a los trabajadores de varios renglones de esa dependencia.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "dia",
            "paises": [
                "GT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "bono",
                "salubristas",
                "Ministerio de Salud Pública"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El viceministro de Finanzas, Walter Figueroa, propuso un bono de Q1 mil 800 para los trabajadores de los renglones 011, 021, 022 y 031.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "dia",
            "paises": [
                "GT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "bono",
                "salubristas",
                "Walter Figueroa"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El artículo 140 del Presupuesto General 2025 contempla que el Ministerio de Salud realice readecuaciones para financiar el proceso de incorporación de contratistas al renglón 011.",
            "tipo_hecho": "CONCEPTO",
            "fecha_ocurrencia_inicio": null,
            "fecha_ocurrencia_fin": null,
            "precision_temporal": null,
            "paises": [
                "GT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 5,
            "confiabilidad": 5,
            "etiquetas": [
                "Presupuesto General 2025",
                "Ministerio de Salud"
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
            "nombre": "Ministerio de Salud Pública",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Juan Carlos Oxom",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Walter Figueroa",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "José Chic",
            "tipo": "PERSONA",
            "alias": []
        },
        {
            "nombre": "Santiago Atitlán",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Sololá",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Centro de Atención",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Antigua Guatemala",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Quetzaltenango",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Honduras",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Caso Odebrecht",
            "tipo": "CONCEPTO",
            "alias": []
        },
        {
            "nombre": "Ministerio de Finanzas",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "Artículo 140 del presupuesto general 2025",
            "tipo": "NORMATIVA",
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
            "cita": "\"Hablamos de un punto medio, se requeriría de cinco números gruesos, de Q463 millones adicionales. Estamos partiendo de eso, la búsqueda de ese monto, que está más o menos por ese rango de Q1 mil 800 de bono. Hay que hacer avisos, por ahí los tenemos detectados, lo tenemos que soportar\"",
            "emisor_nombre": "Walter Figueroa",
            "contexto": "Durante una citación este 14 de abril del diputado José Chic",
            "fecha_cita": null
        },
        {
            "cita": "\"Se continúa el análisis técnico de la propuesta de los distintos sindicatos del sector de salud, como parte de este proceso. Se trabajará en la construcción de una propuesta que sea viable y sostenible, con el objetivo de no afectar la prestación de los servicios de salud a la población\"",
            "emisor_nombre": "Juan Carlos Oxom",
            "contexto": "Respondió el Ministerio",
            "fecha_cita": null
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
            "indicador": "Monto propuesto para el bono a los trabajadores del Ministerio de Salud",
            "categoria": "presupuestario",
            "valor_numerico": 1800000,
            "unidad": "quetzales",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Viceministro de Finanzas, Walter Figueroa",
            "notas_contexto": "Cifra promedio"
        },
        {
            "indicador": "Monto máximo propuesto para el bono a los trabajadores del Ministerio de Salud",
            "categoria": "presupuestario",
            "valor_numerico": 4000000,
            "unidad": "quetzales",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Viceministro de Finanzas, Walter Figueroa",
            "notas_contexto": "Una de las peticiones"
        },
        {
            "indicador": "Monto total para análisis de propuestas financieras",
            "categoria": "presupuestario",
            "valor_numerico": 150000000,
            "unidad": "quetzales",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Viceministro de Finanzas, Walter Figueroa",
            "notas_contexto": "Entre Q150 millones y Q200 millones"
        },
        {
            "indicador": "Monto adicional requerido para el bono",
            "categoria": "presupuestario",
            "valor_numerico": 463000000,
            "unidad": "quetzales",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Viceministro de Finanzas, Walter Figueroa",
            "notas_contexto": "Punto medio"
        },
        {
            "indicador": "Monto del fondo disponible para la cartera de Salud",
            "categoria": "presupuestario",
            "valor_numerico": 600000000,
            "unidad": "quetzales",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Viceministro de Finanzas, Walter Figueroa",
            "notas_contexto": "Fondo disponible"
        },
        {
            "indicador": "Monto del bono único para trabajadores del renglón 0029 y subgrupo 018",
            "categoria": "presupuestario",
            "valor_numerico": 2000000,
            "unidad": "quetzales",
            "ambito_geografico": [],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Viceministro de Finanzas, Walter Figueroa",
            "notas_contexto": "Bono único"
        }
    ]
}
```
</details>
