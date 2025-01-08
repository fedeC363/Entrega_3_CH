from django.urls import path
from .views import cargar_cocinero

urlpatterns = [
    path('', cargar_cocinero, name='cargar_cocinero'),
]