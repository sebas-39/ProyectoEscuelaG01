from multiprocessing import context
from django.shortcuts import render
from datetime import datetime

from schoolapp.models import Programa

def home(request):
    tiempo_ahora = datetime.now()
    programas = Programa.objects.all()
    contexto = {
        'hora': tiempo_ahora,
        'programas': programas
    }
    return render(request,'inicio.html', contexto)
