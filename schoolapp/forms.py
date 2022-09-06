from dataclasses import fields
from pyexpat import model
from django import forms

from .models import Programa, Estudiante

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = '__all__'
        
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        