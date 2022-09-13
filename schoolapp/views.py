from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from datetime import datetime

from schoolapp.models import Estudiante, Programa, LogAuditor
from schoolapp.forms import ProgramaForm, EstudianteForm

def home(request):
    return render(request,'index.html')

def listar_estudiante(request):
    estudiantes = Estudiante.objects.all()
    contexto = {
        'estudiantes': estudiantes
    }
    return render(request, 'estudiante/listar.html', contexto)

def crear_estudiante(request):
    contexto = dict()
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensaje de almacenamiento correcto
        else:
            #mensaje de almacenamiento incorrecto
            pass
    else:
        form = EstudianteForm()
        contexto['form'] = form
        return render(request, 'estudiante/form.html', contexto) 

def crear_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        contexto = dict()
        if form.is_valid():
            try:
                form.save()
                LogAuditor.objects.create(mensajeError="Se guardo el programa correctamente")
            except ValueError as e:
                LogAuditor.objects.create(mensajeError=e)
            contexto['mensaje'] = "El programa se almacenó correctamente"
        else:
            contexto['mensaje'] = "Error al almacenar el programa"
        return render(request, 'programa/mensaje.html', contexto)
    else:
        programaForm = ProgramaForm()
        contexto = {
            'programaForm': programaForm,
            'boton': 'Guardar',
            'accion': 'Crear'
            }
        return render(request, 'programa/form_programa.html', contexto)

def actualizar_program(request, id):
    try:
        programa = Programa.objects.get(id=id)
    except ObjectDoesNotExist:
        mensaje = "El programa que pretender editar no existe"
        LogAuditor.objects.create(mensajeError=mensaje)
        return HttpResponse(mensaje)
        
    contexto = dict()
    if request.method == 'POST':
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            contexto['mensaje'] = "El programa fue editado correctamente"
        else:
            contexto['mensaje'] = "Error al almacenar el programa"
        return render(request, 'programa/mensaje.html', contexto)
    else:
        programForm = ProgramaForm(instance=programa)
        contexto['programaForm'] = programForm
        contexto['boton'] = 'Editar'
        contexto['accion'] = 'Editar'
        return render(request, 'programa/form_programa.html', contexto)