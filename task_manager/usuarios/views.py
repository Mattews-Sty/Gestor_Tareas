from django.shortcuts import render


# views.py
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def view_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile.save()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('view_profile')  # Redirigir a la página de perfil
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

