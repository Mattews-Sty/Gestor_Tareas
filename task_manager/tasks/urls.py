from django.urls import path
from . import views

urlpatterns = [
    path('<int:proyecto_id>/tareas/', views.tarea_list, name='tarea_list'),
    path('<int:proyecto_id>/tareas/crear/', views.tarea_create, name='tarea_create'),
    path('tareas/<int:tarea_id>/editar/', views.tarea_edit, name='tarea_edit'),
    path('tareas/<int:tarea_id>/eliminar/', views.tarea_delete, name='tarea_delete'),
    path('tareas/<int:tarea_id>/detail/', views.tarea_detail, name='tarea_detail'),
    path('tareas/<int:tarea_id>/completar/', views.tarea_toggle_complete, name='tarea_toggle_complete'),
]
