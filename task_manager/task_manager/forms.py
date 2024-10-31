# task_manager/forms.py

# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.password_validation import validate_password
import re

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        min_length=8  # Ajuste para la longitud mínima de la contraseña
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Ya existe una cuenta con ese correo electrónico.')
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        if re.match(r'^\d+$', password1):
            raise ValidationError('La contraseña no puede contener solo números.')
        validate_password(password1)  # Utiliza los validadores de Django para verificar la contraseña
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contraseñas no coinciden.')
        return password2

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            validate_password(password1)  # Verifica las restricciones de la contraseña

        return cleaned_data


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nueva contraseña'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmar nueva contraseña'})



class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('No Existe Una Cuenta Con Este Correo lectrónico.')
        return email
