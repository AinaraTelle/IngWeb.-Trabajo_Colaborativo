from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

class registroFrom(forms.Form):
    nombre_usuario=forms.CharField(required=True, label="Introduzca su nombre")
    email_usuario=forms.EmailField(required= True,label="Introduzca su email")
    password=forms.CharField(widget=forms.PasswordInput, label="Introduzca la contraseña")
    password2=forms.CharField(widget=forms.PasswordInput, label="Introduzca la contraseña otra vez")
    
class logInForm(forms.Form):
    nombre_usuario=forms.CharField(required=True, label="Introduzca su nombre")
    email_usuario=forms.EmailField(required= True,label="Introduzca su email")
    password=forms.CharField(widget=forms.PasswordInput, label="Introduzca la contraseña")