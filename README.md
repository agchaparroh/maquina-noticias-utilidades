# Guía Completa del Sistema de Procesamiento de Noticias

Esta guía está diseñada para usuarios sin conocimientos técnicos avanzados. Contiene toda la información necesaria para entender el proyecto, utilizar el sistema y trabajar con Claude Code.

## 1. ¿Qué es este proyecto?

Estamos desarrollando un **sistema de procesamiento de noticias** que analiza artículos periodísticos en español y extrae información estructurada de ellos. Este sistema:

- Lee artículos de noticias
- Identifica elementos importantes (personas, organizaciones, eventos, citas, datos)
- Analiza las relaciones entre estos elementos
- Organiza toda esta información en un formato estructurado (JSON)

Imagina que tienes un artículo de periódico y necesitas identificar rápidamente quién dijo qué, qué eventos ocurrieron, qué datos se mencionaron, etc. Este sistema hace ese trabajo automáticamente.

## 2. Enfoques de Procesamiento

El proyecto utiliza dos métodos diferentes para procesar artículos:

### 2.1 Enfoque "Single-Prompt" (Inicial)
- Cada tipo de información se extrae por separado
- Utiliza 5 prompts independientes para diferentes tareas:
  - Evaluación de relevancia
  - Extracción de hechos
  - Extracción de entidades (personas, organizaciones, etc.)
  - Extracción de citas
  - Extracción de datos numéricos

### 2.2 Enfoque "Pipeline" (Actual)
- Procesamiento secuencial donde cada paso alimenta al siguiente
- Tiene 5 pasos ordenados:
  1. **Filtrado**: Evalúa si el artículo es relevante o debe descartarse
  2. **Elementos Básicos**: Extrae información fundamental (temas, entidades principales)
  3. **Citas y Datos**: Identifica citas textuales y datos cuantitativos
  4. **Relaciones**: Analiza conexiones entre entidades y eventos
  5. **JSON Final**: Consolida toda la información en un formato estructurado

Actualmente, estamos enfocados en **evaluar y optimizar** el enfoque pipeline con el modelo **llama-3.1-8b-instant** procesando un conjunto de 72 artículos de prueba.

## 3. Estructura de Archivos y Carpetas

El proyecto está organizado de la siguiente manera:

```
/home/ubuntu/maquina-noticias-utilidades/  # Repositorio principal del proyecto
├── CLAUDE.md                     # Instrucciones para Claude Code (este archivo)
├── .gitignore                    # Archivo que indica a Git qué archivos ignorar
├── data/                         # Datos de artículos
│   ├── benchmark_test_set/       # 72 artículos de prueba en formato JSON (¡NO ELIMINAR!)
│   ├── noticias_procesadas/      # Artículos procesados
│   └── noticias_raw/             # Artículos sin procesar
├── experiments/                  # Resultados de experimentos 
├── prompts/                      # Plantillas para modelos de IA
│   └── pipeline/                 # Prompts para el enfoque secuencial (5 prompts)
└── scripts/                      # Scripts para ejecutar experimentos
    └── run_pipeline_experiment.py # Script principal
```

**IMPORTANTE**: Los 72 artículos de prueba en `data/benchmark_test_set/` son muy valiosos y difíciles de conseguir. Están protegidos por el sistema de control de versiones Git y no deben ser eliminados.

## 4. Herramientas y Tecnologías: Explicación para Principiantes

### 4.1 ¿Qué es Git?

Git es un sistema de control de versiones que registra los cambios en los archivos a lo largo del tiempo. Es como un historial detallado de modificaciones que permite:

- Llevar un registro de quién hizo qué cambios y cuándo
- Volver a versiones anteriores si algo sale mal
- Trabajar en paralelo con otras personas sin pisar sus cambios
- Experimentar en nuevas ramas sin afectar el trabajo principal

Piensa en Git como un "guardado automático" muy avanzado que recuerda cada versión de tus documentos y te permite volver a cualquier punto.

### 4.2 ¿Qué es GitHub?

GitHub es una plataforma web que funciona como un almacén remoto para proyectos que usan Git. Permite:

- Almacenar copias de tu proyecto en la nube (repositorios)
- Colaborar con otros desarrolladores desde cualquier lugar
- Compartir y mostrar tu código públicamente
- Gestionar contribuciones a través de "pull requests"
- Seguir problemas (issues) y planificar el trabajo

La relación entre Git y GitHub es similar a la de un procesador de texto (como Word) y un servicio de almacenamiento en la nube (como OneDrive): Git gestiona las versiones localmente, mientras que GitHub almacena y comparte estas versiones en internet.

### 4.3 ¿Qué es Claude Code?

Claude Code es una interfaz de línea de comandos que te permite interactuar con Claude, un asistente de IA desarrollado por Anthropic. Con Claude Code puedes:

