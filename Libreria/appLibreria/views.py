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
            'Libros':  Libros#Lista de objetos "libro"
        }
        print("Genero del libro: ", genero_libro)
    except models.Libro.DoesNotExist:#Pagina personalizada del error
        raise Http404("No hay ningun libro de dicho genero")
    return render(request, 'genero.html', context) #Render se usa para crear un HTML como resuesta, por decirlo simple, y le pasamos lo que necesita para funcionar
        #return HttpResponse("Consultando genero del libro %s." %genero_libro)

def portadaYAntiguedad(request): #devuelve la portada tambien pero no he encontrado el atributo en modelos por lo que aun no añado
    #return HttpResponse("Portada y antiguedad del libro %s" % fecha_libro) #no puedo devolver portada si no esta
    return render(request, 'inicio_novedades.html')

def precio(request, precio_libro):
    precio_lib = float(precio_libro)
    return HttpResponse("Precio de libro %f" %precio_lib)