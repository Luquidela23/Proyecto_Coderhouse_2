from django.shortcuts import render, get_object_or_404
from .models import Articulo
from .forms import ArticuloForm

def home_blog(request):
    # Muestra la lista de artículos en la página de inicio
    articulos = Articulo.objects.all()
    return render(request, 'blog/home_blog.html', {'articulos': articulos})

def about(request):
    # Página de "Acerca de"
    return render(request, 'blog/about.html')

def detalle_articulo(request, articulo_id):
    # Detalle de un artículo específico
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    return render(request, 'blog/detalle_articulo.html', {'articulo': articulo})

def crear_articulo(request):
    # Crear un nuevo artículo
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/articulo_creado.html')
    else:
        form = ArticuloForm()
    return render(request, 'blog/crear_articulo.html', {'form': form})

def editar_articulo(request, articulo_id):
    # Editar un artículo existente
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return render(request, 'blog/articulo_editado.html')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'blog/editar_articulo.html', {'form': form, 'articulo': articulo})

def eliminar_articulo(request, articulo_id):
    # Eliminar un artículo
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    if request.method == 'POST':
        articulo.delete()
        return render(request, 'blog/articulo_eliminado.html')
    return render(request, 'blog/eliminar_articulo.html', {'articulo': articulo})

def lista_articulos(request):
    # Lista de todos los artículos
    articulos = Articulo.objects.all()
    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})
