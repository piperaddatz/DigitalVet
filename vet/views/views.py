from django.shortcuts import render, redirect
from django import forms
from ..forms import CustomUserCreationForm, MascotaForm
from ..models import CustomUser, Mascota, Clinica, Diagnostico
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def mascotasListado(request, sort):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    # sort = id, nombre, raza, especie
    mascotas = Mascota.objects.order_by(sort)

    return render(request, 'mascotas/listado.html', {"mascotas":mascotas})


def mascotasCrear(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    form = MascotaForm(request.POST)

    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if form.is_valid():

            new_mascot = Mascota.objects.create(
                    user_id = User.objects.get(pk=request.user.id),
                    nombre = form.cleaned_data["nombre"],
                    especie = form.cleaned_data["especie"],
                    raza = form.cleaned_data["raza"],
                    profile_pic = form.cleaned_data["profile_pic"],
                )
            new_mascot.save()
            #return render(request, 'index.html', {})   
            return redirect('/mascotas/listado/id')

        else:
            form = MascotaForm()

    return render(request, 'mascotas/crear.html', { 'form': form })

def mascotasEditar(request, idMascota):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    mascotaFound = Mascota.objects.get(id=idMascota)
    
    form = MascotaForm(request.POST)

    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if form.is_valid():

            mascotaFound.nombre = form.cleaned_data["nombre"]
            mascotaFound.especie = form.cleaned_data["especie"]
            mascotaFound.raza = form.cleaned_data["raza"]

            mascotaFound.save()
 
            return redirect('/mascotas/listado/id')

        else:
            form = MascotaForm()

    
    return render(request, 'mascotas/editar.html', { 'form': form, 'mascota': mascotaFound })


def mascotasEliminar(request, idMascota):
    mascotaFound = Mascota.objects.get(id=idMascota)

    mascotaFound.delete()

    return redirect('/mascotas/listado/id')

def mascotaCliente(request):
    mascotas = Mascota.objects.filter(user_id=request.user.id)
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'mascotas/listado.html', { "mascotas":mascotas })



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

    



def diagnosticoListado(request, pk):
    diagnosticos = Diagnostico.objects.filter(mascota=pk)
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'diagnosticos/diagnosticos.html', {"diagnosticos":diagnosticos})


def diagnosticoDetalle(request, pk):
    diagnosticos = Diagnostico.objects.filter(id=pk)
    diagnostico = diagnosticos[0]
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'diagnosticos/detalle.html', {"diagnostico":diagnostico})


def PerfilUsuario(request):
    return render(request, 'registration/profile.html', {})

def salir(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')