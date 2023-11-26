from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Articulo
from .forms import ArticuloForm

def home_blog(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})

def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    return render(request, 'blog/detalle_articulo.html', {'articulo': articulo})

@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            nuevo_articulo = form.save(commit=False)
            nuevo_articulo.autor = request.user
            nuevo_articulo.save()
            return redirect('blog:lista_articulos')
    else:
        form = ArticuloForm()

    return render(request, 'blog/crear_articulo.html', {'form': form})

@login_required
def editar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    if request.user == articulo.autor:
        if request.method == 'POST':
            form = ArticuloForm(request.POST, instance=articulo)
            if form.is_valid():
                form.save()
                return redirect('blog:detalle_articulo', articulo_id=articulo.pk)
        else:
            form = ArticuloForm(instance=articulo)
        return render(request, 'blog/editar_articulo.html', {'form': form})
    else:
        return redirect('blog:lista_articulos')

@login_required
def eliminar_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    if request.user == articulo.autor:
        articulo.delete()
    return redirect('blog:lista_articulos')
