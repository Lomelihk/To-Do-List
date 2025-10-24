# Importaciones necesarias para las vistas de Django
from django.shortcuts import render  # Para renderizar plantillas con contexto
from django.views.generic.list import ListView  # Vista genérica para mostrar listas de objetos
from django.views.generic.detail import DetailView  # Vista genérica para mostrar detalles de un objeto
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # Vistas genéricas para crear, editar y eliminar objetos
from django.urls import reverse_lazy  # Para redireccionar después de operaciones exitosas
from .models import Tarea  # Importamos nuestro modelo Tarea


class ListaPendientes(ListView):
    """
    Vista para mostrar una lista de todas las tareas.
    Hereda de ListView que proporciona funcionalidad para mostrar listas de objetos.
    """
    model = Tarea  # Especifica qué modelo usar (Tarea)
    context_object_name = 'tareas'  # Nombre de la variable en el template (en lugar del default 'object_list')


class DetalleTarea(DetailView):
    """
    Vista para mostrar los detalles de una tarea específica.
    Hereda de DetailView que proporciona funcionalidad para mostrar un objeto individual.
    """
    model = Tarea  # Especifica qué modelo usar (Tarea)
    context_object_name = 'tarea'  # Nombre de la variable en el template (en lugar del default 'object')
    template_name = 'base/tarea.html'  # Especifica qué plantilla usar (en lugar del default)


class CrearTarea(CreateView):
    """
    Vista para crear una nueva tarea.
    Hereda de CreateView que proporciona funcionalidad para crear nuevos objetos.
    """
    model = Tarea  # Especifica qué modelo usar (Tarea)
    fields = '__all__'  # Incluye todos los campos del modelo en el formulario
    success_url = reverse_lazy('lista_pendientes')  # URL a la que redirigir después de crear exitosamente