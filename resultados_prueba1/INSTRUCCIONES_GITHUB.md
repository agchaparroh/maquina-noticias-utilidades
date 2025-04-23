# Instrucciones para subir a GitHub

Para subir estos resultados a GitHub, sigue estos pasos:

1. Crea un nuevo repositorio en GitHub (por ejemplo, "resultados-benchmark-noticias" o el nombre que prefieras)

2. Configura el repositorio remoto con el comando:
```bash
git remote add origin https://github.com/agchaparroh/nombre-del-repositorio.git
```

3. Sube los cambios al repositorio remoto:
```bash
git push -u origin master
```

Si prefieres usar la rama principal "main" en lugar de "master", puedes renombrar la rama:
```bash
git branch -m master main
git push -u origin main
```

## Estructura de Archivos

En este repositorio se encuentran:

- `prompt_test_results/`: Archivos JSON con resultados brutos
- `prompt_test_markdowns/`: Archivos Markdown con resultados formateados
- `consolidation_script.py`: Script utilizado para generar los reportes Markdown
- `README.md`: Descripción general del proyecto

## Nota

Si encuentras problemas con las credenciales de git, puedes configurarlas temporalmente:
```bash
git config --global user.email "tu-email@ejemplo.com"
git config --global user.name "Tu Nombre"
```

O usar tokens de acceso personal para la autenticación.