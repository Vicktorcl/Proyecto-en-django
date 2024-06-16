from django.urls import path
#from django.views.generic.base import TemplateView
#from django.contrib.auth import views as auth_views
from .views import inicio, ficha, ingresar, registro, nosotros, carrito
from .views import api_ropa, misdatos_cliente, misscompras, administrar_tienda
# from .views import admin_productos
# from .views import admin_usuarios, admin_bodega, ventas, boleta, ingresar, admin_usuarios
# from .views import misdatos, miscompras, salir, carrito, ficha
# from .views import cambiar_estado_boleta, poblar, obtener_productos, eliminar_producto_en_bodega
# from .views import premio, eliminar_producto_en_carrito, agregar_producto_al_carrito
# from .views import vaciar_carrito, mipassword, cambiar_password


urlpatterns = [
    path('', inicio, name='inicio'),
    path('ficha/<producto_id>', ficha, name='ficha'),
    path('ingresar', ingresar, name='ingresar'),
    path('registro', registro, name='registro'),
    path('nosotros', nosotros, name='nosotros'),
    path('api_ropa', api_ropa, name='api_ropa'),
    path('misdatos_cliente', misdatos_cliente, name='misdatos_cliente'),
    path('misscompras', misscompras, name='misscompras'),
    path('administrar_tienda', administrar_tienda, name='administrar_tienda'),
    path('carrito', carrito, name='carrito'),

    # path('admin_productos/<accion>/<id>', admin_productos, name='admin_productos'),
    # path('admin_usuarios/<accion>/<id>', admin_usuarios, name='admin_usuarios'),
    # path('cambiar_password', cambiar_password, name='cambiar_password'),
    # path('admin_bodega', admin_bodega, name='admin_bodega'),
    # path('obtener_productos', obtener_productos, name='obtener_productos'),
    # path('eliminar_producto_en_bodega/<bodega_id>', eliminar_producto_en_bodega, name='eliminar_producto_en_bodega'),
    # path('ventas', ventas, name='ventas'),
    # path('boleta/<nro_boleta>', boleta, name='boleta'),
    # path('cambiar_estado_boleta/<nro_boleta>/<estado>', cambiar_estado_boleta, name='cambiar_estado_boleta'),
    # path('misdatos', misdatos, name='misdatos'),
    # path('mipassword', mipassword, name='mipassword'),
    # path('miscompras', miscompras, name='miscompras'),
    # path('salir', salir, name='salir'),
    # path('carrito', carrito, name='carrito'),
    # path('eliminar_producto_en_carrito/<carrito_id>', eliminar_producto_en_carrito, name='eliminar_producto_en_carrito'),
    # path('vaciar_carrito', vaciar_carrito, name='vaciar_carrito'),
    # path('agregar_producto_al_carrito/<producto_id>', agregar_producto_al_carrito, name='agregar_producto_al_carrito'),
    # path('premio', premio, name='premio'),
    # path('poblar', poblar, name='poblar'),
]
