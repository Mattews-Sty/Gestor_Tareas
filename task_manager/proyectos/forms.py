from django import forms
from .models import Proyecto, Tarea



class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_limite']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'proyecto', 'asignado_a', 'completado']


from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_limite']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }


from django import forms
from .models import Proyecto
from django.contrib.auth.models import User

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
