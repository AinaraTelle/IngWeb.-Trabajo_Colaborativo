from django.urls import path
from . import views

urlpatterns = [
    path('', views.portadaYAntiguedad, name='antiguedad'), 
    path('index/', views.index, name='index'),

    # path('genero/<str:genero_libro>/', views.genero, name='genero'),#H = historico, R = romance, A = acción, F = fantasia enel buscador poner las letras solas, no las palabras, asi esta en la BD
    path('genero/<str:genero_libro>/', views.genero, name='genero'),#H = historico, R = romance, A = acción, F = fantasia enel buscador poner las letras solas, no las palabras, asi esta en la BD
    
    path('genero/H/', views.genero, name='genH'),
    path('genero/F/', views.genero, name='genF'),
    path('genero/A/', views.genero, name='genA'),
    path('genero/R/', views.genero, name='genR'),
    path('genero/', views.generoTodosLibros, name='generoTodosLibros'),

    path('precios/',views.precioTodosLibros, name='precioTodosLibros'),

    path('precio/<str:precio_libro>/', views.precio, name='precio'), #PD: en python no existen comas "," el precio seria 20.95 por ejemplo en vez de 20,95
    path('backapp/', views.masCortos,name='masCortos' ),
    path('detalles/<str:isbn_sel>', views.detalles_libro, name='detalleLibro')
]