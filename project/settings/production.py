from .base import * # noqa
import os
import environ

DIRNAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(DIRNAME)

DEBUG = False

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = [
]

CORS_ALLOWED_ORIGINS = ["capacitor://localhost", "https://localhost"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
STATIC_ROOT = BASE_DIR / 'static'
