"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import inicio,prueba,iniciarsesion,registrarse,cancelarreserva,editestacionamiento,reservar,pagoa,pestacionamiento,eperfil,eestacionamiento,deshabilitare,rechazare,aceptare,habilitare,eliminare,cerrarsesion,registro,perfil,recuperarContrasena,enviar_correo,mapa,aestacionamiento,agregarestacionamiento,editestacionamiento,eliminarUsuario
urlpatterns = [
    path('mapa',mapa,name='mapa'),
    path('',prueba,name='prueba'),
    path('pagoa',pagoa,name='pagoa'),
    path('aestacionamiento',aestacionamiento,name='aestacionamiento'),
    path('pestacionamiento/<int:ide>',pestacionamiento,name='pestacionamiento'),
    path('reservar/<int:ide>',reservar,name='reservar'),
    path('agregarestacionamiento',agregarestacionamiento,name='agregarestacionamiento'),
    path('editestacionamiento/<int:ide>',editestacionamiento,name='editestacionamiento'),
    path('eestacionamiento/<int:ide>',eestacionamiento,name='eestacionamiento'),
    path('inicio',inicio,name='inicio'),
    path('iniciarsesion',iniciarsesion,name='iniciarsesion'),
    path('cancelarreserva/<str:ide>',cancelarreserva,name='cancelarreserva'),
    path('registrarse',registrarse,name='registrarse'),
    path('registro',registro,name='registro'),
    path('cerrarsesion',cerrarsesion,name='cerrarsesion'),
    path('perfil',perfil,name='perfil'),
    path('recuperarContrasena',recuperarContrasena,name='recuperarContrasena'),
    path('enviar_correo', enviar_correo, name='enviar_correo'),
    path('deshabilitare/<int:ide>',deshabilitare,name='deshabilitare'),
    path('habilitare/<int:ide>',habilitare,name='habilitare'),
    path('eliminare/<int:ide>',eliminare,name='eliminare'),
    path('rechazare/<int:ide>',rechazare,name='rechazare'),
    path('aceptare/<int:ide>',aceptare,name='aceptare'),
    path('eperfil',eperfil,name='eperfil'),
    path('eliminarUsuario',eliminarUsuario,name='eliminarUsuario'),
]