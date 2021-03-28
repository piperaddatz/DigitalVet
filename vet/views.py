from django.shortcuts import render, redirect
from . import forms
from .forms import CustomUserCreationForm
from .models import CustomUser, Mascota, Clinica
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def mascotasListado(request):
    mascotas = Mascota.objects.all()
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'mascotas/listado.html', {"mascotas":mascotas})


def clinicaListado(request):
    clinicas = Clinica.objects.all()
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'clinicas/listado.html', {"clinicas":clinicas})



def medicosListado(request):
    users = CustomUser.objects.filter(rol="medico")
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'medicos/listado.html', {"users":users})



def PerfilUsuario(request):
    return render(request, 'registration/profile.html', {})

def salir(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')