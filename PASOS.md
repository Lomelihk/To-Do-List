# Pasos de Desarrollo de la Aplicación "To-Do List"

Este documento detalla los pasos seguidos para desarrollar esta aplicación de lista de tareas utilizando el framework Django.

## 1. Configuración Inicial del Proyecto

El primer paso fue crear la estructura básica del proyecto y de la aplicación principal.

1.  **Crear el Proyecto Django:** Se utilizó el comando `django-admin` para generar el esqueleto del proyecto. El `.` al final indica que se cree en el directorio actual.
    ```bash
    django-admin startproject proyecto .
    ```

2.  **Crear la Aplicación `base`:** Dentro del proyecto, se creó una aplicación llamada `base` que contendrá toda la lógica principal (modelos, vistas, etc.).
    ```bash
    python manage.py startapp base
    ```

3.  **Registrar la Aplicación:** Se añadió la nueva aplicación `base` a la lista `INSTALLED_APPS` en el archivo `proyecto/settings.py` para que Django la reconozca.
    ```python
    # proyecto/settings.py
    INSTALLED_APPS = [
        # ... apps de django
        'base.apps.BaseConfig',
    ]
    ```

## 2. Definición del Modelo de Datos

Se definió un modelo `Tarea` en `base/models.py` para representar cada tarea en la base de datos.

-   **`usuario`**: Una relación (ForeignKey) con el modelo `User` de Django para saber quién creó la tarea.
-   **`titulo`**: Un campo de texto corto para el nombre de la tarea.
-   **`descripcion`**: Un campo de texto largo para detalles adicionales.
-   **`completo`**: Un campo booleano (`True`/`False`) para marcar si la tarea ha sido completada.
-   **`creado`**: Un campo de fecha y hora que se guarda automáticamente al crear la tarea.

```python
# base/models.py
from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completo']
```

## 3. Migraciones de la Base de Datos

Una vez definido el modelo, se crearon y aplicaron las migraciones para que Django construyera la tabla correspondiente en la base de datos (SQLite por defecto).

1.  **Crear el archivo de migración:**
    ```bash
    python manage.py makemigrations
    ```
2.  **Aplicar la migración a la base de datos:**
    ```bash
    python manage.py migrate
    ```

## 4. Creación de las Vistas (Lógica)

Se utilizaron las "Class-Based Views" (Vistas Basadas en Clases) de Django para manejar la lógica de la aplicación de una manera organizada y reutilizable en `base/views.py`.

-   `ListaPendientes (ListView)`: Muestra la lista de todas las tareas.
-   `DetalleTarea (DetailView)`: Muestra los detalles de una única tarea.
-   `CrearTarea (CreateView)`: Muestra un formulario para crear una nueva tarea y la guarda.
-   `EditarTarea (UpdateView)`: Muestra un formulario para editar una tarea existente.
-   `EliminarTarea (DeleteView)`: Muestra una página de confirmación para eliminar una tarea.

## 5. Configuración de URLs

Se definieron las rutas para que cada URL se corresponda con una vista.

1.  **URLs del Proyecto:** En `proyecto/urls.py`, se incluyeron las URLs de la aplicación `base` en la ruta principal del sitio.
    ```python
    # proyecto/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('base.urls')), # Incluye las URLs de la app 'base'
    ]
    ```

2.  **URLs de la Aplicación:** En `base/urls.py`, se definió una ruta para cada vista.
    ```python
    # base/urls.py
    from django.urls import path
    from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea

    urlpatterns = [
        path('', ListaPendientes.as_view(), name='lista_pendientes'),
        path('tarea/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
        path('crear-tarea/', CrearTarea.as_view(), name='crear_tarea'),
        path('editar-tarea/<int:pk>/', EditarTarea.as_view(), name='editar_tarea'),
        path('eliminar-tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),
    ]
    ```

## 6. Creación de Plantillas (Templates)

Se crearon archivos HTML en `base/templates/base/` para renderizar la interfaz de usuario. Django, por convención, busca las plantillas de las vistas genéricas con nombres específicos.

-   `tarea_list.html`: Muestra la lista de tareas (usada por `ListaPendientes`).
-   `tarea.html`: Muestra el detalle de una tarea (usada por `DetalleTarea`).
-   `tarea_form.html`: Muestra el formulario para crear o editar una tarea (usada por `CrearTarea` y `EditarTarea`).
-   `tarea_confirm_delete.html`: Muestra el mensaje de confirmación para eliminar una tarea (usada por `EliminarTarea`).

## 7. Registro en el Panel de Administración

Para poder gestionar las tareas fácilmente desde el panel de administrador de Django, se registró el modelo `Tarea` en el archivo `base/admin.py`.

```python
# base/admin.py
from django.contrib import admin
from .models import Tarea

admin.site.register(Tarea)
```

## 8. Dependencias del Proyecto

Las librerías de Python necesarias para este proyecto se listan en `requirements.txt`. La principal dependencia es Django.

-   `asgiref`
-   `Django`
-   `sqlparse`
-   `tzdata`
