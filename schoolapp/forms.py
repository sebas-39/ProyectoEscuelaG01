from django import forms

from .models import Programa, Estudiante

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = '__all__'
        
class EstudianteForm(forms.ModelForm):
    username = forms.CharField(label='Usuario', max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
           'placeholder': 'Usuario' 
        }
    ))
    password = forms.CharField(label='Contraseña', max_length=30, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    first_name = forms.CharField(label='Nombres', max_length=30, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    
    last_name = forms.CharField(label='Apellidos', max_length=60, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    cod_estudiante = forms.CharField(label='Cód. Estudiante', max_length=12, widget=forms.TextInput(
        attrs={
           'class': 'form-control',
           'placeholder': 'Código del Estudiante' 
        }
    ))
    acudiente = forms.CharField(label='Acudiente',max_length=180, widget=forms.TextInput(
        attrs={
           'class': 'form-control' 
        }
    ))
    telefono = forms.CharField(label='Teléfono', max_length=14, required=False, widget=forms.TextInput(
        attrs={
           'class': 'form-control' 
        }
    ))
    direccion = forms.CharField(label='Dirección', max_length=50, required=False, widget=forms.TextInput(
        attrs={
           'class': 'form-control' 
        }
    ))
    
    class Meta:
        model = Estudiante
        exclude = ['user']
        