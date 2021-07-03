from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.descripcion}"

class Producto(models.Model):
    titulo = models.CharField(max_length=150, null=False)
    descripcion = models.CharField(max_length=2000, null=False)
    precio = models.FloatField()
    imagen = models.FileField(upload_to='imagenes/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="producto_categoria")
    def __str__(self):
        return f"{self.titulo} - {self.descripcion} ({self.precio})"

class Carrito(models.Model):
    usuario = User
    total_carrito = models.FloatField()
    productos = models.ManyToManyField(Producto)
    
