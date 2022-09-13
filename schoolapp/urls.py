from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('crear/programa/', crear_programa),
    path('actualizar/programa/<int:id>', actualizar_program),
    path('listar/estudiantes', listar_estudiante)
]
