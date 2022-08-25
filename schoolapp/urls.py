from django.urls import path
from .views import home, crear_programa

urlpatterns = [
    path('', home),
    path('crear/programa/', crear_programa)
]
