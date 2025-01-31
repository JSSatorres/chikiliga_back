# Proyecto Backend con Python: Scraper para Comunio

## INSTALAR MONGO

python -m pip install "pymongo[srv]"

## Requisitos

Primero, vamos a hacer un proyecto en Python que usará FastAPI para crear un API REST, y utilizaremos `Requests` y `BeautifulSoup` para hacer scraping a la página de Comunio. Ten en cuenta que necesitarás autenticarte para acceder a tu cuenta de Comunio, por lo que utilizaremos cookies/sesión para autenticación.

### Estructura del Proyecto

- `main.py` - Archivo principal donde correremos nuestro servidor FastAPI.
- `scraper.py` - Aquí implementaremos la lógica para hacer scraping de la página de Comunio.
- `Dockerfile` - Para empaquetar la aplicación y facilitar el despliegue.
- `requirements.txt` - Para definir las dependencias del proyecto.

### Dependencias a instalar

```bash
pip install fastapi uvicorn requests beautifulsoup4
```

### Crear y Activar un Entorno Virtual

Es recomendable usar un entorno virtual para instalar las dependencias del proyecto de forma aislada y evitar conflictos con otras instalaciones de Python en tu sistema.

#### Crear el Entorno Virtual

Desde la carpeta raíz del proyecto, ejecuta el siguiente comando para crear un entorno virtual llamado `venv`:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` que contendrá una instalación aislada de Python junto con todas las dependencias del proyecto.

#### Activar el Entorno Virtual

- **En Windows**:
  - Si estás en **PowerShell**:
    ```powershell
    .\venv\Scripts\Activate
    ```
  - Si estás en **cmd**:
    ```cmd
    venv\Scripts\activate.bat
    ```
- **En Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

Cuando el entorno esté activado, verás algo similar a `(venv)` al inicio de la línea de comandos, indicando que el entorno virtual está activo.

### Instalar las Dependencias del Proyecto

Con el entorno virtual activado, instala todas las dependencias necesarias utilizando el archivo `requirements.txt`. Desde la carpeta raíz del proyecto, ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará **FastAPI**, **Uvicorn**, **requests**, y **BeautifulSoup4**, necesarios para que el proyecto funcione correctamente.

### Ejecutar el Servidor FastAPI

Con todas las dependencias instaladas, es hora de ejecutar el servidor FastAPI utilizando **Uvicorn**. Este servidor se encargará de manejar las solicitudes HTTP y ejecutar el scraping.

Desde la carpeta donde se encuentra `main.py`, ejecuta el siguiente comando:

```bash
uvicorn main:app --reload
```

- **`main:app`**: `main` se refiere al archivo `main.py`, y `app` es la instancia de FastAPI dentro de ese archivo.
- **`--reload`**: Esto permite que el servidor se reinicie automáticamente cuando realices cambios en el código, ideal para desarrollo.

Después de ejecutar este comando, deberías ver algo como:

```
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Esto significa que el servidor está corriendo en la dirección `http://127.0.0.1:8000`.

### Verificar el Funcionamiento del Proyecto

#### Probar el Endpoint de Scraping

Para verificar que el scraper está funcionando correctamente, puedes acceder al endpoint `/scrape`:

- Abre tu navegador y visita: [http://127.0.0.1:8000/scrape](http://127.0.0.1:8000/scrape).
- Esto debería devolver una respuesta JSON con los datos que se han scrapeado desde la página de Comunio.

#### Documentación de la API con Swagger

FastAPI proporciona una interfaz de documentación automática con **Swagger UI**. Puedes acceder a ella en:

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Aquí podrás ver todos los endpoints disponibles y probarlos directamente desde el navegador.

#### Probar la Interfaz HTML (Opcional)

Si el proyecto incluye una interfaz HTML (`index.html`), puedes abrirla en tu navegador para interactuar con el servidor y ver los datos obtenidos mediante el scraping:

1. Navega al archivo `index.html` y ábrelo con tu navegador.
2. Haz clic en el botón "Obtener Datos" para obtener la información desde el servidor FastAPI.
   #   c h i k i l i g a _ b a c k 
    
    
