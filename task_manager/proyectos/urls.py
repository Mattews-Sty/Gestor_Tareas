from django.urls import path
from . import views

urlpatterns = [
    path('', views.proyecto_list, name='proyecto_list'),
    path('nuevo/', views.proyecto_create, name='proyecto_create'),
    path('<int:pk>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('editar/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),  # URL para editar un proyecto
    path('<int:proyecto_id>/tareas/', views.tarea_list, name='tarea_list'),
    path('colaboradores/<int:pk>/', views.editar_colaboradores, name='editar_colaboradores'), # URL para editar colaboradores
    path('eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'), # URL para eliminar un proyecto
    path('<int:proyecto_id>/tareas/nueva/', views.tarea_create, name='tarea_create'),
]

