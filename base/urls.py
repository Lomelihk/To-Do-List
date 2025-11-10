from django.urls import path
from .views import (
    ListaPendientes, DetalleTarea, CrearTarea, EditarTarea,
    EliminarTarea, LogeonUsuario, RegistrarUsuario
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Tareas
    path('', ListaPendientes.as_view(), name='lista_pendientes'),
    path('tarea/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear_tarea'),
    path('editar-tarea/<int:pk>/', EditarTarea.as_view(), name='editar_tarea'),
    path('eliminar-tarea/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),
    
    # Autenticación
    path('login/', LogeonUsuario.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegistrarUsuario.as_view(), name='register'),
]
