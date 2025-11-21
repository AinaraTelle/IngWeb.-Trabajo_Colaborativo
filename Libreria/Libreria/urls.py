"""
URL configuration for Libreria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('appLibreria.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#Basicamente, esto sirve para que las imagenes subidas por nosotros se vean en la pagina, ya que lo que subimos hemos de ponerlo en media
#Y para que django lo tome como imagenes hay que "avisarle"

#http://127.0.0.1:8000/

# NOMBRE Y CONTRA Y CORREO DEL ADMINISTRADOR:
#Nombre:    Admin
#Contra:    Admin
#Correo:    Administer@gmail.com

#Para conectarse: http://127.0.0.1:8000/admin/