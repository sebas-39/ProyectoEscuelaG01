from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from schoolapp.models import Estudiante, Programa, LogAuditor
from schoolapp.forms import ProgramaForm, EstudianteForm, UserForm, LoginForm

def register(request):
    contexto = dict()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                email=email,
                last_name=last_name
            )
            mensaje = f"Usuario {user.username} es almacenado correctamente"
        else:
            mensaje = "Error al registrar usuario"
        return render(request, 'mensaje.html', {'mensaje': mensaje}) 
    else:
        user = UserForm()
        contexto['userform'] = user
        return render(request, 'cuenta/registrar.html', contexto)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            else:
                mensaje = "No tiene permisos para acceder"
                return render(request, 'mensaje.html', {'mensaje': mensaje})             
        else:
            mensaje = "Verificar los datos ingresados"
            return render(request, 'mensaje.html', {'mensaje': mensaje}) 
    else:
        form = LoginForm()
        return render(request, 'cuenta/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect(reverse('login'))
    
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
    contexto['accion'] = 'Crear'
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            contexto['mensaje'] = 'El estudiante fue almacenado correctamente'
        else:
            contexto['mensaje'] = 'Los datos enviados desde el formulario no son validos'
        return render(request, 'estudiante/mensaje.html', contexto)
    else:
        form = EstudianteForm()
        contexto['boton'] = 'Guardar'
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