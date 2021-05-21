from .settings import *

import os
import django_heroku

# Usar SECRET_KEY desde Heroku enviroment values
SECRET_KEY = os.environ['SECRET_KEY']
# Desactivar modo debug
DEBUG = os.getenv('DJANGO_DEBUG', 'FALSE') == 'TRUE'
# Permitir Host de Heroku enviroment values
ALLOWED_HOSTS = [os.environ['HOST']]

# Activar paquete Django-Heroku.
django_heroku.settings(locals())
