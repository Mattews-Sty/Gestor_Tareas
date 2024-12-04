# Create your views here.
# tasks/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from proyectos.models import Proyecto
from django.contrib import messages
from .models import Proyecto, Tarea
from .forms import TareaForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Cambia 'dashboard' por la ruta de tu dashboard
        else:
            messages.error(request, "Usuario o Contraseña Incorrectos")
    return render(request, 'login.html')  # Llama a la plantilla de inicio de sesión

# views.py
def dashboard(request):
    return render(request, 'dashboard.html')  # Asegúrate de tener este template

@login_required
def tarea_list(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, creador=request.user)
    tareas = Tarea.objects.filter(proyecto=proyecto)
    return render(request, 'tarea_list.html', {'proyecto': proyecto, 'tareas': tareas})

from django.shortcuts import render, get_object_or_404
from .models import Tarea
from proyectos.models import Proyecto

def tarea_list(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.user in proyecto.colaboradores.all() or request.user == proyecto.creador:
        tareas = Tarea.objects.filter(proyecto=proyecto)
        return render(request, 'tarea_list.html', {'proyecto': proyecto, 'tareas': tareas})
    else:
        return redirect('proyecto_list')  # Redirige a la lista de proyectos si el usuario no tiene acceso


@login_required
def tarea_create(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id, creador=request.user)
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.save()
            return redirect('tarea_list', proyecto_id=proyecto.id)
    else:
        form = TareaForm()
    return render(request, 'tarea_form.html', {'form': form, 'proyecto': proyecto})

@login_required
def tarea_edit(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tarea_list', proyecto_id=tarea.proyecto.id)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tarea_form.html', {'form': form, 'proyecto': tarea.proyecto})

@login_required
def tarea_delete(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    proyecto_id = tarea.proyecto.id
    tarea.delete()
    return redirect('tarea_list', proyecto_id=proyecto_id)

@login_required
def tarea_detail(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        tarea.estado = 'Done'
        tarea.save()
        return redirect('tarea_list', proyecto_id=tarea.proyecto.id)
    return render(request, 'tarea_detail.html', {'tarea': tarea})

@login_required
def tarea_toggle_complete(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completado = not tarea.completado
    tarea.save()
    return redirect('tarea_list', proyecto_id=tarea.proyecto.id)
