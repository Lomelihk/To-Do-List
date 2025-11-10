# Pasos de Desarrollo de la Aplicación "To-Do List"

Este documento detalla los pasos seguidos para desarrollar esta aplicación de lista de tareas utilizando el framework Django.

## 1. Configuración Inicial del Proyecto

El primer paso fue crear la estructura básica del proyecto y de la aplicación principal.

1.  **Crear el Proyecto Django:** Se utilizó el comando `django-admin` para generar el esqueleto del proyecto.
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

Una vez definido el modelo, se crearon y aplicaron las migraciones para que Django construyera la tabla correspondiente en la base de datos.

1.  **Crear el archivo de migración:**
    ```bash
    python manage.py makemigrations
    ```
2.  **Aplicar la migración a la base de datos:**
    ```bash
    python manage.py migrate
    ```

## 4. Creación de las Vistas (Lógica)

Se utilizaron las "Class-Based Views" (Vistas Basadas en Clases) de Django para manejar la lógica de la aplicación en `base/views.py`.

-   `ListaPendientes (ListView)`: Muestra la lista de tareas.
-   `DetalleTarea (DetailView)`: Muestra los detalles de una única tarea.
-   `CrearTarea (CreateView)`: Muestra un formulario para crear una nueva tarea.
-   `EditarTarea (UpdateView)`: Muestra un formulario para editar una tarea existente.
-   `EliminarTarea (DeleteView)`: Muestra una página de confirmación para eliminar una tarea.

## 5. Configuración de URLs

Se definieron las rutas para que cada URL se corresponda con una vista.

1.  **URLs del Proyecto:** En `proyecto/urls.py`, se incluyeron las URLs de la aplicación `base`.
    ```python
    # proyecto/urls.py
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('base.urls')),
    ]
    ```

2.  **URLs de la Aplicación:** En `base/urls.py`, se definió una ruta para cada vista.
    ```python
    # base/urls.py
    urlpatterns = [
        path('', ListaPendientes.as_view(), name='lista_pendientes'),
        # ... otras rutas
    ]
    ```

## 6. Creación de Plantillas (Templates)

Se crearon archivos HTML en `base/templates/base/` para renderizar la interfaz de usuario.

-   `tarea_list.html`: Para la lista de tareas.
-   `tarea.html`: Para el detalle de una tarea.
-   `tarea_form.html`: Para crear o editar una tarea.
-   `tarea_confirm_delete.html`: Para confirmar la eliminación.
-   `login.html`: Para el formulario de inicio de sesión.

## 7. Registro en el Panel de Administración

Se registró el modelo `Tarea` en `base/admin.py` para poder gestionarlo desde el panel de administrador.

```python
# base/admin.py
from django.contrib import admin
from .models import Tarea

admin.site.register(Tarea)
```

## 8. Implementación de Autenticación

Se añadió la funcionalidad de inicio y cierre de sesión.

1.  **Crear Vistas de Login/Logout:** Se utilizaron las vistas integradas de Django `LoginView` y `LogoutView`.
2.  **Configurar URLs de Autenticación:** Se añadieron las rutas para `login/` y `logout/` en `base/urls.py`.
    ```python
    # base/urls.py
    from django.contrib.auth.views import LoginView, LogoutView

    urlpatterns = [
        # ...
        path('login/', LoginView.as_view(template_name='base/login.html'), name='login'),
        path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    ]
    ```
3.  **Corregir Redirección Post-Login:** Por defecto, Django redirige a `/accounts/profile/` tras un login exitoso. Para corregir el error 404, se especificó una URL de redirección en `proyecto/settings.py`.
    ```python
    # proyecto/settings.py
    LOGIN_REDIRECT_URL = '/'
    ```

## 9. Dependencias del Proyecto

Las librerías de Python necesarias para este proyecto se listan en `requirements.txt`.
```
asgiref==3.9.2
Django==5.2.6
sqlparse==0.5.3
tzdata==2025.2
```