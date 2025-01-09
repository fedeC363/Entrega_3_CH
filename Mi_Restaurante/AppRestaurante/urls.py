from django.urls import path
from .views import cargar_cocinero, mostrar_reservas, reservar_turno

urlpatterns = [
    path('', cargar_cocinero, name='cargar_cocinero'),
    path('reservar_turno/', reservar_turno, name='reservar_turno'),
    path('reservas/', mostrar_reservas, name='mostrar_reservas'),
]