from django.shortcuts import render, redirect
from .forms import CocineroForms, Comentario_acerca_restauranteForms, ReservarForms
from .models import Cocinero, Comentario_acerca_restaurante, Reservar
from django.db.models import Q
# Create your views here.


def cargar_cocinero(request):
    if request.method == 'POST':
        form = CocineroForms(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = CocineroForms()
    return render(request, 'AppRestaurante/cargar_cocinero.html', {'form': form})

def reservar_turno(request):
    if request.method == 'POST':
        form = ReservarForms(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = ReservarForms()
    return render(request, 'AppRestaurante/reservar_turnos.html', {'form': form})

def mostrar_reservas(request):
    reservas = Reservar.objects.all()
    return render(request, 'AppRestaurante/mostrar_reservas.html', {'reservas': reservas})

def hacer_comenterio(request):
    if request.method == 'POST':
        form = Comentario_acerca_restauranteForms(request.POST)
        if form.is_valid():
            form.save()
    else: 
        form = Comentario_acerca_restauranteForms()
    return render(request, 'AppRestaurante/hacer_comentario.html', {'form': form})

def inicio(request):
    return render(request, 'AppRestaurante/pagina_inicio.html')

#===============================BUSQUEDA=============================================
def buscar(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        cocineros = Cocinero.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query) | Q(especialidad__icontains=query)
        )

        for cocinero in cocineros:
            resultados.append({
                'tipo': 'Estudiante',
                'nombre': cocinero.nombre,
                'apellido': cocinero.apellido,
                'email': cocinero.email,
                'especialidad': cocinero.especialidad,
            })

    return render(request, 'AppRestaurante/busqueda_chef.html', {'resultados': resultados})