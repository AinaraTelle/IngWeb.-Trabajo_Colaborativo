from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

class registroFrom(UserCreationForm):
    nombre=forms.CharField(required=True, label="Introduzca su nombre")
    email=forms.EmailField(required= True,label="Introduzca su email")
    class Meta:
        model=User
        # fields= ['nombre', 'email', 'contrasenya', 'contrasenyaVis'] #esto era lo que estaba antes. Pero el programa no ejecuta
        
        fields= UserCreationForm.Meta.fields  # con esto, el programa sí ejecuta