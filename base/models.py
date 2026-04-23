from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    """ Representa una tarea en la lista de quehaceres. """
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Retorna el título de la tarea como su representación en string. """
        return self.titulo

    class Meta:
        """ Ordena las tareas por estado de completitud. """
        ordering = ['completo']
