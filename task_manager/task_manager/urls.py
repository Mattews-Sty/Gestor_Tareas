"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# task_manager/urls.py
from django.contrib import admin
from django.urls import path
from tasks.views import login_view
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('login/', login_view, name='login'),  # URL para el login
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_user, name='register'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
# task_manager/urls.py

