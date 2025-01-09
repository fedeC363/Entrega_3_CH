from django.shortcuts import render, redirect
from .forms import CocineroForms, Comentario_acerca_restauranteForms, ReservaForms
from .models import Cocinero, Comentario_acerca_restaurante, Reserva
# Create your views here.

def cargar_cocinero(request):
    if request.method == 'POST':
        form = CocineroForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio.html')
    else: 
        form = CocineroForms()
    return render(request, 'AppRestaurante/cargar_cocinero.html', {'form': form})

def mostrar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'AppRestaurante/mostrar_reservas_froms.html', {'reservas': reservas})