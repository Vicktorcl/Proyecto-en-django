from .models import Producto, Boleta
from .forms import IngresarForm, ProductoForm
from django.shortcuts import redirect, render
from django.contrib import messages


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
        'form': form(),
    })
        
def productos(request, accion, id):
    
    if request.method == 'POST':
        if accion == 'crear':
            form = ProductoForm(request.POST, request.FILES)
        elif accion == 'actualizar':
            form = ProductoForm(request.POST, request.FILES, instance=Producto.objects.get(id=id))
        if form.is_valid():
            producto = form.save()
            ProductoForm(instance=producto)
            messages.success(request, f'El producto "{str(producto)}" se logró {accion} correctamente')
            return redirect (productos, 'actualizar', producto.id)
        else:
            messages.error(request, 'El producto no se pudo guardar correctamente')
    if request.method == 'GET':
        if accion == 'crear':
            form = ProductoForm()
        elif accion == 'actualizar':
            form = ProductoForm(instance=Producto.objects.get(id=id))
        elif accion == 'eliminar':
            Producto.objects.get(id=id).delete()
            messages.success(request, 'El producto fue eliminado correctamente')
            return redirect(productos, 'crear', 0)
    
    
    lista = Producto.objects.all()
    return render(request, 'core/productos.html', {
        'form': form,
        'productos': lista
                    })
        
def nosotros(request):
    return render(request, 'core/nosotros.html',)


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

def boleta(request):
    return render(request, 'core/boleta.html')

def ventas(request):
    return render(request, 'core/ventas.html')



def bodega(request):
    return render(request, 'core/bodega.html')

def mantenedor_usuarios(request):
    return render(request, 'core/mantenedor_usuarios.html')
    