- Pedir asistencia para tareas de programación
- Explorar y manipular archivos y directorios
- Ejecutar comandos como si estuvieras en una terminal
- Analizar código y solucionar problemas
- Generar nuevos códigos o modificar existentes

Claude Code combina la potencia de un modelo de lenguaje avanzado con la capacidad de interactuar directamente con tu sistema de archivos y ejecutar código.

### 4.4 ¿Qué es un Modelo de IA como Llama?

Los modelos de IA como Llama son sistemas de inteligencia artificial entrenados para comprender y generar texto. En este proyecto utilizamos varios modelos:

- **llama-3.1-8b-instant**: Modelo rápido y eficiente (preferido actualmente)
- **llama3-8b-8192**: Versión estándar con 8 mil millones de parámetros
- **llama-3.3-70b-versatile**: Modelo más potente pero más lento
- **gemma2-9b-it**: Alternativa desarrollada por Google
- **qwen-qwq-32b**: Alternativa desarrollada por Alibaba

Estos modelos funcionan como "cerebros artificiales" que procesan los artículos y extraen la información relevante.

### 4.5 ¿Qué es Groq?

Groq es una plataforma que proporciona acceso a modelos de IA a través de una API (interfaz de programación). Para usar esta API necesitas una clave (API Key), que permite a nuestros scripts comunicarse con los servidores de Groq para procesar artículos.

## 5. Cómo Interactuar con Claude Code

Claude Code entiende lenguaje natural, pero para obtener mejores resultados es útil seguir estas pautas:

### 5.1 Comandos Básicos que puedes pedirle a Claude

**Navegación y búsqueda:**
```
"Muestra los archivos en la carpeta experiments"
"Busca todos los archivos JSON en el directorio data"
"Encuentra archivos que contengan la palabra 'filtrado'"
```

**Ver y editar archivos:**
```
"Muéstrame el contenido del archivo GUIA_SISTEMA.md"
"Crea un nuevo archivo llamado mi_experimento.txt con el siguiente contenido: [contenido]"
"Modifica el archivo X para cambiar Y por Z"
```

**Ejecutar experimentos:**
```
"Ejecuta un experimento pipeline con los artículos 1 al 5 usando el modelo llama-3.1-8b-instant"
"Analiza los resultados del experimento exp_pipeline_llama_72"
```

**Gestión de Git y GitHub:**
```
"Actualiza el repositorio desde GitHub"
"Guarda los cambios del experimento X en GitHub"
"Muestra los cambios pendientes de guardar"
```

### 5.2 Consejos para comunicarte eficazmente con Claude Code

1. **Sé específico**: Menciona nombres de archivos y rutas exactas cuando sea posible
2. **Una tarea a la vez**: Aunque Claude puede manejar instrucciones complejas, es mejor dividir tareas grandes en pasos más pequeños
3. **Proporciona contexto**: Explica brevemente qué estás intentando lograr
4. **Pide explicaciones**: Si no entiendes algo, pide a Claude que lo explique de manera más sencilla
5. **Usa comillas** para indicar texto exacto que quieres buscar o crear

## 6. Comandos Comunes y Cómo Usarlos

### 6.1 Actualizar el Repositorio

Para obtener la última versión del proyecto desde GitHub:

```
"Claude, actualiza el repositorio desde GitHub"
```

Claude ejecutará:
```bash
cd /home/ubuntu/maquina-noticias-utilidades && git pull origin main
```

### 6.2 Ejecutar un Experimento Pipeline

Para procesar artículos con el enfoque pipeline:

```
"Claude, ejecuta un experimento pipeline con los artículos 1 al 10 usando el modelo llama-3.1-8b-instant, nombra el experimento 'mi_prueba_pipeline'"
```

Claude ejecutará algo similar a:
```bash
cd /home/ubuntu/maquina-noticias-utilidades
GROQ_API_KEY='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' python3 scripts/run_pipeline_experiment.py --exp-id "mi_prueba_pipeline" --articles $(seq -f "test_%03g" 1 10) --model "llama-3.1-8b-instant" --prompt-dir prompts/pipeline
```

### 6.3 Ver Resultados de un Experimento

Para revisar los resultados:

```
"Claude, muéstrame los resultados del experimento 'mi_prueba_pipeline'"
```

Claude te mostrará los archivos disponibles y podrá analizar el informe para ti.

### 6.4 Guardar Resultados en GitHub

Para guardar los resultados en GitHub:

```
"Claude, guarda los resultados del experimento 'mi_prueba_pipeline' en GitHub con un mensaje que describa el experimento"
```

Claude ejecutará:
```bash
cd /home/ubuntu/maquina-noticias-utilidades
git add experiments/mi_prueba_pipeline/
git commit -m "Resultados del experimento pipeline con artículos 1-10 usando llama-3.1-8b-instant"
git push origin main
```

