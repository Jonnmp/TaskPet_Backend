from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Extendemos AbstractUser en vez de crear un modelo desde cero.
    Blue Team: Django maneja hasheo de contraseñas, protección contra
    timing attacks en login, y gestión segura de sesiones — reinventar
    esto manualmente es el error #1 que un Red Team explota.
    """
    pass