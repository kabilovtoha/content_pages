from .base import *  # noqa
from .base import env


DEBUG = True


ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1', '.ngrok.io']

BASE_URL = 'http://127.0.0.1:8000'
INSTALLED_APPS += ["django_extensions"]