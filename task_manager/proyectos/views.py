from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm
from django.contrib.auth.decorators import login_required

@login_required
def proyecto_list(request):
    proyectos = Proyecto.objects.filter(creador=request.user)
    return render(request, 'proyecto_list.html', {'proyectos': proyectos})



@login_required







@login_required
def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})

@login_required
def tarea_list(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id, creador=request.user)
    tareas = Tarea.objects.filter(proyecto=proyecto)
    return render(request, 'tarea_list.html', {'proyecto': proyecto, 'tareas': tareas})

@login_required
def tarea_create(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id, creador=request.user)
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



from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto
from .forms import ProyectoForm




from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto
from .forms import ProyectoColaboradoresForm

def editar_colaboradores(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoColaboradoresForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('detalle_proyecto', pk=proyecto.pk)
    else:
        form = ProyectoColaboradoresForm(instance=proyecto)
    return render(request, 'editar_colaboradores.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto
from .forms import ProyectoForm

def proyecto_create(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.creador = request.user
            proyecto.save()
            form.save_m2m()  # Guardar los colaboradores
            return redirect('proyecto_list')
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', {'form': form})


def proyecto_list(request):
    proyectos = Proyecto.objects.filter(colaboradores=request.user) | Proyecto.objects.filter(creador=request.user)
    return render(request, 'proyecto_list.html', {'proyectos': proyectos})





from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Proyecto

def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if proyecto.creador != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este proyecto.")
    if request.method == 'POST':
        proyecto.delete()
        return redirect('proyecto_list')
    return render(request, 'eliminar_proyecto.html', {'proyecto': proyecto})


def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if proyecto.creador != request.user and request.user not in proyecto.colaboradores.all():
        return HttpResponseForbidden("No tienes permiso para editar este proyecto.")
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('detalle_proyecto', pk=proyecto.pk)
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'editar_proyecto.html', {'form': form})
