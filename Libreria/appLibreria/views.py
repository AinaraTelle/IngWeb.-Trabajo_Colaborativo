from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def genero(request, genero_libro):
    return HttpResponse("Consultando genero del libro %s." %genero_libro)

def portadaYAntiguedad(request, fecha_libro): #devuelve la portada tambien pero no he encontrado el atributo en modelos por lo que aun no añado
    return HttpResponse("Portada y antiguedad del libro %s" % fecha_libro) #no puedo devolver portada si no esta

def precio(request, precio_libro):
    return HttpResponse("Precio de libro %f" %precio_libro)