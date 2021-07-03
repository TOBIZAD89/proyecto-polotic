
from django.urls import path
from . import views

app_name = "PRUEBAAPP"
urlpatterns = [
    path('', views.home, name="index"),
    path('acerca-de', views.acerca, name="acerca-de"),
    path('plantilla',views.plantilla, name="plantilla"),
    path('contactos', views.contactos, name="contactos"),
    path('nuevo-producto', views.nuevo_producto, name="nuevo-producto"),
    path('login',views.login, name="login"),
    path('registrarse',views.registrarse, name="registrarse"),
    path('ver-producto', views.ver_producto, name="ver-producto"),
    path('resultadobusqueda', views.resultadobusqueda, name="resultadobusqueda"),
    path('categorias', views.categorias, name="categorias"),
    path('home', views.home, name="home"),
    
]
