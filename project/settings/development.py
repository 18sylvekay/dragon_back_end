from .base import * # noqa
import os
from pathlib import Path
import environ

BASE_DIR = Path('/var/www/dragon_back_end/')

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
SECRET_KEY = env("SECRET_KEY")

CORS_ALLOWED_ORIGINS = [f"http://*.localhost:{port}" for port in range(5173, 5184)]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
