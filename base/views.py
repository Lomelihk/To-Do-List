# --- Importaciones Necesarias ---
from django.shortcuts import render  # Función para renderizar plantillas HTML con datos de contexto.
from django.views.generic.list import ListView  # Vista genérica para mostrar una lista de objetos de un modelo.
from django.views.generic.detail import DetailView  # Vista genérica para mostrar el detalle de un objeto específico.
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # Vistas para formularios de creación, edición y eliminación.
from django.contrib.auth.views import LoginView  # Vistas para manejar el inicio y cierre de sesión de usuarios.
from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin para restringir el acceso a usuarios autenticados.
from django.urls import reverse_lazy  # Utilidad para obtener una URL a partir de su nombre, de forma diferida (lazy).
from .models import Tarea  # Importa el modelo 'Tarea' que definimos en models.py.


# --- Vistas Basadas en Clases (Class-Based Views) ---
# Django ofrece vistas genéricas que simplifican las tareas comunes (listar, detallar, crear, etc.).

class ListaPendientes(LoginRequiredMixin, ListView):
    """
    Esta vista muestra la lista de todas las tareas pendientes.
    Hereda de ListView, que automáticamente consulta todos los objetos del modelo especificado.
    """
    model = Tarea  # 1. Especifica que el modelo a utilizar para esta lista es 'Tarea'.
    context_object_name = 'tareas'  # 2. Define el nombre de la variable que contendrá la lista de tareas en la plantilla HTML.
                                    # Por defecto, sería 'object_list'. Con esto, la llamamos 'tareas'.


class DetalleTarea(LoginRequiredMixin, DetailView):
    """
    Esta vista muestra los detalles de una única tarea.
    Hereda de DetailView, que espera una clave primaria (pk) en la URL para buscar un objeto específico.
    """
    model = Tarea  # 1. Especifica que el modelo a utilizar es 'Tarea'.
    context_object_name = 'tarea'  # 2. Define el nombre de la variable para el objeto en la plantilla. Por defecto, sería 'object'.
    template_name = 'base/tarea.html'  # 3. Especifica un nombre de plantilla diferente al que Django busca por defecto ('tarea_detail.html').


class CrearTarea(LoginRequiredMixin, CreateView):
    """
    Esta vista muestra un formulario para crear una nueva tarea.
    Hereda de CreateView, que renderiza un formulario basado en el modelo y procesa los datos enviados.
    """
    model = Tarea  # 1. Especifica que el modelo a utilizar para crear un objeto es 'Tarea'.
    fields = '__all__'  # 2. Indica que todos los campos del modelo 'Tarea' deben ser incluidos en el formulario.
    success_url = reverse_lazy('lista_pendientes')  # 3. Define a qué URL redirigir al usuario después de que la tarea se haya creado con éxito.
                              # 'reverse_lazy' busca la URL con el nombre 'lista_pendientes'.

class EditarTarea(LoginRequiredMixin, UpdateView):
    """
    Esta vista muestra un formulario para editar una tarea existente.
    Hereda de UpdateView, que funciona de manera similar a CreateView pero para actualizar un objeto existente.
    """
    model = Tarea  # 1. Especifica el modelo a utilizar.
    fields = '__all__'  # 2. Indica que todos los campos se pueden editar en el formulario.
    success_url = reverse_lazy('lista_pendientes')  # 3. Redirige a la lista de pendientes después de una edición exitosa.

class EliminarTarea(LoginRequiredMixin, DeleteView):
    """
    Esta vista muestra una página de confirmación antes de eliminar una tarea.
    Hereda de DeleteView.
    """
    model = Tarea  # 1. Especifica el modelo del objeto a eliminar.
    context_object_name = 'tarea' # 2. Cambia el nombre del objeto en la plantilla a 'tarea'.
    success_url = reverse_lazy('lista_pendientes')  # 3. Redirige a la lista de pendientes después de eliminar la tarea.
    # Django buscará automáticamente una plantilla llamada 'tarea_confirm_delete.html' para esta vista.

class LogeonUsuario(LoginView):
    """
    Esta vista maneja el inicio de sesión de usuarios.
    Hereda de LoginView, que proporciona toda la funcionalidad necesaria para autenticar usuarios.
    """
    template_name = 'base/login.html'  # 1. Especifica la plantilla HTML para el formulario de inicio de sesión.
    field = '__all__'  # Incluye todos los campos del formulario de inicio de sesión (por defecto, 'username'
    redirect_authenticated_user = True  # 2. Si el usuario ya está autenticado, lo redirige automáticamente.

    def get_success_url(self):
        """
        Define la URL a la que se redirige al usuario después de un inicio de sesión exitoso.
        """ 
        return reverse_lazy('lista_pendientes')  # Redirige a la lista de pendientes.