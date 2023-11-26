from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, PerfilForm
from .models import Perfil

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('perfil')
    else:
        form = RegistroForm()
    return render(request, 'perfiles/registro.html')

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('perfil')
    else:
        form = AuthenticationForm()
    return render(request, 'perfiles/inicio_sesion.html', {'form': form})

@login_required
def perfil(request):
    return render(request, 'perfiles/perfil.html')

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'perfiles/editar_perfil.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')