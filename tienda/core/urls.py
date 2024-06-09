from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from .views import inicio, registro, nosotros, ficha, ingresar


urlpatterns = [
    path('', inicio, name="core/inicio"),
    path('ficha', ficha, name="core/ficha"),
    path('registro', registro, name="core/registro"),
    path('nosotros', nosotros, name="core/nosotros"),
    path('ingresar', ingresar, name="core/ingresar")
]
