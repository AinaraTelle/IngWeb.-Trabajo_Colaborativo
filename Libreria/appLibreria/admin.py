from django.contrib import admin

# Register your models here.
from .models import Autor, Editorial, Libro, Usuario, Carrito

admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Carrito)
