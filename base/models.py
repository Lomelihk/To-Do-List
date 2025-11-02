# Importa las funcionalidades necesarias de Django.
from django.db import models  # 'models' contiene las clases base para crear los modelos de la base de datos.
from django.contrib.auth.models import User  # Importa el modelo 'User' que Django provee para la gestión de usuarios.

# --- Definición del Modelo Tarea ---
# Un modelo en Django es la fuente única y definitiva de información sobre tus datos.
# Cada modelo se asigna a una única tabla de la base de datos.

class Tarea(models.Model):
    """
    Esta clase representa una tarea en la lista de pendientes.
    Hereda de 'models.Model', la clase base para todos los modelos en Django.
    """

    # --- Campos del Modelo ---

    # Campo para relacionar la tarea con un usuario específico.
    usuario = models.ForeignKey(
        User,  # Establece una relación 'muchos a uno' con el modelo User. Cada tarea pertenece a un usuario.
        on_delete=models.CASCADE,  # Si un usuario es eliminado, todas sus tareas también serán eliminadas.
        null=True,  # Permite que este campo sea 'NULL' en la base de datos. Es útil si una tarea no está asignada a nadie.
        blank=True  # Permite que este campo esté en blanco en los formularios de Django.
    )

    # Campo para el título de la tarea.
    titulo = models.CharField(
        max_length=200  # Define un campo de texto con una longitud máxima de 200 caracteres.
    )

    # Campo para la descripción detallada de la tarea.
    descripcion = models.TextField(
        null=True,  # Permite que el campo sea 'NULL' en la base de datos.
        blank=True  # Permite que el campo esté en blanco en los formularios. 'TextField' es para textos largos.
    )

    # Campo para marcar si la tarea está completa o no.
    completo = models.BooleanField(
        default=False  # Por defecto, una nueva tarea se crea como "no completada" (False).
    )

    # Campo para registrar la fecha y hora de creación de la tarea.
    creado = models.DateTimeField(
        auto_now_add=True  # Establece automáticamente la fecha y hora actuales cuando se crea un objeto por primera vez.
    )

    # --- Métodos del Modelo ---

    def __str__(self):
        """
        Este método define cómo se representará un objeto 'Tarea' como una cadena de texto.
        Es útil en el panel de administración de Django o al imprimir el objeto.
        """
        return self.titulo  # Devuelve el título de la tarea.

    # --- Metadatos del Modelo ---

    class Meta:
        """
        La clase 'Meta' interna permite configurar metadatos para el modelo.
        """
        # 'ordering' especifica el orden por defecto para los objetos cuando se consultan en la base de datos.
        ordering = ['completo']  # Ordena las tareas mostrando primero las incompletas ('completo'=False).