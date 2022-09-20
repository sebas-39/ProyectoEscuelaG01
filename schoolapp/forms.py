from dataclasses import fields
from django import forms
from django.contrib.auth.models import User

from .models import Programa, Estudiante

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = '__all__'
        
class EstudianteForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-select'
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
        fields = '__all__'
        
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Usuario', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    password = forms.CharField(max_length=80, label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    ))    
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(
        attrs={
            'class': 'form-control'
        }
    ))
    
    first_name = forms.CharField(max_length=40, label='Nombres', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    
    last_name = forms.CharField(max_length=40, label='Apellidos', widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Usuario'
        }
    ))
    password = forms.CharField(label='Password', max_length=80, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))