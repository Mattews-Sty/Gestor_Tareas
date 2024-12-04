from django.db import models
from django.contrib.auth.models import User
from proyectos.models import Proyecto

class Tarea(models.Model):
    ESTADOS = [
        ('ToDo', 'To Do'),
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey('proyectos.Proyecto', on_delete=models.CASCADE, related_name='tareas')
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='ToDo')

    def __str__(self):
        return self.nombre
