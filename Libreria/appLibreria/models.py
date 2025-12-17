from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Autor(models.Model):
    nombre=models.CharField(max_length=50)#No se pone la id por que la base de datos asigna automaticamente la id
    def __str__(self):
        return self.nombre #Ayuda al admin, ya que aparece el nombre en pantalla del autor

class Editorial(models.Model):
    nif=models.CharField(max_length=9,primary_key=True)
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    isbn=models.CharField(max_length=13,primary_key=True)
    titulo=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='',null=True)#El uploadto es si en media tenemos subcarpetas deberiamos de especificar pero en este caso no
    descripcion=models.CharField(max_length=300)
    fecha_publicacion=models.DateField()#Importante: No hay en django una función que solo se pueda poner año y mes
    precio=models.FloatField()
    num_paginas=models.IntegerField()
    stock=models.IntegerField()
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    editorial=models.ForeignKey(Editorial,on_delete=models.CASCADE)
    class Genero(models.TextChoices):
        historico= "H", "Historico" #Se pone dos veces ya que el primer valor es lo que se guarda en la bd y la segunda lo que se vera en las templates
        romance= "R", "Romance"
        accion= "A", "Acción"  
        fantasia= "F", "Fantasía"
    genero=models.CharField(max_length=1,choices=Genero.choices)#Se limita la elección a las de genero
    class Idioma(models.TextChoices):
        espaniol="ESP", "Español"
        euskera="EUS", "Euskera"
        ingles="ENG", "Ingles"
    idioma=models.CharField(max_length=3,choices=Idioma.choices)
    
    def __str__(self):
        return self.titulo


class Carrito(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    @property
    def total(self):
        return sum(item.libro.precio * item.cantidad for item in self.items.all()) #EN vez de atributo es funcion, mas exacto y mas facil de utilizar
    def __str__(self):
        return f"Carrito de {self.usuario.username} ({self.items.count()} libros)"

class CarritoItem(models.Model):
    carrito = models.ForeignKey('Carrito', related_name='items', on_delete=models.CASCADE)#Para invocar los libros que contiene el carrito utilizamos items
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    

