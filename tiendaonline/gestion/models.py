from django.db import models

# Create your models here.
Class Clientes(models.model):
    nombre=models.charfield(max_length=30)
    direccion=models.charfield(max_length=50)
    email=models.emailfield()
    tfno=models.charfield(max_length=7)
    
Class articulos(models.model):
    nombre=models.charfield(max_length=30)
    seccion=modelscharfield(max_length=30)

Class Pedidos(models.model):
    numero=models.integrefield()
    fecha=models.datefield()
    entregado=models.booleanfield()




