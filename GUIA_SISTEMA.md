# Guía del Sistema de Procesamiento de Noticias

## 1. Descripción General del Sistema

El sistema de procesamiento de noticias es una herramienta diseñada para extraer información estructurada de artículos periodísticos en español. El sistema analiza noticias, identifica elementos clave como entidades, hechos, citas y relaciones, y genera una representación estructurada en formato JSON.

### Objetivos del Sistema
- Extraer información estructurada de artículos periodísticos en español
- Identificar elementos informativos clave (entidades, hechos, citas, datos)
- Analizar relaciones entre entidades y eventos
- Generar un JSON estructurado con toda la información procesada

## 2. Estructura del Directorio

El proyecto está organizado de la siguiente manera:

```
/home/ubuntu/
├── CLAUDE.md                     # Instrucciones para Claude Code
├── maquina-noticias-utilidades/  # Repositorio principal del proyecto
│   ├── CLAUDE.md                 # Copia de instrucciones para Claude
│   ├── data/                     # Datos de artículos y resultados
│   │   └── Originales/           # 72 artículos de prueba en formato JSON
│   ├── experiments/              # Resultados de experimentos 
│   │   └── [carpetas de experimentos con informes y resultados]
│   ├── prompts/                  # Plantillas de prompts para modelos
│   │   ├── pipeline/             # Prompts para el enfoque secuencial
│   │   │   ├── prompt_0_filtrado.txt
│   │   │   ├── prompt_1_elementos_basicos.txt
│   │   │   ├── prompt_2_citas_datos.txt
│   │   │   ├── prompt_3_relaciones.txt
│   │   │   └── prompt_4_json_final.txt
│   │   └── single_prompt/        # Prompts para tareas independientes
│   │       ├── extraccion_citas.txt
│   │       ├── extraccion_datos.txt
│   │       ├── extraccion_entidades.txt
│   │       ├── extraccion_hechos.txt
│   │       └── relevancia.txt
│   └── scripts/                  # Scripts para ejecutar experimentos
│       ├── run_experiment.py     # Para enfoque single-prompt
│       └── run_pipeline_experiment.py # Para enfoque pipeline
└── data/                         # Datos originales (referenciados por los scripts)
    ├── benchmark_test_set/       # 72 artículos de prueba (originales)
    ├── noticias_procesadas/
    └── noticias_raw/
```

## 3. Enfoques de Procesamiento

### 3.1 Enfoque Single-Prompt
- Utiliza prompts independientes para diferentes tareas de extracción
- Cada prompt se encarga de una tarea específica (relevancia, hechos, entidades, etc.)
- Se ejecuta mediante el script `run_experiment.py`
- No hay dependencia entre tareas; cada prompt extrae su información independientemente

### 3.2 Enfoque Pipeline (Actual)
- Procesamiento secuencial de 5 pasos donde cada paso alimenta al siguiente
- Los pasos son:
  1. **Filtrado**: Evalúa si el artículo es relevante o debe descartarse
  2. **Elementos Básicos**: Extrae información fundamental (temas, entidades principales)
  3. **Citas y Datos**: Identifica citas textuales y datos cuantitativos
  4. **Relaciones**: Analiza conexiones entre entidades y eventos
  5. **JSON Final**: Consolida toda la información en un JSON estructurado
- Se ejecuta mediante el script `run_pipeline_experiment.py`
- Cada paso utiliza los resultados del paso anterior para mejorar su análisis

## 4. Repositorio Git y GitHub

### 4.1 Configuración del Repositorio
- **Repositorio GitHub**: `agchaparroh/maquina-noticias-utilidades`
- **Clave SSH**: Ya configurada para acceso directo
- **Working Directory**: `/home/ubuntu/maquina-noticias-utilidades`

### 4.2 Comandos Git Comunes
- Actualizar repositorio:
  ```bash
  cd /home/ubuntu/maquina-noticias-utilidades && git pull origin main
  ```
- Ver estado de cambios:
  ```bash
  cd /home/ubuntu/maquina-noticias-utilidades && git status
  ```
- Añadir cambios:
  ```bash
  cd /home/ubuntu/maquina-noticias-utilidades && git add [archivos o directorios]
  ```
- Crear un commit:
  ```bash
  cd /home/ubuntu/maquina-noticias-utilidades && git commit -m "Descripción del cambio"
  ```
- Enviar cambios a GitHub:
  ```bash
  cd /home/ubuntu/maquina-noticias-utilidades && git push origin main
  ```

## 5. Ejecución de Experimentos

### 5.1 API Key de Groq
Para ejecutar cualquier experimento, necesitas usar la API Key de Groq:
```
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
```

### 5.2 Ejecutar Experimento Pipeline
```bash
cd /home/ubuntu/maquina-noticias-utilidades
GROQ_API_KEY='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' python3 scripts/run_pipeline_experiment.py --exp-id "nombre_experimento" --articles $(seq -f "test_%03g" 1 72) --model "llama-3.1-8b-instant" --prompt-dir prompts/pipeline
```

