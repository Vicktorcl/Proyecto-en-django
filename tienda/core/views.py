from django.shortcuts import redirect, render
from .models import Producto
from .forms import IngresarForm

def inicio(request):
    productos = Producto.objects.all().order_by('nombre')
    data = { 'productos': productos }
    return render(request, 'core/inicio.html', data)


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

def api_ropa(request):
    return render(request, 'core/api_ropa.html')

def misdatos_cliente(request):
    return render(request, 'core/misdatos_cliente.html')

def misscompras(request):
    return render(request, 'core/misscompras.html')

def administrar_tienda(request):
    return render(request, 'core/administrar_tienda.html')

def carrito(request):
    return render(request, 'core/carrito.html')



