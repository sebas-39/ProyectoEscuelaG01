from multiprocessing import context
from urllib import request
from django.shortcuts import render
from datetime import datetime

from schoolapp.models import Programa
from schoolapp.forms import ProgramaForm

def home(request):
    tiempo_ahora = datetime.now()
    programas = Programa.objects.all()
    contexto = {
        'hora': tiempo_ahora,
        'programas': programas
    }
    return render(request,'programa/inicio.html', contexto)

def crear_programa(request):
    if request.method == 'POST':
        pass
    else:
        programaForm = ProgramaForm()
        contexto = {'programaForm': programaForm}
        return render(request, 'programa/crear_programa.html', contexto)
