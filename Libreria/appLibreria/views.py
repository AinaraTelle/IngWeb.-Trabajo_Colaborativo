from decimal import Decimal
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404 
from appLibreria import models #importamos la tabla de models para poder trabajar con los datos de la BD
from django.contrib.auth.decorators import login_required
from .forms import registroForm,logInForm,updateForm
from .models import Usuario
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


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
      

def paginaHome(request): #devuelve la portada tambien pero no he encontrado el atributo en modelos por lo que aun no añado
    Libros = models.Libro.objects.filter(stock__gte=1)
    context = {
        'Libros': Libros
    }

    return render(request, 'home.html', context)

def paginaInicio(request): #devuelve la portada tambien pero no he encontrado el atributo en modelos por lo que aun no añado
    # Libros = models.Libro.objects.filter(stock__gte=1)
    context = {
        # 'Libros': Libros
    }

    return render(request, 'inicio.html', context)



#Detalles.HTML:

def detalles_libro(request, isbn_sel):
    Libro = models.Libro.objects.get(isbn=isbn_sel)#Obtenemos el libro cuyo isbn es el mismo que el que qeremos ver detallado

    return render(request, 'detalles.html', {'libro': Libro, 'ISBN': isbn_sel})#Esta forma de pasarle "Libro" es la misma de siempre pero sin meterlo todo en una variable


def aniadir_Libro(request, isbn_lib):#Y si hago que pase el ISBN y asi ya sabe que libro se añade
    nv_libro = models.Libro.objects.get(isbn=isbn_lib)
    nv_carrito = models.Carrito.objects.get(usuario=request.user)

    existente, nuevo_libro = models.CarritoItem.objects.get_or_create( carrito = nv_carrito, libro = nv_libro)#Ya guarda automaticamente si lo tiene que crear

    if( not nuevo_libro):#Hay que hacer que cuando no haya mas stock no deje comprar
        #sumamos uno a la cantidad y lo devolvemos
        existente.cantidad += 1
        existente.save()
        
    
    return render(request, 'detalles.html', {'libro': nv_libro, 'ISBN': isbn_lib, 'cant_compra': existente.cantidad})#La idea es que refresque la PG pero añada el libro al carrito



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
    carrito ,creado = models.Carrito.objects.get_or_create(usuario=request.user)# Esta con coma ya que aqui se crea el carrito una vez que el usuario accede por primera vez o detecta si esta creado, por lo tanto el carrito sería el tipo de item y el creado es true o false
    items=carrito.items.all()#Obtenemos los libros con su precio y la cantidad de los mismos
    context = {
        'usuario': request.user,
        'carrito': carrito,
        'items':items,
        'total': carrito.total
    }
    return render(request, "carrito.html", context)

@require_POST
def comprar(request):#Basicamente existe para actualizar la existencias de libros
    carrito=models.Carrito.objects.get(usuario=request.user)
    for item in carrito.items.all():
        libro = item.libro

        if libro.stock >= item.cantidad:
            libro.stock -= item.cantidad  
            libro.save()#Actualiza stock
        else:
            messages.error(request, f"No hay suficiente stock de {libro.titulo}")
            return redirect('ver_carrito')

    
    carrito.items.all().delete()#Vacia el carrito despues de la compra
    return redirect('ver_carrito')  # Una vez terminada la compra se redirige a inicio

def registrar_usuario(request):
    if request.method=='POST':
        form=registroForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['contrasenia']==form.cleaned_data['contrasenia2']:
                usuario=Usuario(
                    email=form.cleaned_data['email'],
                    contrasenia=make_password(form.cleaned_data['contrasenia']),
                    nombre=form.cleaned_data['nombre']
                )
                usuario.save()
                request.session['id']=usuario.id#para hacer login manualmente
                return redirect('generoTodosLibros')
            else:
                return HttpResponse("Contraseñas no coinciden")
    else:
        form=registroForm()
    return render(request, 'registro.html', {'form': form})

def logInUsuario(request):
    if request.method=='POST':
        form=logInForm(request.POST)
        if form.is_valid():
            try:
                usuario=Usuario.objects.get(nombre=form.cleaned_data['nombre'], email=form.cleaned_data['email'])
            except Usuario.DoesNotExist:
                return HttpResponse("Usuario no existente, nombre o direccion incorrectos")
            
            if check_password(form.cleaned_data['contrasenia'], usuario.password_hash):
                request.session['id']=usuario.id
                return redirect('generoTodosLibros')
    else:
        form=logInForm()
    return render(request, 'login.html', {'form':form})

    

def actualizar_contraseña(request):
    id=request.session.get('id')
    if not(id):
        redirect('login')
    usuario=Usuario.objects.get('id')

    if request.method == 'POST': #Poenmos esto ya que se puede llegar a cambiar la contraseña sin querer con un get
        form=updateForm(request.POST)
        if form.is_valid():
            if not check_password(form.cleaned_data['contrasenia'], usuario.contrasenia):
                return HttpResponse("Contraseña actual incorrecta")
            if form.cleaned_data['contrasenia1'] != form.cleaned_data['contrasenia2']:
                return HttpResponse("Las nuevas contraseñas no coinciden")
            usuario.contrasenia = make_password(form.cleaned_data['contrasenia_nueva'])
            usuario.save()
            return redirect('ver_carrito')
    else:
        form=updateForm()
    return render(request, 'carrito.html', {'form': form})