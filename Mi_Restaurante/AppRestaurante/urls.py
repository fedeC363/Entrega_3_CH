from django.urls import path
from .views import cargar_cocinero, mostrar_reservas

urlpatterns = [
    path('cargar_cocinero/', cargar_cocinero, name='cargar_cocinero'),
    path('reservas/', mostrar_reservas, name='mostrar_reservas'),
]