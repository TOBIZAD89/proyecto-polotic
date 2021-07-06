from PRUEBAAPP.models import Carrito, Categoria
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required

def index(request):

    categorias = Categoria.objects.all()
    return render(request,"hola/layout.html", {
          "categorias":categorias
    })

def acerca(request):
      categorias = Categoria.objects.all()
      return render(request,"hola/acercade.html",  {"categorias":categorias})

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

@permission_required('PRUEBAAPP.add_producto')
def nuevo_producto(request):
      categorias = Categoria.objects.all()  
      if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormProductoCustom(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect(reverse('PRUEBAAPP:home'))
      else:
        form = FormProductoCustom()
        return render(request,"hola/nuevoproducto.html",{
              "form": form,
              "categorias":categorias,
              "operacion": "alta"
        })


@permission_required('PRUEBAAPP.change_producto')
def editar_producto(request, producto_id):
      categorias = Categoria.objects.all()  
      if request.method == 'POST':
        un_producto = get_object_or_404(Producto, id=producto_id)
        
        # create a form instance and populate it with data from the request:
        form = FormProductoCustom(request.POST, request.FILES, instance=un_producto)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect(reverse('PRUEBAAPP:home'))
      else:
        un_producto = get_object_or_404(Producto, id=producto_id)
        form = FormProductoCustom(instance=un_producto)
        return render(request,"hola/nuevoproducto.html",{
              "form": form,
              "categorias":categorias,
              "operacion": "editar"
        })


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
      
def ver_producto(request, producto_id):
      un_producto = get_object_or_404(Producto, id=producto_id)
      return render(request,"hola/ver-producto.html", {"producto": un_producto}
      )

@permission_required('PRUEBAAPP.delete_producto')
def eliminar_producto(request, producto_id):
      un_producto = get_object_or_404(Producto, id=producto_id)
      un_producto.delete()
      return HttpResponseRedirect(reverse('PRUEBAAPP:home'))


def resultadobusqueda(request):
      categorias = Categoria.objects.all()  
      if request.method == "POST":
        valor_busqueda = request.POST["busqueda"]
        productos = Producto.objects.filter(descripcion__contains=valor_busqueda)
        return render(request,"hola/resultadobusqueda.html", {
            "productos": productos,
            "busqueda": valor_busqueda,
            "categorias": categorias
        })
      else:
        return render(request,"hola/resultadobusqueda.html", {"categorias":categorias})


def categorias(request, categoria_id):
      categorias = Categoria.objects.all()  
      productos = Producto.objects.filter(categoria=categoria_id)
      categoria = Categoria.objects.get(id=categoria_id)
      return render(request,"hola/resultadobusqueda.html", {
            "productos": productos,
            "busqueda": "Categoria " + categoria.descripcion,
            "categorias": categorias
        })

@login_required
def carrito(request):
  categorias = Categoria.objects.all()    
  try:
      un_carrito = Carrito.objects.get(usuario=request.user)
  except Carrito.DoesNotExist:
    un_carrito = Carrito.objects.create(usuario=request.user)
    un_carrito.save()   
    #un_carrito = None
  return render(request,"hola/carrito.html", {
        "carrito": un_carrito,
        "categorias": categorias,
            
  })

@login_required
def agregar_carrito(request, producto_id):
  un_producto = get_object_or_404(Producto, id=producto_id)
  un_carrito = Carrito.objects.get(usuario=request.user)
  un_carrito.productos.add(un_producto)
  un_carrito.save();
  return HttpResponseRedirect(reverse('PRUEBAAPP:carrito'))

@login_required
def eliminar_carrito(request, producto_id=None):
  un_carrito = Carrito.objects.get(usuario=request.user)
  if (producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    un_carrito.productos.remove(un_producto)
  else:
   un_carrito.productos.clear()

  un_carrito.save();
  return HttpResponseRedirect(reverse('PRUEBAAPP:carrito'))

def home(request):
      categorias = Categoria.objects.all()
      productos = Producto.objects.all()
      productos_destacados = Producto.objects.filter(destacado=True)
      return render(request,"hola/home.html", {
            "categorias": categorias,
            "productos": productos,
            "productos_destacados": productos_destacados
      })







