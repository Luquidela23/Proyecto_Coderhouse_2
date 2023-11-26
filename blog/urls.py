from django.urls import path
from .views import home_blog, about, detalle_articulo, crear_articulo, editar_articulo, eliminar_articulo, lista_articulos

app_name = 'blog'

urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('about/', about, name='about'),
    path('pages/<int:articulo_id>/', detalle_articulo, name='detalle_articulo'),
    path('crear_articulo/', crear_articulo, name='crear_articulo'),
    path('editar_articulo/<int:articulo_id>/', editar_articulo, name='editar_articulo'),
    path('eliminar_articulo/<int:articulo_id>/', eliminar_articulo, name='eliminar_articulo'),
    path('lista_articulos/', lista_articulos, name='lista_articulos'),
]