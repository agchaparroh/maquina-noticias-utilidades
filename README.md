# Máquina de Noticias - Utilidades de Benchmark

Este repositorio contiene herramientas para evaluar y optimizar la extracción de información estructurada de artículos periodísticos utilizando modelos de lenguaje de Groq.

## Estructura del Repositorio

```
/
├── scripts/                     # Scripts principales para ejecutar experimentos
│   ├── run_experiment.py        # Script para experimentos con prompts individuales
│   └── run_pipeline_experiment.py # Script para experimentos con pipeline multi-prompt
│
├── prompts/                     # Plantillas de prompts para los modelos
│   ├── single_prompt/           # Prompts para extracción en una sola llamada al modelo
│   │   ├── relevancia.txt
│   │   ├── extraccion_hechos.txt
│   │   ├── extraccion_entidades.txt
│   │   ├── extraccion_citas.txt
│   │   └── extraccion_datos.txt
│   │
│   └── pipeline/                # Prompts para el pipeline multi-paso
│       ├── prompt_0_filtrado.txt
│       ├── prompt_1_elementos_basicos.txt
│       ├── prompt_2_citas_datos.txt
│       ├── prompt_3_relaciones.txt
│       └── prompt_4_json_final.txt
│
├── experiments/                 # Resultados de los experimentos
│   ├── exp_01_llama3.1_baseline/  # Experimento base con prompts individuales
│   │   ├── informe_exp_01_llama3.1_baseline.md
│   │   └── metricas_exp_01_llama3.1_baseline.csv
│   │
│   └── exp_02_pipeline_llama3-8b/ # Experimento con pipeline multi-prompt
│       ├── informe_exp_02_pipeline_llama3-8b.md
│       ├── metricas_exp_02_pipeline_llama3-8b.csv
│       └── raw_outputs/         # Salidas detalladas por artículo y paso
│
├── CLAUDE.md                    # Instrucciones y contexto para Claude Code
└── README.md                    # Este archivo
```

## Tipos de Experimentos

### 1. Experimentos con Prompts Individuales (run_experiment.py)

Ejecuta cada tarea de extracción (relevancia, hechos, entidades, citas, datos) por separado sobre los artículos.

```bash
GROQ_API_KEY='...' python3 scripts/run_experiment.py --exp-id "nombre_experimento" --articles test_001 test_002 --task relevancia --model "llama3-8b-8192"
```

### 2. Experimentos con Pipeline Multi-Prompt (run_pipeline_experiment.py)

Ejecuta un pipeline de 5 etapas donde cada paso alimenta al siguiente:
1. Filtrado de relevancia
2. Extracción de elementos básicos
3. Extracción de citas y datos
4. Análisis de relaciones
5. Generación de JSON final

```bash
GROQ_API_KEY='...' python3 scripts/run_pipeline_experiment.py --exp-id "nombre_experimento" --articles test_001 test_002 --prompt-dir "./prompts/pipeline" --model "llama3-8b-8192" --input-dir "/path/to/test/data" --output-base-dir "./experiments"
```

## Experimentos Realizados

- **exp_01_llama3.1_baseline**: Experimento base utilizando prompts individuales con el modelo llama3-8b.
- **exp_02_pipeline_llama3-8b**: Experimento con pipeline de múltiples prompts usando llama3-8b-8192.

## Requisitos

- Python 3.8+
- Groq API Key
- Bibliotecas: groq, tenacity, tqdm, asyncio