# djangofire-api

Django API REST que acepta JWT de Firebase

## Instalación

Para instalar de manera local ejecute los siguientes comandos:

- Instalar dependencias: `sudo apt install python3 python3-pip python3-virtualenv`

- Clonar el repositorio: `git clone https://github.com/angelxehg/djangofire-api`

- Crear un entorno virtual: `cd djangofire-api` y `virtualenv .venv/`

- Activar entorno virtual: `source .venv/bin/activate`

- Instalar paquetes: `pip3 install -r requirements.txt`

- Migrar estructura base de datos: `./manage.py migrate`

- Crear un super usuario: `./manage.py createsuperuser`

- Iniciar servidor local: `./manage.py runserver`
