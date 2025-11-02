# --- Importaciones Necesarias ---
from django.contrib import admin  # Importa el framework del panel de administración.
from .models import Tarea  # Importa el modelo 'Tarea' desde el archivo models.py de la misma aplicación.

# --- Registro de Modelos ---
# Para que un modelo aparezca y sea gestionable en el panel de administración de Django,
# debe ser registrado aquí.

# La siguiente línea le dice a Django que cree una interfaz en el panel de administración para el modelo 'Tarea'.
admin.site.register(Tarea)
