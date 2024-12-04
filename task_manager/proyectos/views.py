from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm
from django.contrib.auth.decorators import login_required

@login_required
def proyecto_list(request):
    proyectos = Proyecto.objects.filter(creador=request.user)
    return render(request, 'proyecto_list.html', {'proyectos': proyectos})


@login_required
def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})


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
