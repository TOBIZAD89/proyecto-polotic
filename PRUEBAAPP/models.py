from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields import EmailField

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.descripcion}"

class Producto(models.Model):
    titulo = models.CharField(max_length=150, null=False)
    descripcion = models.CharField(max_length=2000, null=False)
    precio = models.FloatField()
    imagen = models.FileField(upload_to='imagenes/', blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="producto_categoria")
    destacado = models.BooleanField(default=False, null=False)
    def __str__(self):
        return f"{self.titulo} - {self.descripcion} ({self.precio})"

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="usuario_carrito", null=True)
    productos = models.ManyToManyField(Producto)

    def todos_productos_carrito(self):
        return self.productos.all()
    
    def total_carrito(self):
         return sum([producto.precio for producto in self.productos.all()])



    
class Contacto(models.Model):
    email = models.EmailField(null=False)
    mensaje = models.CharField(max_length=150, null=False)
    def __str__(self):
        return self.email