from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre=models.CharField(max_length=50)#No se pone la id por que la base de datos asigna automaticamente la id
    def __str__(self):
        return self.nombre #Ayuda al admin, ya que aparece el nombre en pantalla del autor

class Editorial(models.Model):
    nif=models.CharField(max_length=9,primary_key=True)
    nombre=models.CharField(max_length=50)
class Libro(models.Model):
    isbn=models.CharField(max_length=13,primary_key=True)
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=300)
    fecha_publicacion=models.DateField()#Importante: No hay en django una función que solo se pueda poner año y mes
    precio=models.FloatField()
    num_paginas=models.IntegerField()
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
    stock=models.IntegerField
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    email=models.CharField(max_length=50)
    contrasenia=models.CharField(max_length=50)
    nombre=models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario=models.OneToOneField(Usuario, on_delete=models.CASCADE)
    libros = models.ManyToManyField(Libro)
    @property
    def total(self):
        return sum(libro.precio for libro in self.libros.all()) #EN vez de atributo es funcion, mas exacto y mas facil de utilizar
    def __str__(self):
        return f"Carrito de {self.usuario.username} ({self.libros.count()} libros)"
    


                                    


