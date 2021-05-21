# djangofire-api

Django API REST que acepta JWT de Firebase

## Instalación

Para instalar de manera local ejecute los siguientes comandos:

- Instalar dependencias: `sudo apt install python3 python3-pip python3-virtualenv`

- Clonar el repositorio: `git clone https://github.com/angelxehg/djangofire-api`

- Crear un entorno virtual: `cd djangofire-api` y `virtualenv .venv/`

- Activar entorno virtual: `source .venv/bin/activate`

- Instalar paquetes: `pip3 install -r djangofire/requirements.txt`

- Migrar estructura base de datos: `./manage.py migrate`

- Crear un super usuario: `./manage.py createsuperuser`

- Iniciar servidor local: `./manage.py runserver`

## Despliegue en Heroku

Para instalar en Heroku ejecute los siguientes comandos:

- Crear aplicación en Heroku: `heroku create`

- Configurar variables de entorno:

```bash
heroku config:set SECRET_KEY="[SECRET_KEY]"
heroku config:set HOST="[Heroku URL]"
```

- Configurar production settings: `heroku config:set DJANGO_SETTINGS_MODULE=djangofire.production`

- Hacer Git Push a Heroku: `git push heroku main`

- Crear un super usuario: `heroku run python manage.py createsuperuser`
