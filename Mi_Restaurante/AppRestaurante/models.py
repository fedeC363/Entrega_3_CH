from django.db import models

class Cocinero(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    especialidad = models.CharField(max_length=150)
    
    def __str__(self):
        return f'Nombre del chef: {self.nombre} {self.apellido}\nCorreo Electronico: {self.email}\nEspecialidad: {self.especialidad}'

class Comentario_acerca_restaurante(models.Model):
    comentario = models.CharField(max_length=200)
    valoracion = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return f'Su comentario ah sido envidado con exito.'

class Reserva(models.Model):
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    horario = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f'Usted ah reservado el dia {self.fecha} en el horario {self.horario}.'
