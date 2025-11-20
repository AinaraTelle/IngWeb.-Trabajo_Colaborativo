from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse, Http404 
from appLibreria import models #importamos la tabla de models para poder trabajar con los datos de la BD
# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def genero(request, genero_libro):
    try:
        Libros = models.Libro.objects.filter(genero=genero_libro)#Filtramos todos los libros del genero que se ha escogido y los guardamos en Libros
        context = { #Creamos contexto, que se la pasaremos a la HTML para que sepa el contenido de cada variable
            'Libros':  Libros, #Lista de objetos "libro"
            'Genero': genero_libro
        }
        print("Genero del libro: ", genero_libro)
    except models.Libro.DoesNotExist:#Pagina personalizada del error
        raise Http404("No hay ningun libro de dicho genero")
    return render(request, 'genero.html', context) #Render se usa para crear un HTML como resuesta, por decirlo simple, y le pasamos lo que necesita para funcionar
        #return HttpResponse("Consultando genero del libro %s." %genero_libro)

def portadaYAntiguedad(request): #devuelve la portada tambien pero no he encontrado el atributo en modelos por lo que aun no añado
    Libros = models.Libro.objects.filter(stock__gte=20)
    context = {
        'Libros': Libros
    }

    return render(request, 'home.html', context)

def precio(request, precio_libro):
    try:
        precio_lib = Decimal(precio_libro)
        Libros=models.Libro.objects.filter(precio__lt=precio_lib) #<= no permitido
        context = {
            'Libros': Libros,
            'Prec_lib': precio_lib
        }
        print("precio: " + precio_libro)
        print(precio_lib)
        print(Libros)
    except models.Libro.DoesNotExist:#Pagina personalizada del error
        raise Http404("No hay ningun libro de dicho precio o menor")
    
    return render(request, 'precio.html',context)
    #return HttpResponse("Precio de libro %f" %precio_lib)

def masCortos(request):
    try: 
        Libros=models.Libro.objects.filter(num_paginas__lte=300)
        context = {
            'Libros': Libros
        }
    except models.Libro.DoesNotExist:
        raise Http404("No hay ningun libro tan corto")
    return render(request, 'inicio_novedades.html', context)