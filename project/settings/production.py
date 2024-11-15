from .base import * # noqa
import os

DIRNAME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(DIRNAME)

DEBUG = False

ALLOWED_HOSTS = [
]

CORS_ALLOWED_ORIGINS = ["capacitor://localhost", "https://localhost"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
STATIC_ROOT = BASE_DIR / 'static'
