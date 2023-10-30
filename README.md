# Henry_Steam_API

## Descripción

El proyecto **Henry_Steam_API** es una API construida con [FastAPI](https://fastapi.tiangolo.com/) en Python 3.9 que proporciona una interfaz para consultar información sobre usuarios y juegos de la plataforma Steam. Esta API se basa en datos almacenados en dataframes de Pandas y utiliza un modelo de Machine Learning para el endpoint de recomendación de juegos.

## Endpoints y Ejemplos de Uso

La API proporciona varios endpoints para consultar información. A continuación, se detallan los principales endpoints junto con ejemplos de cómo utilizarlos:

### 1. GET /api/v1/developers/top3/

- **Descripción**: Devuelve el top 3 de desarrolladores de juegos para un año específico.
- **Uso**: Ejemplo: `GET /api/v1/developers/top3/2023`

### 2. GET /api/v1/developers//sentiment

- **Descripción**: Devuelve la cantidad de comentarios positivos y negativos para una desarrolladora específica.
- **Uso**: Ejemplo: `GET /api/v1/developers/Valve/sentiment`

### 3. GET /api/v1/developers//history

- **Descripción**: Para una desarrolladora determinada, retorna la cantidad de juegos gratuitos y la cantidad total de juegos por año.
- **Uso**: Ejemplo: `GET /api/v1/developers/Valve/history`

### 4. GET /api/v1/genres//users/top

- **Descripción**: Para un género de juego específico, retorna el usuario con más horas jugadas y una lista de horas jugadas por año.
- **Uso**: Ejemplo: `GET /api/v1/genres/action/users/top`

### 5. GET /api/v1/users/

- **Descripción**: Para un usuario específico, retorna la cantidad de juegos que posee, la cantidad de dinero gastado en Steam y el porcentaje de reseñas realizadas.
- **Uso**: Ejemplo: `GET /api/v1/users/123456`

### 6. GET /api/v1/games//suggest

- **Descripción**: Para un juego específico, retorna una lista de los 5 juegos recomendados en base a ese juego utilizando un modelo de Machine Learning basado en la similitud de coseno.
- **Uso**: Ejemplo: `GET /api/v1/games/7890/suggest`

## Configuración y Uso

1. **Requisitos previos**:

   - Asegúrese de tener Python 3.9 instalado.
   - Instale las dependencias requeridas utilizando `pip`:
     ```
     pip install -r requirements.txt
     ```
2. **Configuración de Docker**

   El proyecto se puede ejecutar en contenedores Docker. Asegúrese de tener los siguientes requisitos:

   - Docker: [Instrucciones de instalación](https://docs.docker.com/get-docker/)
   - Docker Compose: [Instrucciones de instalación](https://docs.docker.com/compose/install/)
3. **Configuración de los dataframes**:

   - Los dataframes de Pandas con los datos necesarios se encuentran en la carpeta "{url_drive}".
   - Asegúrese de tener acceso a estos dataframes y que estén cargados correctamente en el proyecto.
4. **Ejecución de la API**:

   - Ejecute la API utilizando el siguiente comando:

     ```
     uvicorn main:app --host 0.0.0.0 --port 8000 --reload
     ```

     La API estará disponible en `http://localhost:8000`.
5. **Disponibilidad en Render**

   - La API también está disponible en Render en la siguiente URL: [https://henry-steam-api.onrender.com](https://henry-steam-api.onrender.com).
   - Puedes acceder a la documentación de Swagger en: [https://henry-steam-api.onrender.com/docs](https://henry-steam-api.onrender.com/docs)

## Configuración de Docker

El proyecto contiene un Dockerfile que permite empaquetar la aplicación en un contenedor Docker. Además, hay un archivo `docker-compose.yml` para ejecutar la aplicación localmente en el puerto 5000.

### Uso de Docker

1. Asegúrese de tener Docker instalado en su sistema.
2. Construya la imagen de Docker usando el Dockerfile:
   `docker build -t henry-steam-api .`
3. Ejecute el contenedor utilizando la imagen construida:

```bash
docker run -p 5000:5000 henry-steam-api
```

La API estará disponible en `http://localhost:5000`.

### Docker Compose

El proyecto también incluye un archivo `docker-compose.yml` que simplifica la ejecución de la aplicación en Docker. Para ejecutarlo, utilice el siguiente comando:

```bash
docker-compose up
```

La API estará disponible en `http://localhost:5000`.

### Imagen de DockerHub

También puede ejecutar el proyecto utilizando la imagen de DockerHub `melisaarce/henry-steam-api:latest`. Para hacerlo, ejecute el siguiente comando:

```bash
docker run -p 5000:5000 melisaarce/henry-steam-api:latest
```
