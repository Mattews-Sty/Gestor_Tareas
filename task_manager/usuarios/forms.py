# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }

class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'profile_image']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Biografía'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ubicación'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }