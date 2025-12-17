from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

class registroForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=20, label="Nombre de usuario")
    email = forms.EmailField(required=True, max_length=50, label="Email")
    contrasenia = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    contrasenia2 = forms.CharField(widget=forms.PasswordInput, label="Repetir contraseña")

class logInForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=20, label="Nombre de usuario")
    email = forms.EmailField(required=True, max_length=50, label="Email")
    contrasenia = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

class updateForm(forms.Form):
    contrasenia=forms.CharField(required=True, label="Introduzca su contraseña ")
    contrasenia1 = forms.CharField(widget=forms.PasswordInput, label="Nueva contraseña")
    contrasenia2 = forms.CharField(widget=forms.PasswordInput, label="Repetir contraseña")
