from PRUEBAAPP.models import Carrito, Categoria, Contacto, Producto
from django.contrib import admin

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Carrito)