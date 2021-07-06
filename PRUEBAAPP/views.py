from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from django.contrib.auth.decorators import login_required
from PRUEBAAPP.models import Categoria, Producto, Carrito

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
   categorias = Categoria.objects.all()  
   if request.method == 'POST':
      form = FormContactoCustom(request.POST)
      if form.is_valid():
        form.save()          
        return render(request,"hola/contacto-exitoso.html", {"categorias":categorias})
   else:
      form = FormContactoCustom()
      return render(request, "hola/contacto.html", {
        'form': form,
        "categorias": categorias
      })

@login_required
def nuevo_producto(request):
      return render(request,"hola/nuevoproducto.html")

#def registrarse(request):
#      return render(request,"hola/registrarse.html")


def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()          
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {
        'form': form
        })
      
def ver_producto(request):
      return render(request,"hola/ver-producto.html")


def resultadobusqueda(request):
      return render(request,"hola/resultadobusqueda.html")

def categorias(request):
      return render(request,"hola/categorias.html")

def home(request):
      categorias = Categoria.objects.all()
      productos = Producto.objects.all()
      return render(request,"hola/home.html",
      {
            "productos": productos,
            "categorias": categorias
      })







