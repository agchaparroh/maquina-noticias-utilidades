# Contexto para Claude Code - Proyecto Máquina de Noticias (Utilidades Benchmark)

Hola Claude, este archivo contiene información esencial para ayudarte a trabajar en este proyecto.

**NOTA IMPORTANTE**: En ocasiones puedo referirme a este archivo como "CONTEXT.md", pero siempre estaré hablando de este archivo "CLAUDE.md".

**1. Objetivo Actual:**

*   Estamos realizando **experimentos iterativos** para **optimizar los prompts** de extracción de información (relevancia, hechos, entidades, citas, datos) utilizando la API de Groq.
*   Trabajamos con una **muestra reducida de artículos** (definida en cada ejecución) para agilizar las pruebas.
*   Tenemos dos tipos de scripts principales:
    *   `benchmark_utils/run_experiment.py`: Script original para experimentos de un solo prompt.
    *   `benchmark_utils/run_pipeline_experiment.py`: **NUEVO** script para experimentos con pipeline multi-prompt.
*   Los prompts se almacenan como plantillas en:
    *   `benchmark_utils/prompt_templates/`: Para experimentos originales.
    *   `benchmark_utils/prompt_templates_pipeline/`: **NUEVO** directorio para los prompts del pipeline.
*   Los resultados de cada experimento se guardan en carpetas separadas dentro de `benchmark_utils/experiments/`.

**2. Acceso a GitHub:**

*   **¡SÍ tienes acceso a este repositorio en GitHub!** Se configuró una clave SSH para ti.
*   **Nombre de la Clave:** "Claude Code Server"
*   **Huella Digital (Fingerprint):** SHA256:Mri4Ms72KjVVjVC17N72KBTJe5QKi57IWncGef1DTkI
*   **Fecha de Adición:** 21 de abril (aproximadamente).
*   **Repositorio:** `agchaparroh/maquina-noticias-utilidades` (Reemplaza con tu usuario/repo real)
*   **Puedes usar comandos `git` como `git pull`, `git add`, `git commit`, `git push` directamente.** Si encuentras algún problema de permisos, avísame, pero la configuración debería estar activa.

**3. API Key de Groq:**

*   **¡IMPORTANTE!** Para ejecutar los scripts que llaman a la API de Groq (`run_experiment.py`), necesitas la API Key.
*   **La clave es:** `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`
*   **Cómo usarla:** Debes **prefijar el comando de ejecución del script** con la variable de entorno, así:
    ```bash
    GROQ_API_KEY='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' python3 benchmark_utils/run_experiment.py [argumentos...]
    ```
*   **Seguridad:** Sé que incluir la clave aquí no es ideal, pero es necesario para evitar tener que proporcionártela en cada sesión. Por favor, no expongas esta clave en logs públicos o respuestas fuera de este contexto.

**4. Estructura del Directorio Principal (`/home/ubuntu/`):**

*   `benchmark_utils/`: Contiene los scripts de prueba y resultados.
    *   `run_experiment.py`: Script principal actual para pruebas.
    *   `prompt_templates/`: Plantillas de prompts editables.
    *   `experiments/`: Directorio donde se guardan los resultados de cada experimento (subcarpetas por ID).
    *   `../data/benchmark_test_set/`: Ubicación de los archivos `test_XXX.json` originales.
*   (Otros archivos/directorios del proyecto principal si existen)

**5. Comandos Comunes:**

*   Navegar al directorio de trabajo: `cd /home/ubuntu/benchmark_utils`
*   Actualizar desde GitHub: `git pull origin main`
*   Ejecutar un experimento: `GROQ_API_KEY='...' python3 run_experiment.py --exp-id ... --articles ...`
*   Listar resultados de un experimento: `ls -l experiments/<exp_id>/`
*   Subir resultados a GitHub:
    ```bash
    git add experiments/<exp_id>/
    git commit -m "Resultados experimento <exp_id>: [breve descripción]"
    git push origin main
    ```

**Por favor, revisa este archivo al inicio de nuestra sesión si tienes dudas sobre el contexto o tus capacidades.** 

También **puedes y debes actualizar este documento con cada cambio significativo en tu estructura o en el proyecto**

¡Gracias!