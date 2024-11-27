from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField(null=True, blank=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos')
    colaboradores = models.ManyToManyField(User, related_name='colaboraciones', blank=True)  # Campo de colaboradores

    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='tareas')
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    completado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre