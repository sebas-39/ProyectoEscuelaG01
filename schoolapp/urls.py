from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('registrar/', register, name='registrar-usuario'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('crear/programa/', crear_programa),
    path('actualizar/programa/<int:id>', actualizar_program),
    path('listar/estudiantes', listar_estudiante),
    path('crear/estudiante', crear_estudiante)
]
