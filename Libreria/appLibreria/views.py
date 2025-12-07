from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse, Http404 
from appLibreria import models #importamos la tabla de models para poder trabajar con los datos de la BD
from django.contrib.auth.decorators import login_required
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

def generoTodosLibros(request):
    try:
        Libros = models.Libro.objects.all()
        context = { #Creamos contexto, que se la pasaremos a la HTML para que sepa el contenido de cada variable
            'Libros':  Libros, #Lista de objetos "libro"
        }
    except models.Libro.DoesNotExist:#Pagina personalizada del error
        raise Http404("No hay ningun libro de dicho genero")
    return render(request, 'genero.html', context) #Render se usa para crear un HTML como resuesta, por decirlo simple, y le pasamos lo que necesita para funcionar
      

def portadaYAntiguedad(request): #devuelve la portada tambien pero no he encontrado el atributo en modelos por lo que aun no añado
    Libros = models.Libro.objects.filter(stock__gte=1)
    context = {
        'Libros': Libros
    }

    return render(request, 'home.html', context)


def detalles_libro(request, isbn_sel):
    Libro = models.Libro.objects.get(isbn=isbn_sel)#Obtenemos el libro cuyo isbn es el mismo que el que qeremos ver detallado

    return render(request, 'detalles.html', {'libro': Libro})#Esta forma de pasarle "Libro" es la misma de siempre pero sin meterlo todo en una variable

def precioTodosLibros(request):
    try:
        Libros = models.Libro.objects.all()
        context = { #Creamos contexto, que se la pasaremos a la HTML para que sepa el contenido de cada variable
            'Libros':  Libros, #Lista de objetos "libro"
        }
    except models.Libro.DoesNotExist:#Pagina personalizada del error
        raise Http404("No hay ningun libro de dicho genero")
    return render(request, 'precio.html', context) #Render se usa para crear un HTML como resuesta, por decirlo simple, y le pasamos lo que necesita para funcionar

def librosPorPrecio(request):
    try:
        precio_maxV=request.GET.get('precio_max')
        precio_max=Decimal(precio_maxV)
        Libros=models.Libro.objects.filter(precio__lt=precio_max) #<= no permitido
        context = {
            'Libros': Libros,
            'precio_libro': precio_max
        }
    except models.Libro.DoesNotExist:#Pagina personalizada del error
        raise Http404("No hay ningun libro de dicho precio o menor")
    
    return render(request, 'precio.html',context)


def masCortos(request):
    try: 
        Libros=models.Libro.objects.filter(num_paginas__lte=300)
        context = {
            'Libros': Libros
        }
    except models.Libro.DoesNotExist:
        raise Http404("No hay ningun libro tan corto")
    return render(request, 'inicio_novedades.html', context)

def busqueda_autor(request):
    autores=models.Autor.objects.all().order_by("nombre")
    autorbuscado_id=request.GET.get('autor_seleccionado')
    if autorbuscado_id:#Si hay alguna id seleccionada
        autorbuscado_id=int(autorbuscado_id)
        libros=models.Libro.objects.filter(autor_id=autorbuscado_id)#Pasando el str en int sino no detecta el filtro de autor
    else:#Por default o si no hay autor seleccionado
        libros=models.Libro.objects.all()
    context= {
        'autores':autores,
        'autor_seleccionado':autorbuscado_id,
        'libros':libros
    }
    return render(request, 'autor.html', context)



@login_required
def ver_carrito(request):
    carrito ,creado = models.Carrito.objects.get_or_create(usuario=request.user)# Esta con coma ya que aqui se crea el carrito una vez que el usuario accede por primera vez o detecta si esta creadp, por lo tanto el carrito sería el tipo de item y el creado es true o false
    
    context = {
        'usuario': request.user,
        'carrito': carrito,
        'libros': carrito.libros.all(),
        'total': carrito.total
    }
    return render(request, "carrito.html", context)