Parámetros principales:
- `--exp-id`: Identificador único del experimento
- `--articles`: Lista de IDs de artículos a procesar (o secuencia)
- `--model`: Modelo de LLM a utilizar
- `--prompt-dir`: Directorio con plantillas de prompts

### 5.3 Ejecutar Experimento Single-Prompt
```bash
cd /home/ubuntu/maquina-noticias-utilidades
GROQ_API_KEY='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' python3 scripts/run_experiment.py --exp-id "nombre_experimento" --articles $(seq -f "test_%03g" 1 72) --model "llama-3.1-8b-instant" --prompt-dir prompts/single_prompt
```

### 5.4 Modelos Disponibles
- `llama-3.1-8b-instant`: Modelo actual de preferencia (más rápido)
- `llama3-8b-8192`: Versión estándar de Llama 3 (8B parámetros)
- `llama-3.3-70b-versatile`: Modelo más potente pero más lento
- `gemma2-9b-it`: Alternativa de Google
- `qwen-qwq-32b`: Alternativa de Alibaba

## 6. Revisión de Resultados

### 6.1 Estructura de Resultados
Los resultados se guardan en la carpeta `experiments/[nombre_experimento]/` e incluyen:
- `metricas_[nombre_experimento].csv`: Métricas de rendimiento del modelo
- `informe_[nombre_experimento].md`: Informe detallado con resultados
- `raw_outputs/`: Carpeta con las salidas JSON crudas por artículo y paso

### 6.2 Comandos para Revisar Resultados
```bash
# Listar experimentos
ls -la /home/ubuntu/maquina-noticias-utilidades/experiments/

# Ver informe de un experimento en particular
cat /home/ubuntu/maquina-noticias-utilidades/experiments/[nombre_experimento]/informe_[nombre_experimento].md

# Ver métricas
cat /home/ubuntu/maquina-noticias-utilidades/experiments/[nombre_experimento]/metricas_[nombre_experimento].csv
```

## 7. Trabajando con Claude Code

Claude Code es una herramienta poderosa para interactuar con el sistema de forma interactiva. Aquí hay algunos comandos útiles:

### 7.1 Comandos de Navegación y Búsqueda
```
# Ver archivos en un directorio
ls -la /ruta/del/directorio

# Buscar archivos por patrón de nombre
find /home/ubuntu -name "*.json"

# Buscar texto dentro de archivos
grep -r "texto a buscar" /home/ubuntu/maquina-noticias-utilidades/
```

### 7.2 Operaciones con Archivos
```
# Ver contenido de un archivo
cat /ruta/del/archivo.txt

# Crear un nuevo archivo
echo "contenido" > /ruta/nuevo_archivo.txt

# Copiar archivos
cp /origen/archivo.txt /destino/archivo.txt

# Mover o renombrar archivos
mv /origen/archivo.txt /destino/nuevo_nombre.txt

# Eliminar archivos
rm /ruta/archivo.txt
```

### 7.3 Operaciones con Directorios
```
# Crear un directorio
mkdir /ruta/nuevo_directorio

# Eliminar un directorio vacío
rmdir /ruta/directorio

# Eliminar un directorio y su contenido
rm -rf /ruta/directorio
```

### 7.4 Ejecución de Scripts
```
# Ejecutar un script Python
python3 /ruta/script.py

# Ejecutar con parámetros
python3 /ruta/script.py --param1 valor1 --param2 valor2
```

## 8. Próximos Pasos y Prioridades

Los próximos pasos prioritarios para el proyecto incluyen:

1. Completar la ejecución del pipeline con los 72 artículos usando el modelo `llama-3.1-8b-instant`
2. Analizar métricas de rendimiento (tiempo, tokens, tasa de éxito)
3. Revisar resultados para identificar áreas de mejora en los prompts
4. Implementar ajustes en los prompts basados en el análisis
5. Ejecutar nuevos experimentos con los prompts ajustados
6. Generar informes comparativos de rendimiento entre diferentes modelos y versiones de prompts

## 9. Solución de Problemas Comunes

### 9.1 Problemas de API
- **Error de API Key**: Verificar que se está pasando correctamente la variable de entorno `GROQ_API_KEY`
- **Rate Limit**: Espaciar las llamadas o reducir el número de artículos procesados en paralelo
- **Timeout**: Aumentar el valor del parámetro `--timeout` al ejecutar el script

### 9.2 Problemas de Archivos
- **Archivos no encontrados**: Verificar rutas absolutas y permisos
- **Errores de JSON**: Revisar la estructura de los archivos JSON de salida
- **Problemas de permisos**: Usar `chmod` para ajustar permisos si es necesario

### 9.3 Problemas de Git
- **Conflictos de merge**: Resolver manualmente cada conflicto
- **Problemas de push**: Hacer pull antes de push si hay cambios remotos
- **Cambios no guardados**: Verificar con `git status` antes de commit/push