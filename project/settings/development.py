from .base import * # noqa

ALLOWED_HOSTS = [
    '.localhost',
]

CORS_ALLOWED_ORIGINS = [f"http://*.localhost:{port}" for port in range(5173, 5184)]
