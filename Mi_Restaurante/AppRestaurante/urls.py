from django.urls import path
from .views import cargar_cocinero, mostrar_reservas, reservar_turno, inicio, hacer_comenterio

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cargar_cocinero/', cargar_cocinero, name='cargar_cocinero'),
    path('reservar_turno/', reservar_turno, name='reservar_turno'),
    path('reservas/', mostrar_reservas, name='mostrar_reservas'),
    path('hacer_comentario', hacer_comenterio, name='hacer_comentario'),
]