from django.urls import path
from . import views

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]