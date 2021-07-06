
from django.urls import path
from . import views

app_name = "PRUEBAAPP"
urlpatterns = [
    path('', views.home, name="index"),
    path('acerca-de', views.acerca, name="acerca-de"),
    path('contactos', views.contactos, name="contactos"),
    path('carrito', views.carrito, name="carrito"),
    path('agregar-carrito/<int:producto_id>', views.agregar_carrito, name="agregar-carrito"),
    path('eliminar-carrito/<int:producto_id>', views.eliminar_carrito, name="eliminar-carrito"),
    path('eliminar-carrito', views.eliminar_carrito, name="eliminar-carrito"),
    path('nuevo-producto', views.nuevo_producto, name="nuevo-producto"),
    path('registrarse',views.registrarse, name="registrarse"),
    path('ver-producto/<int:producto_id>', views.ver_producto, name="ver-producto"),
    path('editar-producto/<int:producto_id>', views.editar_producto, name="editar-producto"),
    path('eliminar-producto/<int:producto_id>', views.eliminar_producto, name="eliminar-producto"),
    path('resultadobusqueda', views.resultadobusqueda, name="resultadobusqueda"),
    path('categorias/<int:categoria_id>', views.categorias, name="categorias"),
    path('home', views.home, name="home"),
]
