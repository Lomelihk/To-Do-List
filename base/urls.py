# --- Importaciones Necesarias ---
from django.urls import path  # Función para definir rutas de URL.
# Importa todas las vistas que creamos en el archivo views.py para poder asignarlas a una URL.
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea

# --- Definición de Patrones de URL ---
# La variable 'urlpatterns' es una lista que Django busca para encontrar las rutas de la aplicación.
urlpatterns = [
    # path(ruta, vista, nombre)

    # Ruta para la página principal: muestra la lista de tareas.
    # - La cadena vacía '' indica la raíz de la aplicación (ej: http://localhost:8000/).
    # - 'ListaPendientes.as_view()' llama a la vista basada en clase que muestra la lista.
    # - name='lista_pendientes' es un nombre único para esta ruta, útil para crear enlaces en las plantillas.
    path('', ListaPendientes.as_view(), name='lista_pendientes'),

    # Ruta para ver el detalle de una tarea específica.
    # - 'tarea/<int:pk>/' define una URL dinámica. '<int:pk>' captura un entero de la URL (la Primary Key de la tarea) y lo pasa a la vista.
    # - 'DetalleTarea.as_view()' es la vista que mostrará el objeto correspondiente a esa 'pk'.
    path('tarea/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),

    # Ruta para el formulario de creación de una nueva tarea.
    path('crear-tarea/', CrearTarea.as_view(), name='crear_tarea'),

    # Ruta para editar una tarea existente. También requiere la 'pk' de la tarea.
    path('editar-tarea/<int:pk>/', EditarTarea.as_view(), name='editar_tarea'),

    # Ruta para eliminar una tarea existente. También requiere la 'pk'.
    path('eliminar-tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),
]
