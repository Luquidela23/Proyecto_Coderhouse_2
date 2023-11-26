from django.urls import path
from .views import registro, inicio_sesion, perfil, editar_perfil, cerrar_sesion

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]