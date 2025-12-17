from django.shortcuts import redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Tarea

class ListaPendientes(LoginRequiredMixin, ListView):
    
    """
    Esta vista muestra la lista de todas las tareas pendientes.
    Hereda de ListView, que automáticamente consulta todos los objetos del modelo especificado.
    """
    model = Tarea  # 1. Especifica que el modelo a utilizar para esta lista es 'Tarea'.
    context_object_name = 'tareas'  # 2. Define el nombre de la variable que contendrá la lista de tareas en la plantilla HTML.
                                    # Por defecto, sería 'object_list'. Con esto, la llamamos 'tareas'.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Llama al método padre para obtener el contexto base.
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)  # Filtra las tareas para que solo se muestren las del usuario actual.
        context['contador_tareas'] = context['tareas'].filter(completo=False).count()  # Cuenta las tareas no completadas.

        valor_buscar = self.request.GET.get('area_buscar') or ''
        if valor_buscar:
            context['tareas'] = context['tareas'].filter(
                titulo__icontains=valor_buscar
            )
        context['valor_buscar'] = valor_buscar
        return context # Devuelve el contexto modificado (si es necesario).

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
    fields = ['titulo', 'descripcion', 'completo']  # 2. Indica que todos los campos del modelo 'Tarea' deben ser incluidos en el formulario.
    success_url = reverse_lazy('lista_pendientes')  # 3. Define a qué URL redirigir al usuario después de que la tarea se haya creado con éxito.
    # 'reverse_lazy' busca la URL con el nombre 'lista_pendientes'.
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario actual a la tarea.
        return super().form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView):
    """
    Esta vista muestra un formulario para editar una tarea existente.
    Hereda de UpdateView, que funciona de manera similar a CreateView pero para actualizar un objeto existente.
    """
    model = Tarea  # 1. Especifica el modelo a utilizar.
    fields = ['titulo', 'descripcion', 'completo']   # 2. Indica que todos los campos se pueden editar en el formulario.
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
    
class RegistrarUsuario(FormView):
    """Registra nuevos usuarios en la aplicación.
    
    Valida los datos de registro y crea una nueva cuenta,
    iniciando automáticamente sesión si el registro es exitoso.
    """
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('lista_pendientes')

    def form_valid(self, form):
        """Guarda el nuevo usuario e inicia sesión automáticamente."""
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super().form_valid(form)
    
    def get(self, *args, **kwargs):
        """Redirige usuarios autenticados a la lista de tareas."""
        if self.request.user.is_authenticated:
            return redirect('lista_pendientes')
        return super().get(*args, **kwargs)


@require_POST
def toggle_complete(request, pk):
    """Alterna el estado de completitud de una tarea sin recargar la página.
    
    Solo el propietario de la tarea puede cambiar su estado.
    Retorna JSON con el nuevo estado.
    """
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    tarea.completo = not tarea.completo
    tarea.save()
    return JsonResponse({'completo': tarea.completo})