## 7. Parámetros y Opciones Importantes

### 7.1 Para Experimentos Pipeline

- **--exp-id**: Nombre único para identificar el experimento
- **--articles**: Lista de IDs de artículos a procesar (puedes usar `$(seq -f "test_%03g" 1 72)` para todos)
- **--model**: Modelo de IA a utilizar (por defecto "llama-3.1-8b-instant")
- **--prompt-dir**: Carpeta con los archivos de prompts (normalmente "prompts/pipeline")
- **--temperature**: Controla la creatividad del modelo (0.2 por defecto, valores más bajos son más deterministas)
- **--max-tokens**: Máxima longitud de respuesta (4096 por defecto)

### 7.2 Modelos Disponibles (de más rápido a más potente)

- **llama-3.1-8b-instant**: Modelo rápido, buena relación velocidad/calidad (recomendado)
- **llama3-8b-8192**: Balance entre velocidad y capacidad
- **gemma2-9b-it**: Alternativa de Google, rendimiento medio
- **qwen-qwq-32b**: Modelo de mayor capacidad, más lento
- **llama-3.3-70b-versatile**: El modelo más potente pero significativamente más lento

## 8. Trabajando con Archivos y Directorios

Para que Claude Code te ayude con archivos y directorios, puedes pedirle:

### 8.1 Explorar Contenido
```
"Muéstrame qué hay en la carpeta prompts/pipeline"
"Listar todos los experimentos ordenados por fecha"
```

### 8.2 Ver Archivos
```
"Abre el archivo prompts/pipeline/prompt_0_filtrado.txt"
"Muéstrame el informe del último experimento"
```

### 8.3 Crear y Modificar
```
"Crea una carpeta llamada 'mi_nuevo_experimento'"
"Crea un archivo nuevo con este contenido: [contenido]"
"Modifica el archivo X para corregir Y"
```

### 8.4 Copiar y Mover
```
"Copia el archivo X a la carpeta Y"
"Mueve todos los archivos JSON de la carpeta X a Y"
```

## 9. Solución de Problemas Comunes

### 9.1 Problemas de API
- **Error de API Key**: "Claude, verifica si la API Key de Groq está configurada correctamente"
- **Lentitud o timeout**: "Claude, ejecuta el experimento con menos artículos" o "aumenta el timeout a 300 segundos"

### 9.2 Problemas de Archivos
- **Archivo no encontrado**: "Claude, busca dónde está el archivo X" o "verifica si la ruta es correcta"
- **Errores de JSON**: "Claude, analiza el archivo JSON para encontrar errores de formato"

### 9.3 Problemas de Git
- **Conflictos**: "Claude, muéstrame los conflictos en el repositorio y ayúdame a resolverlos"
- **Push rechazado**: "Claude, actualiza el repositorio antes de intentar subir cambios"
- **Archivos ignorados**: "Claude, el archivo X no aparece en Git". Verifica si está en .gitignore

### 9.4 Sobre el Archivo .gitignore

El archivo `.gitignore` en la raíz del repositorio define qué archivos serán ignorados por Git:

- **Archivos de Python**: `__pycache__/`, `*.pyc`, etc.
- **Archivos temporales**: `*.tmp`, `*.log`, etc.
- **Resultados de experimentos**: Si contienen mucho volumen de datos

Los 72 artículos de prueba NO están ignorados en Git, lo que garantiza su preservación en el repositorio.

## 10. Próximos Pasos del Proyecto

Actualmente, nuestras prioridades son:

1. Completar la ejecución del pipeline con los 72 artículos usando llama-3.1-8b-instant
2. Analizar métricas de rendimiento (tiempo, tokens, tasa de éxito)
3. Revisar los resultados para identificar áreas de mejora en los prompts
4. Implementar ajustes en los prompts basados en el análisis
5. Ejecutar nuevos experimentos comparativos entre diferentes modelos

## 11. Cómo Puedes Contribuir

Aunque no necesitas conocimientos técnicos avanzados, puedes ayudar de varias formas:

1. **Revisar resultados**: Analizar si la información extraída es correcta y completa
2. **Sugerir mejoras**: Proponer cambios en los prompts o el flujo de trabajo
3. **Probar diferentes modelos**: Ejecutar experimentos con distintos modelos y comparar
4. **Documentar hallazgos**: Mantener actualizada esta guía con nuevos descubrimientos

Recuerda que Claude Code está aquí para ayudarte con las partes técnicas, así que no dudes en preguntar o pedir asistencia en cualquier momento.

---

**Nota importante**: Este documento se actualiza continuamente. Por favor, revísalo al inicio de cada sesión de trabajo y actualízalo cuando hagas cambios significativos al proyecto.