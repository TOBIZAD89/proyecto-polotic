from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"hola/index.html")

#
#def index(request): 
#      return HttpResponse("hola bienvenidos")

def plantilla(request):
        return render(request,"hola/index.html")

def acerca(request):
        return render(request,"hola/acercade.html")

def contactos(request):
        return render(request,"hola/contacto.html")

def nuevo_producto(request):
      return render(request,"hola/nuevoproducto.html")

def login(request):
      return render(request,"hola/login.html")

def registrarse(request):
      return render(request,"hola/registrarse.html")
      
def ver_producto(request):
      return render(request,"hola/ver-producto.html")


def resultadobusqueda(request):
      return render(request,"hola/resultadobusqueda.html")

def categorias(request):
      return render(request,"hola/categorias.html")

def home(request):
      return render(request,"hola/home.html")







