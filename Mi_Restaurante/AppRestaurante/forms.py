from django import forms
from .models import Cocinero, Comentario_acerca_restaurante, Reservar

class CocineroForms(forms.ModelForm):
    class Meta:
        model = Cocinero
        fields = ['nombre', 'apellido', 'email', 'especialidad']
        
class Comentario_acerca_restauranteForms(forms.ModelForm):
    class Meta:
        model = Comentario_acerca_restaurante
        fields = ['comentario', 'valoracion']
          
class ReservarForms(forms.ModelForm):
    class Meta:
        model = Reservar
        fields = ['fecha', 'hora']