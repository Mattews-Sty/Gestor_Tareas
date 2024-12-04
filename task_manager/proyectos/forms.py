from django import forms
from .models import Proyecto
from django.contrib.auth.models import User



class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_limite']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }


class ProyectoColaboradoresForm(forms.ModelForm):
    colaboradores = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Colaboradores'
    )

    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_limite', 'colaboradores']  # Incluye colaboradores
