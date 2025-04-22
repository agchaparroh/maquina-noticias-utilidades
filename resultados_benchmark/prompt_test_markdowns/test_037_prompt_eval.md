# Evaluación Artículo: test_037

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

<details>
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

## Resumen de Evaluación

| Tarea | Estado | Modelo | Tiempo | Tokens | Ratio |
|-------|--------|--------|--------|--------|-------|
| relevancia | ✅ | `llama3-8b-8192` | 0m 0.68s | 1452.0 | 0.11 |
| extraccion_hechos | ✅ | `llama3-8b-8192` | 0m 2.38s | 3459.0 | 0.34 |
| extraccion_entidades | ✅ | `llama3-8b-8192` | 0m 1.22s | 2375.0 | 0.23 |
| extraccion_citas | ✅ | `llama3-8b-8192` | 0m 1.43s | 2077.0 | 0.13 |
| extraccion_datos | ✅ | `llama3-8b-8192` | 0m 1.75s | 3183.0 | 0.35 |

---

## Resultados Detallados por Tarea

### Tarea: relevancia

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 0.68s
- **Tokens prompt:** 1303.0
- **Tokens respuesta:** 149.0
- **Total tokens:** 1452.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "puntuacion_relevancia": 7,
    "justificacion_relevancia": "La aprobación de un presupuesto de guerra para luchar contra pandillas en Haití tiene un impacto significativo en la seguridad y estabilidad del país.",
    "categorias_asignadas": [
        "Conflicto/Seguridad",
        "Política Nacional"
    ],
    "explicacion_concisa": "El gobierno de Haití aprobó un presupuesto de 275.000 dólares para combatir la violencia de pandillas y fortalecer la frontera con la República Dominicana, en un esfuerzo por abordar la creciente inseguridad en el país."
}
```
</details>


### Tarea: extraccion_hechos

✅ **Estado:** Éxito

**Métricas:**
- **Modelo:** `llama3-8b-8192`
- **Tiempo:** 0m 2.38s
- **Tokens prompt:** 2590.0
- **Tokens respuesta:** 869.0
- **Total tokens:** 3459.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "contenido": "El gobierno de Haití adoptó un 'presupuesto de guerra' para luchar contra las pandillas.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-15T00:00:00Z",
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
                "gobierno"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Casi el 40% del presupuesto se destinará a la policía y al ejército de Haití para combatir a los grupos armados.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-04-15T00:00:00Z",
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
                "ejército"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "Las pandillas que controlan al menos el 85% de la capital, Puerto Príncipe, continúan atacando a las comunidades que la rodean.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-30T00:00:00Z",
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
            "contenido": "Al menos 60 personas murieron tras los ataques lanzados el 30 y 31 de marzo, incluidos pandilleros y reclusos fugados.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-03-30T00:00:00Z",
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
                "muertes"
            ],
            "es_evento_futuro": false,
            "estado_programacion": null
        },
        {
            "contenido": "La violencia de pandillas también ha dejado a más de un millón de personas sin hogar en los últimos años, según la ONU.",
            "tipo_hecho": "SUCESO",
            "fecha_ocurrencia_inicio": "2025-01-01T00:00:00Z",
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
                "pandillas",
                "refugiados"
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
- **Tiempo:** 0m 1.22s
- **Tokens prompt:** 1925.0
- **Tokens respuesta:** 450.0
- **Total tokens:** 2375.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "nombre": "Haití",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "República Dominicana",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Organización de las Naciones Unidas (ONU)",
            "tipo": "INSTITUCION",
            "alias": [
                "ONU",
                "Naciones Unidas"
            ]
        },
        {
            "nombre": "Consejo presidencial de transición de Haití",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Policía de Kenia",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Viv Ansanm",
            "tipo": "OTRO",
            "alias": []
        },
        {
            "nombre": "Red Nacional de Defensa de los Derechos Humanos",
            "tipo": "ORGANIZACION",
            "alias": []
        },
        {
            "nombre": "Hospital Universitario Mirebalais",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Mirebalais",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Saut-d'Eau",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Kenscoff",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Carrefour",
            "tipo": "LUGAR",
            "alias": []
        },
        {
            "nombre": "Misión política de la ONU en Haití",
            "tipo": "INSTITUCION",
            "alias": []
        },
        {
            "nombre": "SPNH-17",
            "tipo": "ORGANIZACION",
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
- **Tiempo:** 0m 1.43s
- **Tokens prompt:** 1837.0
- **Tokens respuesta:** 240.0
- **Total tokens:** 2077.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "cita": "Bandas armadas incendiaron la comisaría y tomaron el control de la prisión, orquestando una fuga masiva de reclusos",
            "emisor_nombre": "Red Nacional de Defensa de los Derechos Humanos",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "Algunos dicen que esto fue facilitado por la redistribución de las fuerzas del orden a Mirebalais, dejando a Saut-d'Eau vulnerable",
            "emisor_nombre": "grupo de derechos humanos",
            "contexto": null,
            "fecha_cita": null
        },
        {
            "cita": "La ausencia de respuesta estatal ha convertido a la policía en bomberos, reaccionando constantemente sin rumbo estratégico, mientras las ciudades caen una tras otra",
            "emisor_nombre": "organización de derechos humanos",
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
- **Tiempo:** 0m 1.75s
- **Tokens prompt:** 2356.0
- **Tokens respuesta:** 827.0
- **Total tokens:** 3183.0


<details open>
<summary>Ver/Ocultar Respuesta LLM</summary>

```json
{
    "resultados": [
        {
            "indicador": "Presupuesto de guerra",
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
            "indicador": "Porcentaje de dinero destinado a la policía y el ejército",
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
            "indicador": "Porcentaje de dinero destinado a fortalecer la frontera con la República Dominicana",
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
            "indicador": "Porcentaje de dinero destinado a programas sociales",
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
            "indicador": "Número de personas muertas en ataques de pandillas",
            "categoria": "social",
            "valor_numerico": 1500,
            "unidad": "personas",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": "2023-01-01",
            "periodo_referencia_fin": "2023-03-27",
            "tipo_periodo": "período",
            "fuente_especifica": "Misión de la ONU",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas heridas en ataques de pandillas",
            "categoria": "social",
            "valor_numerico": 572,
            "unidad": "personas",
            "ambito_geografico": [
                "Haití"
            ],
            "periodo_referencia_inicio": "2023-01-01",
            "periodo_referencia_fin": "2023-03-27",
            "tipo_periodo": "período",
            "fuente_especifica": "Misión de la ONU",
            "notas_contexto": null
        },
        {
            "indicador": "Número de personas sin hogar en Haití",
            "categoria": "social",
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
