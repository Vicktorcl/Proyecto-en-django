from django.shortcuts import redirect, render, get_object_or_404

def inicio(request):
    return render(request, "core/inicio.html")

def nosotros(request):
    return render(request, 'core/nosotros.html')

def ficha(request):
    return render(request, "core/ficha.html")

def registro(request):
    return render(request, 'core/registro.html')

def ingresar(request):
    return render(request, 'core/ingresar.html')

