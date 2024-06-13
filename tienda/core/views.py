<<<<<<< HEAD
from django.shortcuts import redirect, render
from .models import Producto
from .forms import IngresarForm
=======
from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto
>>>>>>> 179383a4078bfb7cd33f8256051d58e87a1e9d02

def inicio(request):
    productos = Producto.objects.all().order_by('nombre')
    data = { 'productos': productos }
<<<<<<< HEAD
    return render(request, 'core/inicio.html', data)
=======
    return render(request, "core/inicio.html", data)


def ficha(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    data = { 'producto': producto }
    return render(request, "core/ficha.html", data)
>>>>>>> 179383a4078bfb7cd33f8256051d58e87a1e9d02


def ficha(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    data = { 'producto': producto }
    return render(request, 'core/ficha.html', data)

def ingresar(request):
    # if request.user.is_authenticated:
    #     return redirect(index)
    form = IngresarForm()
    
    if request.method == 'POST':
        form = IngresarForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #hacer despues
            
    return render(request, 'core/ingresar.html', {
        'form': IngresarForm(),
    })
        

        
def nosotros(request):
    return render(request, 'core/nosotros.html')


def registro(request):
    return render(request, 'core/registro.html')



