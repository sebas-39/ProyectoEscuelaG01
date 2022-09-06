from django.urls import path
from .views import home, crear_programa, actualizar_program

urlpatterns = [
    path('', home),
    path('crear/programa/', crear_programa),
    path('actualizar/programa/<int:id>', actualizar_program)
]
