# Evaluación Artículo: test_065
**Modelo Probado:** `llama-3.1-8b-instant`

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

## Resultados de las Tareas (llama-3.1-8b-instant)

### Tarea: relevancia

✅ **Estado:** Éxito


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 6,
    "justificacion_relevancia": "Relevancia media debido a la propuesta de bono para trabajadores de salud y análisis presupuestario.",
    "categorias_asignadas": [
        "Política Nacional",
        "Economía"
    ],
    "explicacion_concisa": "El Ministerio de Salud Pública analiza propuestas financieras para otorgar un bono a trabajadores de salud, con un monto potencial de Q1 mil 800. El viceministro de Finanzas mencionó que se buscará un punto medio en el rango de Q463 millones adicionales. El bono se prevé para personal de ciertos renglones y subgrupos, con un bono único de Q2 mil para trabajadores del renglón 0029 y subgrupo 018."
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
            "contenido": "El Ministerio de Salud Pública continúa analizando propuestas financieras para otorgar un bono a los trabajadores de varios renglones de esa dependencia.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-20",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "GT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "salud",
                "bono",
                "ministerio"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El viceministro de Finanzas, Walter Figueroa, indicó que una de las propuestas es que el bono sea de Q1 mil 800, como una cifra promedio.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-14",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "GT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "finanzas",
                "bono",
                "salud"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El bono mensual se prevé que sea para personal de los renglones 011, 021, 022 y 031.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-20",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "GT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "salud",
                "bono",
                "renglones"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El artículo 140 del Presupuesto General 2025 contempla que el Ministerio de Salud realice readecuaciones para financiar la incorporación de contratistas al renglón 011.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-20",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "GT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "presupuesto",
                "salud",
                "contratistas"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "El Ministerio de Salud evaluará informes y trabajará en la construcción de una propuesta que sea viable y sostenible.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-20",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "GT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 6,
            "confiabilidad": 5,
            "etiquetas": [
                "salud",
                "ministerio",
                "propuesta"
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
            "alias": [
                "Ministerio de Salud"
            ]
        },
        {
            "nombre": "Juan Carlos Oxom",
            "tipo": "PERSONA",
            "alias": [
                "Juan Carlos Oxom"
            ]
        },
        {
            "nombre": "Pedro Sánchez Pérez-Castejón",
            "tipo": "PERSONA",
            "alias": [
                "Pedro Sánchez"
            ]
        },
        {
            "nombre": "José Chic",
            "tipo": "PERSONA",
            "alias": [
                "José Chic"
            ]
        },
        {
            "nombre": "Walter Figueroa",
            "tipo": "PERSONA",
            "alias": [
                "Walter Figueroa"
            ]
        },
        {
            "nombre": "Santiago Atitlán",
            "tipo": "LUGAR",
            "alias": [
                "Santiago Atitlán"
            ]
        },
        {
            "nombre": "Sololá",
            "tipo": "LUGAR",
            "alias": [
                "Sololá"
            ]
        },
        {
            "nombre": "Caso Odebrecht",
            "tipo": "CONCEPTO",
            "alias": [
                "Caso Odebrecht"
            ]
        },
        {
            "nombre": "Antigua Guatemala",
            "tipo": "LUGAR",
            "alias": [
                "Antigua Guatemala"
            ]
        },
        {
            "nombre": "Quetzaltenango",
            "tipo": "LUGAR",
            "alias": [
                "Quetzaltenango"
            ]
        },
        {
            "nombre": "Honduras",
            "tipo": "LUGAR",
            "alias": [
                "Honduras"
            ]
        },
        {
            "nombre": "ONU",
            "tipo": "OTRO",
            "alias": [
                "ONU"
            ]
        },
        {
            "nombre": "FMI",
            "tipo": "OTRO",
            "alias": [
                "FMI"
            ]
        },
        {
            "nombre": "Gobierno",
            "tipo": "INSTITUCION",
            "alias": [
                "Gobierno"
            ]
        },
        {
            "nombre": "Parlamento",
            "tipo": "INSTITUCION",
            "alias": [
                "Parlamento"
            ]
        },
        {
            "nombre": "Tribunales",
            "tipo": "INSTITUCION",
            "alias": [
                "Tribunales"
            ]
        },
        {
            "nombre": "Fuerzas Armadas",
            "tipo": "INSTITUCION",
            "alias": [
                "Fuerzas Armadas"
            ]
        },
        {
            "nombre": "Policía",
            "tipo": "INSTITUCION",
            "alias": [
                "Policía"
            ]
        },
        {
            "nombre": "Ley",
            "tipo": "NORMATIVA",
            "alias": [
                "Ley"
            ]
        },
        {
            "nombre": "Decreto",
            "tipo": "NORMATIVA",
            "alias": [
                "Decreto"
            ]
        },
        {
            "nombre": "Tratado",
            "tipo": "NORMATIVA",
            "alias": [
                "Tratado"
            ]
        },
        {
            "nombre": "Constitución",
            "tipo": "NORMATIVA",
            "alias": [
                "Constitución"
            ]
        },
        {
            "nombre": "Elecciones",
            "tipo": "EVENTO",
            "alias": [
                "Elecciones"
            ]
        },
        {
            "nombre": "Cumbre",
            "tipo": "EVENTO",
            "alias": [
                "Cumbre"
            ]
        },
        {
            "nombre": "Protestas",
            "tipo": "EVENTO",
            "alias": [
                "Protestas"
            ]
        },
        {
            "nombre": "Conflictos",
            "tipo": "EVENTO",
            "alias": [
                "Conflictos"
            ]
        },
        {
            "nombre": "Desastres Naturales",
            "tipo": "EVENTO",
            "alias": [
                "Desastres Naturales"
            ]
        },
        {
            "nombre": "Caso Gürtel",
            "tipo": "CONCEPTO",
            "alias": [
                "Caso Gürtel"
            ]
        },
        {
            "nombre": "Crisis Migratoria",
            "tipo": "CONCEPTO",
            "alias": [
                "Crisis Migratoria"
            ]
        },
        {
            "nombre": "Centro de Atención",
            "tipo": "LUGAR",
            "alias": [
                "Centro de Atención"
            ]
        },
        {
            "nombre": "Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Salud"
            ]
        },
        {
            "nombre": "Medicina",
            "tipo": "CONCEPTO",
            "alias": [
                "Medicina"
            ]
        },
        {
            "nombre": "Ciencias de la Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Ciencias de la Salud"
            ]
        },
        {
            "nombre": "Ciencias Médicas",
            "tipo": "CONCEPTO",
            "alias": [
                "Ciencias Médicas"
            ]
        },
        {
            "nombre": "Servicios de Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud"
            ]
        },
        {
            "nombre": "Atención en Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Atención en Salud"
            ]
        },
        {
            "nombre": "Prestación de Servicios",
            "tipo": "CONCEPTO",
            "alias": [
                "Prestación de Servicios"
            ]
        },
        {
            "nombre": "Salario Mínimo",
            "tipo": "CONCEPTO",
            "alias": [
                "Salario Mínimo"
            ]
        },
        {
            "nombre": "Actividades No Agrícolas",
            "tipo": "CONCEPTO",
            "alias": [
                "Actividades No Agrícolas"
            ]
        },
        {
            "nombre": "Bono",
            "tipo": "CONCEPTO",
            "alias": [
                "Bono"
            ]
        },
        {
            "nombre": "Propuesta",
            "tipo": "CONCEPTO",
            "alias": [
                "Propuesta"
            ]
        },
        {
            "nombre": "Análisis",
            "tipo": "CONCEPTO",
            "alias": [
                "Análisis"
            ]
        },
        {
            "nombre": "Fondo",
            "tipo": "CONCEPTO",
            "alias": [
                "Fondo"
            ]
        },
        {
            "nombre": "Monto",
            "tipo": "CONCEPTO",
            "alias": [
                "Monto"
            ]
        },
        {
            "nombre": "Rango",
            "tipo": "CONCEPTO",
            "alias": [
                "Rango"
            ]
        },
        {
            "nombre": "Punto Medio",
            "tipo": "CONCEPTO",
            "alias": [
                "Punto Medio"
            ]
        },
        {
            "nombre": "Cifra Promedio",
            "tipo": "CONCEPTO",
            "alias": [
                "Cifra Promedio"
            ]
        },
        {
            "nombre": "Números Gruesos",
            "tipo": "CONCEPTO",
            "alias": [
                "Números Gruesos"
            ]
        },
        {
            "nombre": "Monto Adicional",
            "tipo": "CONCEPTO",
            "alias": [
                "Monto Adicional"
            ]
        },
        {
            "nombre": "Bono Mensual",
            "tipo": "CONCEPTO",
            "alias": [
                "Bono Mensual"
            ]
        },
        {
            "nombre": "Personal de Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Personal de Salud"
            ]
        },
        {
            "nombre": "Red Hospitalaria",
            "tipo": "CONCEPTO",
            "alias": [
                "Red Hospitalaria"
            ]
        },
        {
            "nombre": "Prestación de Servicios de Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Prestación de Servicios de Salud"
            ]
        },
        {
            "nombre": "Población",
            "tipo": "CONCEPTO",
            "alias": [
                "Población"
            ]
        },
        {
            "nombre": "Servicios de Atención en Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Atención en Salud"
            ]
        },
        {
            "nombre": "Servicios de Salud de Calidad",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud de Calidad"
            ]
        },
        {
            "nombre": "Servicios de Salud Dignos",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud Dignos"
            ]
        },
        {
            "nombre": "Servicios de Salud Humanos",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud Humanos"
            ]
        },
        {
            "nombre": "Servicios de Salud con Pertinencia Cultural",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud con Pertinencia Cultural"
            ]
        },
        {
            "nombre": "Santiago Atitlán",
            "tipo": "LUGAR",
            "alias": [
                "Santiago Atitlán"
            ]
        },
        {
            "nombre": "Sololá",
            "tipo": "LUGAR",
            "alias": [
                "Sololá"
            ]
        },
        {
            "nombre": "Ministerio de Salud Pública",
            "tipo": "INSTITUCION",
            "alias": [
                "Ministerio de Salud"
            ]
        },
        {
            "nombre": "Juan Carlos Oxom",
            "tipo": "PERSONA",
            "alias": [
                "Juan Carlos Oxom"
            ]
        },
        {
            "nombre": "Pedro Sánchez Pérez-Castejón",
            "tipo": "PERSONA",
            "alias": [
                "Pedro Sánchez"
            ]
        },
        {
            "nombre": "José Chic",
            "tipo": "PERSONA",
            "alias": [
                "José Chic"
            ]
        },
        {
            "nombre": "Walter Figueroa",
            "tipo": "PERSONA",
            "alias": [
                "Walter Figueroa"
            ]
        },
        {
            "nombre": "Santiago Atitlán",
            "tipo": "LUGAR",
            "alias": [
                "Santiago Atitlán"
            ]
        },
        {
            "nombre": "Sololá",
            "tipo": "LUGAR",
            "alias": [
                "Sololá"
            ]
        },
        {
            "nombre": "Caso Odebrecht",
            "tipo": "CONCEPTO",
            "alias": [
                "Caso Odebrecht"
            ]
        },
        {
            "nombre": "Antigua Guatemala",
            "tipo": "LUGAR",
            "alias": [
                "Antigua Guatemala"
            ]
        },
        {
            "nombre": "Quetzaltenango",
            "tipo": "LUGAR",
            "alias": [
                "Quetzaltenango"
            ]
        },
        {
            "nombre": "Honduras",
            "tipo": "LUGAR",
            "alias": [
                "Honduras"
            ]
        },
        {
            "nombre": "ONU",
            "tipo": "OTRO",
            "alias": [
                "ONU"
            ]
        },
        {
            "nombre": "FMI",
            "tipo": "OTRO",
            "alias": [
                "FMI"
            ]
        },
        {
            "nombre": "Gobierno",
            "tipo": "INSTITUCION",
            "alias": [
                "Gobierno"
            ]
        },
        {
            "nombre": "Parlamento",
            "tipo": "INSTITUCION",
            "alias": [
                "Parlamento"
            ]
        },
        {
            "nombre": "Tribunales",
            "tipo": "INSTITUCION",
            "alias": [
                "Tribunales"
            ]
        },
        {
            "nombre": "Fuerzas Armadas",
            "tipo": "INSTITUCION",
            "alias": [
                "Fuerzas Armadas"
            ]
        },
        {
            "nombre": "Policía",
            "tipo": "INSTITUCION",
            "alias": [
                "Policía"
            ]
        },
        {
            "nombre": "Ley",
            "tipo": "NORMATIVA",
            "alias": [
                "Ley"
            ]
        },
        {
            "nombre": "Decreto",
            "tipo": "NORMATIVA",
            "alias": [
                "Decreto"
            ]
        },
        {
            "nombre": "Tratado",
            "tipo": "NORMATIVA",
            "alias": [
                "Tratado"
            ]
        },
        {
            "nombre": "Constitución",
            "tipo": "NORMATIVA",
            "alias": [
                "Constitución"
            ]
        },
        {
            "nombre": "Elecciones",
            "tipo": "EVENTO",
            "alias": [
                "Elecciones"
            ]
        },
        {
            "nombre": "Cumbre",
            "tipo": "EVENTO",
            "alias": [
                "Cumbre"
            ]
        },
        {
            "nombre": "Protestas",
            "tipo": "EVENTO",
            "alias": [
                "Protestas"
            ]
        },
        {
            "nombre": "Conflictos",
            "tipo": "EVENTO",
            "alias": [
                "Conflictos"
            ]
        },
        {
            "nombre": "Desastres Naturales",
            "tipo": "EVENTO",
            "alias": [
                "Desastres Naturales"
            ]
        },
        {
            "nombre": "Caso Gürtel",
            "tipo": "CONCEPTO",
            "alias": [
                "Caso Gürtel"
            ]
        },
        {
            "nombre": "Crisis Migratoria",
            "tipo": "CONCEPTO",
            "alias": [
                "Crisis Migratoria"
            ]
        },
        {
            "nombre": "Centro de Atención",
            "tipo": "LUGAR",
            "alias": [
                "Centro de Atención"
            ]
        },
        {
            "nombre": "Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Salud"
            ]
        },
        {
            "nombre": "Medicina",
            "tipo": "CONCEPTO",
            "alias": [
                "Medicina"
            ]
        },
        {
            "nombre": "Ciencias de la Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Ciencias de la Salud"
            ]
        },
        {
            "nombre": "Ciencias Médicas",
            "tipo": "CONCEPTO",
            "alias": [
                "Ciencias Médicas"
            ]
        },
        {
            "nombre": "Servicios de Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud"
            ]
        },
        {
            "nombre": "Atención en Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Atención en Salud"
            ]
        },
        {
            "nombre": "Prestación de Servicios",
            "tipo": "CONCEPTO",
            "alias": [
                "Prestación de Servicios"
            ]
        },
        {
            "nombre": "Salario Mínimo",
            "tipo": "CONCEPTO",
            "alias": [
                "Salario Mínimo"
            ]
        },
        {
            "nombre": "Actividades No Agrícolas",
            "tipo": "CONCEPTO",
            "alias": [
                "Actividades No Agrícolas"
            ]
        },
        {
            "nombre": "Bono",
            "tipo": "CONCEPTO",
            "alias": [
                "Bono"
            ]
        },
        {
            "nombre": "Propuesta",
            "tipo": "CONCEPTO",
            "alias": [
                "Propuesta"
            ]
        },
        {
            "nombre": "Análisis",
            "tipo": "CONCEPTO",
            "alias": [
                "Análisis"
            ]
        },
        {
            "nombre": "Fondo",
            "tipo": "CONCEPTO",
            "alias": [
                "Fondo"
            ]
        },
        {
            "nombre": "Monto",
            "tipo": "CONCEPTO",
            "alias": [
                "Monto"
            ]
        },
        {
            "nombre": "Rango",
            "tipo": "CONCEPTO",
            "alias": [
                "Rango"
            ]
        },
        {
            "nombre": "Punto Medio",
            "tipo": "CONCEPTO",
            "alias": [
                "Punto Medio"
            ]
        },
        {
            "nombre": "Cifra Promedio",
            "tipo": "CONCEPTO",
            "alias": [
                "Cifra Promedio"
            ]
        },
        {
            "nombre": "Números Gruesos",
            "tipo": "CONCEPTO",
            "alias": [
                "Números Gruesos"
            ]
        },
        {
            "nombre": "Monto Adicional",
            "tipo": "CONCEPTO",
            "alias": [
                "Monto Adicional"
            ]
        },
        {
            "nombre": "Bono Mensual",
            "tipo": "CONCEPTO",
            "alias": [
                "Bono Mensual"
            ]
        },
        {
            "nombre": "Personal de Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Personal de Salud"
            ]
        },
        {
            "nombre": "Red Hospitalaria",
            "tipo": "CONCEPTO",
            "alias": [
                "Red Hospitalaria"
            ]
        },
        {
            "nombre": "Prestación de Servicios de Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Prestación de Servicios de Salud"
            ]
        },
        {
            "nombre": "Población",
            "tipo": "CONCEPTO",
            "alias": [
                "Población"
            ]
        },
        {
            "nombre": "Servicios de Atención en Salud",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Atención en Salud"
            ]
        },
        {
            "nombre": "Servicios de Salud de Calidad",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud de Calidad"
            ]
        },
        {
            "nombre": "Servicios de Salud Dignos",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud Dignos"
            ]
        },
        {
            "nombre": "Servicios de Salud Humanos",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud Humanos"
            ]
        },
        {
            "nombre": "Servicios de Salud con Pertinencia Cultural",
            "tipo": "CONCEPTO",
            "alias": [
                "Servicios de Salud con Pertinencia Cultural"
            ]
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
            "cita": "Hablamos de un punto medio, se requeriría de cinco números gruesos, de Q463 millones adicionales. Estamos partiendo de eso, la búsqueda de ese monto, que está más o menos por ese rango de Q1 mil 800 de bono. Hay que hacer avisos, por ahí los tenemos detectados, lo tenemos que soportar",
            "emisor_nombre": "funcionario de Finanzas",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "Se continúa el análisis técnico de la propuesta de los distintos sindicatos del sector de salud, como parte de este proceso. Se trabajará en la construcción de una propuesta que sea viable y sostenible, con el objetivo de no afectar la prestación de los servicios de salud a la población",
            "emisor_nombre": "Ministerio de Salud",
            "contexto": null,
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
            "indicador": "Monto promedio del bono para trabajadores de varios renglones del Ministerio de Salud Pública",
            "categoria": "presupuestario",
            "valor_numerico": 1800,
            "unidad": "quetzales",
            "ambito_geografico": [
                "Guatemala"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Monto máximo del bono para trabajadores del renglón 0029 y subgrupo 018 del Ministerio de Salud Pública",
            "categoria": "presupuestario",
            "valor_numerico": 2000,
            "unidad": "quetzales",
            "ambito_geografico": [
                "Guatemala"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Rango de análisis de costos para el bono de los trabajadores del Ministerio de Salud Pública",
            "categoria": "presupuestario",
            "valor_numerico": 150000000,
            "unidad": "quetzales",
            "ambito_geografico": [
                "Guatemala"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Rango de análisis de costos para el bono de los trabajadores del Ministerio de Salud Pública",
            "categoria": "presupuestario",
            "valor_numerico": 200000000,
            "unidad": "quetzales",
            "ambito_geografico": [
                "Guatemala"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Monto de fondos disponibles para el Ministerio de Salud Pública",
            "categoria": "presupuestario",
            "valor_numerico": 600000000,
            "unidad": "quetzales",
            "ambito_geografico": [
                "Guatemala"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Monto adicional requerido para el bono de los trabajadores del Ministerio de Salud Pública",
            "categoria": "presupuestario",
            "valor_numerico": 463000000,
            "unidad": "quetzales",
            "ambito_geografico": [
                "Guatemala"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Monto del bono para personal de los renglones 011, 021, 022 y 031 del Ministerio de Salud Pública",
            "categoria": "presupuestario",
            "valor_numerico": 1800,
            "unidad": "quetzales",
            "ambito_geografico": [
                "Guatemala"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": null,
            "notas_contexto": null
        },
        {
            "indicador": "Monto del bono para trabajadores del renglón 0029 y subgrupo 018 del Ministerio de Salud Pública",
            "categoria": "presupuestario",
            "valor_numerico": 2000,
            "unidad": "quetzales",
            "ambito_geografico": [
                "Guatemala"
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
