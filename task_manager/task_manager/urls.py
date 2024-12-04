from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from task_manager.views import login_view, register_user, dashboard, home, password_reset, password_reset_done, logout_view  # Asegurarse de importar 'login_view' y 'register_user' desde 'task_manager.views'
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetConfirmView
from proyectos import views as proyectos_views  # Importar las vistas de 'proyectos'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),  # Usar 'login_view' para el login
    path('register/', register_user, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset_done/', password_reset_done, name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('crear-proyecto/', proyectos_views.proyecto_create, name='crear_proyecto'),
    path('proyecto/<int:pk>/', proyectos_views.detalle_proyecto, name='detalle_proyecto'),
    path('proyectos/', include('proyectos.urls')),  # Incluir las URLs de la app 'proyectos'
    path('usuarios/', include('usuarios.urls')),
    path('tasks/', include('tasks.urls')),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

