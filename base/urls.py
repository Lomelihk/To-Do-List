from django.urls import path
from .views import lista_pendientes

urlpatterns = [
    path('', lista_pendientes, name='lista_pendientes'),
]
