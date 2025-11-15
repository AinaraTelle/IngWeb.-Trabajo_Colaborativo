from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('genero/<str:genero_libro>/', views.genero, name='genero'),#H = historico, R = romance, A = acción, F = fantasia enel buscador poner las letras solas, no las palabras, asi esta en la BD
    path('', views.portadaYAntiguedad, name='antiguedad'), 
    path('precio/<str:precio_libro>/', views.precio, name='precio'), #PD: en python no existen comas "," el precio seria 20.95 por ejemplo en vez de 20,95
]