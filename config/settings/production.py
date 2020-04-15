from .base import *  # noqa
from .base import env


ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["some_domen.com"])


BASE_URL = 'example.com'