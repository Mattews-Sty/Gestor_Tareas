# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import RegisterForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            # Crear el nuevo usuario
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            send_mail(
                'Cuenta Creada Exitosamente',
                f'¡Hola {username}!\n\nTu cuenta ha sido creada con éxito en nuestra plataforma.\n\n\n\n© 2024, The Scrumers Team. Todos los derechos reservados.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            # Autenticar y loguear al usuario recién creado
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Cuenta creada exitosamente. ¡Bienvenido!')
                return redirect('dashboard')  # Redirigir al dashboard después del login
        else:
            for error in form.errors.values():
                messages.error(request, error)
            return redirect('register')  # Redirigir para mostrar el mensaje
    else:
        form = RegisterForm()
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


from django.contrib.auth.forms import PasswordResetForm , SetPasswordForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


# Vista para la página de recuperación de contraseña
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('password_reset_done')
        for error in form.errors.values():
                messages.error(request, error)
        return redirect('password_reset')  # Redirigir para mostrar el mensaje
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html')


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

def password_reset_done(request):
    return render(request, 'password_reset_done.html')


# views.py
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetConfirmView
from .forms import CustomSetPasswordForm

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('login')
    template_name = 'set_password.html'

    def form_valid(self, form):
        # Aquí es donde puedes agregar notificación de éxito
        messages.success(self.request, '¡Contraseña cambiada exitosamente!')
        return super().form_valid(form)
