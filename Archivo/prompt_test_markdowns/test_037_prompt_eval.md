# Evaluación Artículo: test_037
**Modelo Probado:** `llama-3.1-8b-instant`

## Metadatos del Artículo Original

| Campo          | Valor                                      |
|----------------|--------------------------------------------|
| **URL**        | https://www.infobae.com/america/america-latina/2025/04/15/el-gobierno-de-haiti-adopto-un-presupuesto-de-guerra-para-luchar-contra-las-pandillas/           |
| **Título**     | El gobierno de Haití adoptó un “presupuesto de guerra” para luchar contra las pandillas       |
| **Medio**      | infobae         |
| **País Pub.**  | None |
| **Fecha Pub.** | 2025-04-15T00:16:47.612000+00:00 |
| **Recopilado** | 2025-04-21T00:43:16.713782+00:00 |

---

## Contenido del Artículo Analizado

<details open>
<summary>Ver/Ocultar Contenido Completo</summary>

```text
El gobierno de Haití anunció el lunes que aprobó lo que llamó un “presupuesto de guerra” de 275.000 dólares destinado a aliviar la crisis del país ante el aumento de la violencia de pandillas.
Casi el 40% del dinero se destinará a la policía y al ejército de Haití “para combatir a los grupos armados que amenazan la estabilidad nacional”, mientras que casi el 20% se destinará a fortalecer la frontera que el país comparte con la República Dominicana, dijo el consejo presidencial de transición de Haití en un comunicado.
Otro 16% se destinará a programas sociales, incluyendo aquellos enfocados en educación, salud y asistencia humanitaria. El consejo afirmó que el presupuesto especial refleja el compromiso del estado de actuar con decisión y abordar la creciente inseguridad.
Sin embargo, no se espera que el dinero adicional alivie la falta de recursos que afecta a la misión respaldada por la ONU, liderada por la policía de Kenia, que está luchando para ayudar a las autoridades locales a sofocar la violencia de las pandillas.
Las pandillas que controlan al menos el 85% de la capital, Puerto Príncipe, continúan atacando a las comunidades que la rodean.
Recientemente, una poderosa coalición de pandillas conocida como Viv Ansanm tomó el control de las localidades de Mirebalais y Saut’d’Eau, en la región central de Haití, según la Red Nacional de Defensa de los Derechos Humanos, un grupo local. Agentes de policía de la comisaría de Mirebalais y de la prisión local huyeron durante los ataques, indicó.
“Bandas armadas incendiaron la comisaría y tomaron el control de la prisión, orquestando una fuga masiva de reclusos”, indicó la organización, señalando que en la prisión había 533 reclusos.
El personal y los pacientes del Hospital Universitario Mirebalais también fueron evacuados.
Al menos 60 personas murieron tras los ataques lanzados el 30 y 31 de marzo, incluidos pandilleros y reclusos fugados, según el grupo de derechos humanos.
Mientras tanto, la vecina ciudad de Saut-d’Eau cayó en manos de las pandillas en la tarde del 3 de abril, dijeron activistas.
“Algunos dicen que esto fue facilitado por la redistribución de las fuerzas del orden a Mirebalais, dejando a Saut-d’Eau vulnerable”, dijo el grupo la semana pasada.
Entre los muertos durante los ataques había dos monjas y un policía, mientras que dos periodistas siguen desaparecidos.
“Al ignorar el colapso de la región central, las autoridades de transición demuestran que no tienen un plan real para restaurar los derechos ciudadanos y la seguridad pública”, declaró la organización de derechos humanos. “La ausencia de respuesta estatal ha convertido a la policía en bomberos, reaccionando constantemente sin rumbo estratégico, mientras las ciudades caen una tras otra”.
El grupo señaló que civiles y grupos de autodefensa en ambas localidades “habían dado repetidas alarmas que fueron ignoradas”.
Mientras tanto, más de 260 personas murieron en otro ataque de pandillas en dos comunidades de la capital de Haití a fines de enero, según la misión política de la ONU en Haití, que cuestionó la demora en la respuesta de las autoridades .
Los ataques ocurrieron en Kenscoff y en zonas de Carrefour. Otra comunidad de Kenscoff fue atacada durante el fin de semana, con al menos un policía desaparecido y varios heridos, según SPNH-17, un sindicato policial.
En total, del 1 de enero al 27 de marzo, se ha reportado la muerte de más de 1500 personas en Haití y otras 572 resultaron heridas, según la misión de la ONU. La violencia de pandillas también ha dejado a más de un millón de personas sin hogar en los últimos años, según la ONU.
(Con información de AP)
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
    "puntuacion_relevancia": 8,
    "justificacion_relevancia": "La violencia de pandillas en Haití es un tema de gran trascendencia geopolítica",
    "categorias_asignadas": [
        "Conflicto/Seguridad",
        "Política Nacional"
    ],
    "explicacion_concisa": "El gobierno de Haití aprobó un presupuesto especial para combatir la violencia de pandillas, que controlan gran parte de la capital. El presupuesto incluye fondos para la policía, el ejército y programas sociales. La violencia ha causado muertes y daños en varias localidades."
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
            "contenido": "El gobierno de Haití aprobó un presupuesto de guerra de 275.000 dólares para luchar contra las pandillas.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-15",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "HT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "Haití",
                "pandillas",
                "presupuesto",
                "guerra"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Casi el 40% del presupuesto se destinará a la policía y al ejército de Haití para combatir a los grupos armados.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-15",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "HT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "Haití",
                "policía",
                "ejército",
                "pandillas"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Casi el 20% del presupuesto se destinará a fortalecer la frontera con la República Dominicana.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-15",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "HT",
                "DO"
            ],
            "ubicaciones_especificas": [],
            "importancia": 7,
            "confiabilidad": 5,
            "etiquetas": [
                "Haití",
                "República Dominicana",
                "frontera",
                "presupuesto"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Otro 16% del presupuesto se destinará a programas sociales, incluyendo educación, salud y asistencia humanitaria.",
            "tipo_hecho": "DECLARACION",
            "fecha_ocurrencia_inicio": "2025-04-15",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "HT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "Haití",
                "programas sociales",
                "educación",
                "salud"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Las pandillas controlan al menos el 85% de la capital, Puerto Príncipe.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-15",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "HT"
            ],
            "ubicaciones_especificas": [
                "Puerto Príncipe"
            ],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "Haití",
                "pandillas",
                "Puerto Príncipe"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Una poderosa coalición de pandillas conocida como Viv Ansanm tomó el control de las localidades de Mirebalais y Saut’d’Eau.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-15",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "exacta",
            "paises": [
                "HT"
            ],
            "ubicaciones_especificas": [
                "Mirebalais",
                "Saut’d’Eau"
            ],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "Haití",
                "pandillas",
                "Mirebalais",
                "Saut’d’Eau"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Al menos 60 personas murieron tras los ataques lanzados el 30 y 31 de marzo.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-30",
            "fecha_ocurrencia_fin": "2025-03-31",
            "precision_temporal": "dia",
            "paises": [
                "HT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 9,
            "confiabilidad": 5,
            "etiquetas": [
                "Haití",
                "ataques",
                "muertes"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La violencia de pandillas ha dejado a más de un millón de personas sin hogar en los últimos años.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-15",
            "fecha_ocurrencia_fin": null,
            "precision_temporal": "año",
            "paises": [
                "HT"
            ],
            "ubicaciones_especificas": [],
            "importancia": 8,
            "confiabilidad": 5,
            "etiquetas": [
                "Haití",
                "pandillas",
                "sin hogar"
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
            "nombre": "Gobierno de Haití",
            "tipo": "INSTITUCION",
            "alias": [
                "Gobierno de Haití"
            ]
        },
        {
            "nombre": "Haití",
            "tipo": "LUGAR",
            "alias": [
                "Haití"
            ]
        },
        {
            "nombre": "República Dominicana",
            "tipo": "LUGAR",
            "alias": [
                "República Dominicana"
            ]
        },
        {
            "nombre": "ONU",
            "tipo": "INSTITUCION",
            "alias": [
                "Organización de las Naciones Unidas"
            ]
        },
        {
            "nombre": "Policía de Kenia",
            "tipo": "INSTITUCION",
            "alias": [
                "Policía de Kenia"
            ]
        },
        {
            "nombre": "Puerto Príncipe",
            "tipo": "LUGAR",
            "alias": [
                "Puerto Príncipe"
            ]
        },
        {
            "nombre": "Mirebalais",
            "tipo": "LUGAR",
            "alias": [
                "Mirebalais"
            ]
        },
        {
            "nombre": "Saut’d’Eau",
            "tipo": "LUGAR",
            "alias": [
                "Saut’d’Eau"
            ]
        },
        {
            "nombre": "Viv Ansanm",
            "tipo": "OTRO",
            "alias": [
                "Viv Ansanm"
            ]
        },
        {
            "nombre": "Red Nacional de Defensa de los Derechos Humanos",
            "tipo": "ORGANIZACION",
            "alias": [
                "Red Nacional de Defensa de los Derechos Humanos"
            ]
        },
        {
            "nombre": "Hospital Universitario Mirebalais",
            "tipo": "LUGAR",
            "alias": [
                "Hospital Universitario Mirebalais"
            ]
        },
        {
            "nombre": "Sindicato Policial Nacional Haitiano (SPNH-17)",
            "tipo": "ORGANIZACION",
            "alias": [
                "SPNH-17"
            ]
        },
        {
            "nombre": "Misión política de la ONU en Haití",
            "tipo": "INSTITUCION",
            "alias": [
                "Misión política de la ONU en Haití"
            ]
        },
        {
            "nombre": "Caso de violencia de pandillas en Haití",
            "tipo": "EVENTO",
            "alias": [
                "Caso de violencia de pandillas en Haití"
            ]
        },
        {
            "nombre": "Elecciones en Haití",
            "tipo": "EVENTO",
            "alias": [
                "Elecciones en Haití"
            ]
        },
        {
            "nombre": "Crisis en Haití",
            "tipo": "CONCEPTO",
            "alias": [
                "Crisis en Haití"
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
            "cita": "un “presupuesto de guerra” de 275.000 dólares destinado a aliviar la crisis del país ante el aumento de la violencia de pandillas",
            "emisor_nombre": "gobierno de Haití",
            "contexto": "El gobierno de Haití anunció el lunes que aprobó lo que llamó un “presupuesto de guerra” de 275.000 dólares destinado a aliviar la crisis del país ante el aumento de la violencia de pandillas.",
            "fecha_cita": null
        },
        {
            "cita": "para combatir a los grupos armados que amenazan la estabilidad nacional",
            "emisor_nombre": "consejo presidencial de transición de Haití",
            "contexto": "Casi el 40% del dinero se destinará a la policía y al ejército de Haití “para combatir a los grupos armados que amenazan la estabilidad nacional”, mientras que casi el 20% se destinará a fortalecer la frontera que el país comparte con la República Dominicana, dijo el consejo presidencial de transición de Haití en un comunicado.",
            "fecha_cita": null
        },
        {
            "cita": "El presupuesto especial refleja el compromiso del estado de actuar con decisión y abordar la creciente inseguridad",
            "emisor_nombre": "consejo presidencial de transición de Haití",
            "contexto": "El consejo afirmó que el presupuesto especial refleja el compromiso del estado de actuar con decisión y abordar la creciente inseguridad.",
            "fecha_cita": null
        },
        {
            "cita": "Bandas armadas incendiaron la comisaría y tomaron el control de la prisión, orquestando una fuga masiva de reclusos",
            "emisor_nombre": "Red Nacional de Defensa de los Derechos Humanos",
            "contexto": "“Bandas armadas incendiaron la comisaría y tomaron el control de la prisión, orquestando una fuga masiva de reclusos”, indicó la organización, señalando que en la prisión había 533 reclusos.",
            "fecha_cita": null
        },
        {
            "cita": "Al ignorar el colapso de la región central, las autoridades de transición demuestran que no tienen un plan real para restaurar los derechos ciudadanos y la seguridad pública",
            "emisor_nombre": "Red Nacional de Defensa de los Derechos Humanos",
            "contexto": "“Al ignorar el colapso de la región central, las autoridades de transición demuestran que no tienen un plan real para restaurar los derechos ciudadanos y la seguridad pública”, declaró la organización de derechos humanos.",
            "fecha_cita": null
        },
        {
            "cita": "La ausencia de respuesta estatal ha convertido a la policía en bomberos, reaccionando constantemente sin rumbo estratégico, mientras las ciudades caen una tras otra",
            "emisor_nombre": "Red Nacional de Defensa de los Derechos Humanos",
            "contexto": "“La ausencia de respuesta estatal ha convertido a la policía en bomberos, reaccionando constantemente sin rumbo estratégico, mientras las ciudades caen una tras otra”.",
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
            "indicador": "Presupuesto asignado a la policía y el ejército de Haití",
            "categoria": "presupuestario",
            "valor_numerico": 275000,
            "unidad": "USD",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Gobierno de Haití",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje del presupuesto destinado a la policía y el ejército de Haití",
            "categoria": "presupuestario",
            "valor_numerico": 40,
            "unidad": "%",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Gobierno de Haití",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje del presupuesto destinado a fortalecer la frontera con la República Dominicana",
            "categoria": "presupuestario",
            "valor_numerico": 20,
            "unidad": "%",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Gobierno de Haití",
            "notas_contexto": null
        },
        {
            "indicador": "Porcentaje del presupuesto destinado a programas sociales",
            "categoria": "presupuestario",
            "valor_numerico": 16,
            "unidad": "%",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Gobierno de Haití",
            "notas_contexto": null
        },
        {
            "indicador": "Número de reclusos en la prisión de Mirebalais",
            "categoria": "demográfico",
            "valor_numerico": 533,
            "unidad": "personas",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "Red Nacional de Defensa de los Derechos Humanos",
            "notas_contexto": null
        },
        {
            "indicador": "Número de muertos en los ataques de pandillas en Mirebalais y Saut’d’Eau",
            "categoria": "demográfico",
            "valor_numerico": 60,
            "unidad": "personas",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": "2023-03-30",
            "periodo_referencia_fin": "2023-04-03",
            "tipo_periodo": "puntual",
            "fuente_especifica": "Red Nacional de Defensa de los Derechos Humanos",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas muertas en otro ataque de pandillas en la capital de Haití",
            "categoria": "demográfico",
            "valor_numerico": 260,
            "unidad": "personas",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": "2023-01-01",
            "periodo_referencia_fin": "2023-01-31",
            "tipo_periodo": "mensual",
            "fuente_especifica": "Misión política de la ONU en Haití",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas muertas en Haití desde enero a marzo de 2023",
            "categoria": "demográfico",
            "valor_numerico": 1500,
            "unidad": "personas",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": "2023-01-01",
            "periodo_referencia_fin": "2023-03-27",
            "tipo_periodo": "acumulado",
            "fuente_especifica": "Misión de la ONU",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas heridas en Haití desde enero a marzo de 2023",
            "categoria": "demográfico",
            "valor_numerico": 572,
            "unidad": "personas",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": "2023-01-01",
            "periodo_referencia_fin": "2023-03-27",
            "tipo_periodo": "acumulado",
            "fuente_especifica": "Misión de la ONU",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas sin hogar en Haití en los últimos años",
            "categoria": "demográfico",
            "valor_numerico": 1000000,
            "unidad": "personas",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": null,
            "periodo_referencia_fin": null,
            "tipo_periodo": null,
            "fuente_especifica": "ONU",
            "notas_contexto": null
        }
    ]
}
```
</details>
