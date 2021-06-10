# Data Project 4

## Pasos a seguir para lanzar el servicio

- Lanzar el archivo docker-compose.yml:
    ```
    docker-compose up -d
    ```

- Lanzar el servicio app.py dentro de la carpeta team_frontend:

    - Crear entorno virtual e instalar requirements:
        ```
        python3 -m venv venv
        source venv/bin/activate
        pip install -r ./team_frontend/requirements.txt
        ```

    - Ejecutar app.py
        ```
        python3 ./team_frontend/app.py
        ```
