# Archivo principal de enrutamiento del proyecto Django.

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # Incluye las URLs de la aplicación 'base'
    path('', include('base.urls')),
]
