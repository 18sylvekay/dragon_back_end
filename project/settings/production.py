from .base import * # noqa
import os
from pathlib import Path
import environ

BASE_DIR = Path('/home/kayson99/dragon_back_end/')

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [
    'kayson99.pythonanywhere.com'
]

CORS_ALLOWED_ORIGINS = ["capacitor://localhost", "https://localhost"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
STATIC_ROOT = BASE_DIR / 'static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
