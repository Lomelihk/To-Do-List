from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tarea(models.Model):

    #los apartados null y blank son para poder tener el
    # permiso de dejar el espacio en blanco del valor de usuario null p
    #puede estar vacio y blank para dejar el formulario en blanco
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null = True,
                                blank = True,
                                )
    #max_length es para tener un limitede caracteres
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null = True,
                                    blank = True)
    completo = models. BooleanField(default= False)
    creado = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completo']