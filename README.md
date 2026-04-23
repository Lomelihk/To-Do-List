# To-Do List

Aplicación web de gestión de tareas construida con Django 5.2. Permite a cada usuario registrado crear, editar, completar y eliminar sus propias tareas, con búsqueda en tiempo real.

## Características

- Autenticación completa: registro, inicio y cierre de sesión
- CRUD de tareas: crear, ver, editar y eliminar
- Filtrado por usuario: cada usuario solo ve sus propias tareas
- Búsqueda por título en tiempo real
- Contador de tareas pendientes en el panel principal
- Panel de administración de Django integrado

## Tecnologías

| Capa | Tecnología |
|---|---|
| Backend | Python 3 + Django 5.2 |
| Base de datos | SQLite (desarrollo) |
| Frontend | HTML5 + CSS personalizado |

## Instalación

### 1. Clonar el repositorio

```bash
git clone git@github.com:Lomelihk/To-Do-List.git
cd To-Do-List
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
# venv\Scripts\activate        # Windows

pip install -r requirements.txt
```

### 3. Aplicar migraciones

```bash
python manage.py migrate
```

### 4. Crear superusuario (opcional, para el panel admin)

```bash
python manage.py createsuperuser
```

### 5. Iniciar el servidor

```bash
python manage.py runserver
```

Abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador.

## Estructura del proyecto

```
To-Do-List/
├── base/
│   ├── models.py       # Modelo Tarea (titulo, descripcion, completo, usuario)
│   ├── views.py        # Vistas CRUD + autenticación
│   ├── urls.py         # Rutas de la app
│   ├── templates/      # Plantillas HTML
│   └── migrations/
├── proyecto/
│   ├── settings.py
│   └── urls.py
├── static/css/
│   └── style.css
├── manage.py
└── requirements.txt
```

## Modelo de datos

```python
class Tarea(models.Model):
    usuario     = ForeignKey(User)
    titulo      = CharField(max_length=200)
    descripcion = TextField(null=True, blank=True)
    completo    = BooleanField(default=False)
    creado      = DateTimeField(auto_now_add=True)
```

## Dependencias

```
Django==5.2.6
asgiref==3.9.2
sqlparse==0.5.3
tzdata==2025.2
```