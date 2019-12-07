import os


API_V1_STR = "/api/v1"

SECRET_KEY = os.urandom(32)

BACKEND_CORS_ORIGINS = [
    'http://localhost:8080',
]
PROJECT_NAME = 'FastAPI Skeleton'
