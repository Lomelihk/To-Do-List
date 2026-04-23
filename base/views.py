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
    """ Muestra la lista de tareas del usuario autenticado. """
    model = Tarea
    context_object_name = 'tareas'

    def get_context_data(self, **kwargs):
        """ Filtra las tareas por usuario y añade un contador de tareas pendientes. """
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['contador_tareas'] = context['tareas'].filter(completo=False).count()

        valor_buscar = self.request.GET.get('area_buscar') or ''
        if valor_buscar:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscar)
        context['valor_buscar'] = valor_buscar
        return context

class DetalleTarea(LoginRequiredMixin, DetailView):
    """ Muestra los detalles de una única tarea. """
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'

class CrearTarea(LoginRequiredMixin, CreateView):
    """ Formulario para crear una nueva tarea. """
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('lista_pendientes')
    
    def form_valid(self, form):
        """ Asigna el usuario actual a la tarea antes de guardarla. """
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView):
    """ Formulario para editar una tarea existente. """
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('lista_pendientes')

class EliminarTarea(LoginRequiredMixin, DeleteView):
    """ Pide confirmación antes de eliminar una tarea. """
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('lista_pendientes')

class LogeonUsuario(LoginView):
    """ Maneja el inicio de sesión de usuarios. """
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        """ Redirige al usuario a la lista de pendientes después de iniciar sesión. """
        return reverse_lazy('lista_pendientes')
    
class RegistrarUsuario(FormView):
    """ Maneja el registro de nuevos usuarios. """
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('lista_pendientes')

    def form_valid(self, form):
        """ Si el formulario es válido, guarda al usuario e inicia sesión. """
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super().form_valid(form)
    
    def get(self, *args, **kwargs):
        """ Si el usuario ya está autenticado, lo redirige. """
        if self.request.user.is_authenticated:
            return redirect('lista_pendientes')
        return super().get(*args, **kwargs)


@require_POST
def toggle_complete(request, pk):
    """ Alterna el estado de 'completo' de una tarea. """
    tarea = get_object_or_404(Tarea, pk=pk, usuario=request.user)
    tarea.completo = not tarea.completo
    tarea.save()
    return JsonResponse({'completo': tarea.completo})
