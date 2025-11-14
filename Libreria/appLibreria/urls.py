from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genero/<str:genero>/', views.Libro, name='genero'),
    path('fecha/<str:fecha_libro>/', views.Libro, name='antiguedad'), #no portada 
    path('precio/<int:precio_libro/', views.Libro, name='precio'),
]