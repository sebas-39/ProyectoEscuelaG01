from multiprocessing import context
from urllib import request
from django.shortcuts import render
from datetime import datetime

from schoolapp.models import LogAuditor, Programa
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
        form = ProgramaForm(request.POST)
        contexto = dict()
        if form.is_valid():
            try:
                form.save()
                LogAuditor.objects.create(mensajeError = "Se guardo el programa correctamente")
            except ValueError as e:
                LogAuditor.objects.create(mensajeError = e)
                contexto = {
                    "mensaje": "El programa se almaceno correctamente"
                }
        else:
            contexto = {
                "mensaje": "Error al almacenar el programa"
            }
        return render(request, "programa/mensaje.html", contexto)
    else:
        programaForm = ProgramaForm()
        contexto = {'programaForm': programaForm}
        return render(request, 'programa/crear_programa.html', contexto)
