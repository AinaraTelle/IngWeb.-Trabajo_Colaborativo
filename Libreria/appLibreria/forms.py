from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

class registroFrom(UserCreationForm):
    nombre=forms.CharField(required=True, label="Introduzca su nombre")
    email=forms.EmailField(required= True,label="Introduzca su email")
    class Meta:
        model=User
        fields= ['nombre', 'email', 'contrasenya', 'contrasenyaVis']