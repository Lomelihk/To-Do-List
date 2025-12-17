from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    """Modelo de tareas para la aplicación To-Do List.
    
    Representa una tarea individual con su contenido, estado de completitud
    y asociación con un usuario específico.
    """

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Usuario propietario de la tarea"
    )

    titulo = models.CharField(
        max_length=200,
        help_text="Título descriptivo de la tarea"
    )

    descripcion = models.TextField(
        null=True,
        blank=True,
        help_text="Descripción detallada de la tarea (opcional)"
    )

    completo = models.BooleanField(
        default=False,
        help_text="Indica si la tarea ha sido completada"
    )

    creado = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora de creación de la tarea"
    )

    def __str__(self):
        """Retorna la representación en string del objeto Tarea."""
        return self.titulo

    class Meta:
        """Configuración del modelo Tarea."""
        ordering = ['completo']
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
