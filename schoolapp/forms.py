from dataclasses import fields
from pyexpat import model
from django import forms

from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ('nombre', 'descripcion')