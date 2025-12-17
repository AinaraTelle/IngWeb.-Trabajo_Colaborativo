from django.urls import path
from . import views

urlpatterns = [
    path('home', views.paginaHome, name='antiguedad'), 
    path('', views.paginaInicio, name='inicio'), 
    path('index/', views.index, name='index'),

    path('genero/<str:genero_libro>/', views.genero, name='genero'),#H = historico, R = romance, A = acción, F = fantasia enel buscador poner las letras solas, no las palabras, asi esta en la BD
    
    path('genero/H/', views.genero, name='genH'),
    path('genero/F/', views.genero, name='genF'),
    path('genero/A/', views.genero, name='genA'),
    path('genero/R/', views.genero, name='genR'),
    path('genero/', views.generoTodosLibros, name='generoTodosLibros'),

    path('autores/',views.busqueda_autor, name='busqueda_autores'),

    path('precio/',views.precioTodosLibros, name='precioTodosLibros'),
    # path('precio/<int:precio_max>/', views.librosPorPrecio, name='librosPorPrecio'), #PD: en python no existen comas "," el precio seria 20.95 por ejemplo en vez de 20,95
    path('precio/', views.librosPorPrecio, name='librosPorPrecio'), 


    path('backapp/', views.masCortos,name='masCortos' ),
    path('detalles/<str:isbn_sel>/', views.detalles_libro, name='detalleLibro'),
    path('detalles/ref/<str:isbn_lib>/<str:cant>/', views.aniadir_Libro, name='aniadirLibro'),

    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/comprar/', views.comprar, name='comprar'),
    path('carrito/actualizar_contraseña/', views.actualizar_contraseña, name='actualizar_contraseña'),

    path('registro/',views.registrar_usuario, name='registrarUsuario'),
    path('login/',views.logInUsuario, name='LogIn'),
    path('logout/',views.logOut, name='logOut')
]