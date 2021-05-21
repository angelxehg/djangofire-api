from .settings import *

import os
import django_heroku

# Usar SECRET_KEY desde Heroku enviroment values
SECRET_KEY = os.environ['SECRET_KEY']
# Desactivar modo debug
DEBUG = os.getenv('DJANGO_DEBUG', 'FALSE') == 'TRUE'
# Permitir Host de Heroku enviroment values
ALLOWED_HOSTS = [os.environ['HOST']]

# Activar Firebase JWT
INSTALLED_APPS = INSTALLED_APPS + [
    'drf_firebase_auth'
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'drf_firebase_auth.authentication.FirebaseAuthentication',
    ),
}
# Configurar Firebase JWT
DRF_FIREBASE_AUTH = {
    # allow anonymous requests without Authorization header set
    'ALLOW_ANONYMOUS_REQUESTS': os.getenv('ALLOW_ANONYMOUS_REQUESTS', False),
    # allow creation of new local user in db
    'FIREBASE_CREATE_LOCAL_USER': os.getenv('FIREBASE_CREATE_LOCAL_USER', True),
    # attempt to split firebase user.display_name and set local user
    # first_name and last_name
    'FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME': os.getenv('FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME', True),
    # commonly JWT or Bearer (e.g. JWT <token>)
    'FIREBASE_AUTH_HEADER_PREFIX': os.getenv('FIREBASE_AUTH_HEADER_PREFIX', 'Bearer'),
    # verify that JWT has not been revoked
    'FIREBASE_CHECK_JWT_REVOKED': os.getenv('FIREBASE_CHECK_JWT_REVOKED', True),
    # require that firebase user.email_verified is True
    'FIREBASE_AUTH_EMAIL_VERIFICATION': os.getenv('FIREBASE_AUTH_EMAIL_VERIFICATION', False),
    # secrets of firebase
    'FIREBASE_SERVICE_ACCOUNT_KEY': {
        "type": "service_account",
        "project_id": os.getenv('FIREBASE_PROJECT_ID', ''),
        "private_key_id": os.getenv('FIREBASE_PRIVATE_KEY_ID', ''),
        "private_key": os.getenv('FIREBASE_PRIVATE_KEY', '').replace('\\n', '\n'),
        "client_email": os.getenv('FIREBASE_CLIENT_EMAIL', ''),
        "client_id": os.getenv('FIREBASE_CLIENT_ID', ''),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.getenv('FIREBASE_CLIENT_X509_URL', ''),
    }
}

# Activar paquete Django-Heroku.
django_heroku.settings(locals())
