from django.shortcuts import render, redirect
from .forms import CocineroForms, Comentario_acerca_restauranteForms, ReservaForms
from .models import Cocinero, Comentario_acerca_restaurante, Reserva

def cargar_cocinero(request):
    if request.method == 'POST':
        form = CocineroForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else: 
        form = CocineroForms()
    return render(request, 'AppRestaurante/cargar_cocinero_form.html', {'form': form})