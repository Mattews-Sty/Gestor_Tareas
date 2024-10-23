from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages  # Importar el sistema de mensajes
from django.core.mail import send_mail
from django.conf import settings

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Verificar si el nombre de usuario o el correo electrónico ya existen
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return redirect('register')  # Redirigir para mostrar el mensaje

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Ya existe una cuenta con ese correo electrónico.')
            return redirect('register')  # Redirigir para mostrar el mensaje

        # Crear el nuevo usuario
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        send_mail(
            'Cuenta creada exitosamente',  # Asunto
            f'Hola {username},\n\nTu cuenta ha sido creada con éxito en nuestra plataforma.',  # Cuerpo del mensaje
            settings.EMAIL_HOST_USER,  # Remitente (tu correo desde settings.py)
            [email],  # Destinatario (el correo del usuario)
            fail_silently=False,
        )
        # Autenticar y loguear al usuario recién creado
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Cuenta creada exitosamente. ¡Bienvenido!')
            return redirect('dashboard')  # Redirigir al dashboard después del login

    # Si el método es GET, renderizar el formulario de registro
    return render(request, 'register.html')


# task_manager/views.py
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Vista para iniciar sesión
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige al dashboard después de iniciar sesión
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos")
            return render(request, 'login.html')  # Vuelve a mostrar el formulario de login

    return render(request, 'login.html')  # Si no es POST, muestra el formulario


from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

# Vista para la página de recuperación de contraseña
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
        
    return render(request, 'password_reset.html', {'form': form})


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

def home(request):
    return render(request, 'home.html')  