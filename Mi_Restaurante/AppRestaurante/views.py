from django.shortcuts import render, redirect
from .forms import CocineroForms, Comentario_acerca_restauranteForms, ReservarForms
from .models import Cocinero, Comentario_acerca_restaurante, Reservar
# Create your views here.

def cargar_cocinero(request):
    if request.method == 'POST':
        form = CocineroForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservar_turno')
    else: 
        form = CocineroForms()
    return render(request, 'AppRestaurante/cargar_cocinero.html', {'form': form})

def reservar_turno(request):
    if request.method == 'POST':
        form = ReservarForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_reservas')
    else: 
        form = ReservarForms()
    return render(request, 'AppRestaurante/reservar_turnos.html', {'form': form})

def mostrar_reservas(request):
    reservas = Reservar.objects.all()
    return render(request, 'AppRestaurante/mostrar_reservas.html', {'reservas': reservas})