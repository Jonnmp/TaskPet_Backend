# prod.py
from .base import *
from decouple import config

DEBUG = False
# Evita exponer fragmentos de codigo, rutas o variables en caso de que ocurra 
# algun fallo en el sistema, evitando filtar informacion sensible

CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", default="").split(",")
# Soo autoriza peticiones de paginas alojadas en mi dominio

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# 🔵 Fuerza HTTPS y marca cookies como "solo por HTTPS" — mitiga
# ataques de interceptación en redes no confiables (ej. WiFi público).