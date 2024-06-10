from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto

def inicio(request):
    productos = Producto.objects.all().order_by('nombre')
    data = { 'productos': productos }
    return render(request, "core/inicio.html", data)


def ficha(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    data = { 'producto': producto }
    return render(request, "core/ficha.html", data)

def nosotros(request):
    return render(request, 'core/nosotros.html')


def registro(request):
    return render(request, 'core/registro.html')

def ingresar(request):
    return render(request, 'core/ingresar.html')

