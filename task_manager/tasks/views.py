from django.shortcuts import render

# Create your views here.
# tasks/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Cambia 'dashboard' por la ruta de tu dashboard
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos")
    return render(request, 'login.html')  # Llama a la plantilla de inicio de sesión

# views.py

from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')  # Asegúrate de tener este template
