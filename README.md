# 🐾 TaskPet Backend

API REST para TaskPet, construida con Django REST Framework y MariaDB, pensada como la base de sincronización multi-dispositivo (escritorio y, a futuro, móvil) del ecosistema TaskPet.

Repositorio del cliente de escritorio (Electron): [TaskPet](https://github.com/Jonnmp/TaskPet)

## 🛠️ Stack

- Django 5.1 + Django REST Framework
- MariaDB 11
- Docker / docker-compose
- Autenticación JWT (`djangorestframework-simplejwt`)

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Jonnmp/TaskPet_Backend.git
   cd TaskPet_Backend
   ```

2. Copia la plantilla de variables de entorno y complétala con tus propios valores:
   ```bash
   cp .env.example .env
   ```
   Genera una `SECRET_KEY` real con:
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(50))"
   ```

3. Levanta los servicios (Django + MariaDB):
   ```bash
   docker compose up
   ```

4. En otra terminal, aplica las migraciones y crea un superusuario:
   ```bash
   docker compose run --rm web python manage.py migrate
   docker compose run --rm web python manage.py createsuperuser
   ```

5. Accede al panel de administración en `http://localhost:8000/admin/`

## 📁 Estructura

```
TaskPet_Backend/
├── config/
│   └── settings/
│       ├── base.py     # configuración compartida
│       ├── dev.py       # desarrollo local
│       └── prod.py      # producción (DEBUG=False, HTTPS forzado)
└── apps/
    ├── users/            # modelo de usuario personalizado
    ├── tasks/             # API de tareas
    └── petstats/          # estadísticas de la mascota
```

## 🔌 Endpoints principales

| Método | Ruta                   | Descripción                          |
|--------|------------------------|---------------------------------------|
| POST   | `/api/token/`           | Login — devuelve `access` y `refresh` |
| POST   | `/api/token/refresh/`   | Renueva el `access` token             |
| GET    | `/api/tasks/`           | Lista las tareas del usuario autenticado |
| POST   | `/api/tasks/`           | Crea una tarea nueva                  |
| GET/PATCH/DELETE | `/api/tasks/{id}/` | Detalle, edición o borrado de una tarea propia |

Todas las rutas de `/api/tasks/` requieren el header `Authorization: Bearer <access_token>`.

## 🔐 Consideraciones de seguridad implementadas

- **Filtrado por usuario en cada consulta** (`get_queryset`), previniendo IDOR (acceso a recursos ajenos vía manipulación de IDs).
- **Campo `user` excluido del serializer**, asignado únicamente del lado del servidor (`request.user`), previniendo mass assignment.
- **Tokens JWT de vida corta** (15 min access / 7 días refresh, con rotación y blacklist), reduciendo la ventana de explotación ante un token robado.
- **Rate limiting** en endpoints anónimos (login) para mitigar fuerza bruta.
- **Validadores de contraseña** (longitud mínima, no comunes, no numéricas).
- **Separación `dev`/`prod`** de configuración: `DEBUG=False`, HTTPS forzado y cookies seguras en producción.
- **Secretos fuera del código**: `SECRET_KEY` y credenciales de base de datos viven en `.env`, nunca en el repositorio.

## 🗺️ Próximos pasos

- [ ] Refactorizar el cliente Electron (`TaskManager.js`) para consumir esta API en vez de `tasks-data.json` local
- [ ] Integrar la API oficial de Moodle (Web Services) para detectar entregas automáticamente
- [ ] Bóveda de credenciales para tokens de terceros (Moodle), cifrada con AES-256
- [ ] Gamificación de `PetStats` basada en tiempo real del servidor

## 📄 Licencia

ISC