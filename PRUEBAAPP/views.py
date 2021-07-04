from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *

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
      return render(request,"hola/home.html")







