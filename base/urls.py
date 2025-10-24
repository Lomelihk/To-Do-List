from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea

urlpatterns = [
    path('', ListaPendientes.as_view(), name='lista_pendientes'),
    path('tarea/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
    path('crear-tarea/', CrearTarea.as_view(), name='crear_tarea'),
]
