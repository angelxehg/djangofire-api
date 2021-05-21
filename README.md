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

## Uso de JWT de Firebase (Solo producción)

Es necesario obtener el archivo .json de cuenta de servicio en `Configuración > Cuentas de servicio` de la consola de Firebase. *Se debe resguardar este archivo, ya que no se puede recuperar*. Posteriormente se deben extraer algunos valores y ser usados como variables de entorno:

```env
FIREBASE_PROJECT_ID=
FIREBASE_PRIVATE_KEY_ID=
FIREBASE_PRIVATE_KEY=
FIREBASE_CLIENT_EMAIL=
FIREBASE_CLIENT_ID=
FIREBASE_CLIENT_X509_URL=
```

NOTA: Estos valores solo son cargados mediante el archivo production.py, por lo que los tokens JWT de Firebase no funcionarán en el entorno de desarrollo por defecto.

## Despliegue en Heroku

Para instalar en Heroku ejecute los siguientes comandos:

- Crear aplicación en Heroku: `heroku create`

- Configurar variables de entorno:

```bash
heroku config:set SECRET_KEY="[SECRET_KEY]"
heroku config:set HOST="[Heroku URL]"
heroku config:set FIREBASE_PROJECT_ID="[VALOR]"
heroku config:set FIREBASE_PRIVATE_KEY_ID="[VALOR]"
heroku config:set FIREBASE_PRIVATE_KEY="[VALOR]"
heroku config:set FIREBASE_CLIENT_EMAIL="[VALOR]"
heroku config:set FIREBASE_CLIENT_ID="[VALOR]"
heroku config:set FIREBASE_CLIENT_X509_URL="[VALOR]"
```

- Configurar production settings: `heroku config:set DJANGO_SETTINGS_MODULE=djangofire.production`

- Hacer Git Push a Heroku: `git push heroku main`

- Crear un super usuario: `heroku run python manage.py createsuperuser`
