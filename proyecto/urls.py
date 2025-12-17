"""
Configuración de URL para el proyecto.

Este archivo es el enrutador principal del proyecto Django. Django examina la lista `urlpatterns`
para determinar a qué vista o enrutador secundario debe dirigir una solicitud de URL.
"""
# --- Importaciones Necesarias ---
from django.contrib import admin  # Importa el sitio de administración de Django.
from django.urls import path, include  # 'path' para definir rutas, 'include' para incluir otros archivos de configuración de URL.

# --- Lista Principal de Patrones de URL ---
urlpatterns = [
    # 1. Ruta para el Panel de Administración de Django.
    # Cualquier URL que comience con 'admin/' será manejada por el sitio de administración de Django.
    path('admin/', admin.site.urls),

    # 2. Ruta para la aplicación 'base'.
    # Se utiliza 'include()' para delegar el manejo de las URLs a otro archivo.
    # En este caso, cualquier URL que llegue a la raíz ('') será enviada al archivo 'urls.py'
    # de la aplicación 'base' para que sea procesada allí.
    path('', include('base.urls')),
]
