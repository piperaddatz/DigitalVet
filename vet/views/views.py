from django.shortcuts import render, redirect
from django import forms
from ..forms import CustomUserCreationForm, MascotaForm, DiagnosticoForm, ClinicaForm
from ..models import CustomUser, Mascota, Clinica, Diagnostico, Trabaja
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def index(request):
    return render(request, 'index.html', {})






###########################     Views de mascotas     #######################

def mascotasListado(request, sort):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    # sort = id, nombre, raza, especie
    mascotas = Mascota.objects.order_by(sort)

    return render(request, 'mascotas/listado.html', {"mascotas":mascotas})


def mascotasCrear(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    form = MascotaForm(request.POST, request.FILES)

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


def mascotasDetalle(request, idMascota):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    
    mascotaFound = Mascota.objects.get(id=idMascota)
    
    return render(request, 'mascotas/detalle.html', {  'mascota': mascotaFound })



def mascotasEditar(request, idMascota):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    mascotaFound = Mascota.objects.get(id=idMascota)
    
    form = MascotaForm(request.POST, request.FILES)

    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if form.is_valid():

            mascotaFound.nombre = form.cleaned_data["nombre"]
            mascotaFound.especie = form.cleaned_data["especie"]
            mascotaFound.raza = form.cleaned_data["raza"]
            mascotaFound.profile_pic = request.FILES.get('profile_pic')

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




###########################     Views de Clinicas     #######################


def clinicaListado(request):
    clinicas = Clinica.objects.all()
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'clinicas/listado.html', {"clinicas":clinicas})


def clinicaCrear(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    form = ClinicaForm(request.POST)

    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if form.is_valid():

            new_clinica = Clinica.objects.create(
                    nombre = form.cleaned_data["nombre"],
                    direccion = form.cleaned_data["direccion"],
                    email = form.cleaned_data["email"],
                    fono = form.cleaned_data["fono"],
                    profile_pic = form.cleaned_data["profile_pic"],
                                )
            new_clinica.save()
            #return render(request, 'index.html', {})   
            return redirect('/clinica/listado')

        else:
            print('formulario rechazado')
            form = ClinicaForm()

    return render(request, 'clinicas/crear.html', { 'form': form })


def clinicaEditar(request, idClinica):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    clinicaFound = Clinica.objects.get(id=idClinica)
    
    form = ClinicaForm(request.POST)

    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if form.is_valid():

            clinicaFound.nombre = form.cleaned_data["nombre"]
            clinicaFound.direccion = form.cleaned_data["direccion"]
            clinicaFound.email = form.cleaned_data["email"]
            clinicaFound.fono = form.cleaned_data["fono"]
            clinicaFound.save()
 
            return redirect('/clinica/listado')

        else:
            form = clinicaForm()

    
    return render(request, 'clinicas/editar.html', { 'form': form, 'clinica': clinicaFound })



def clinicaDetalle(request, idClinica):
    clinicas = Clinica.objects.filter(id=idClinica)
    clinica = clinicas[0]
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'clinicas/detalle.html', {"clinica":clinica})




def clinicaEliminar(request, idClinica):
    clinicaFound = Clinica.objects.get(id=idClinica)

    clinicaFound.delete()

    return redirect('/clinica/listado')




###########################     Views de Medicos    #######################

def medicosListado(request):
    users = CustomUser.objects.filter(rol="medico")
    trabaja = Trabaja.objects.all()
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'medicos/listado.html', {"users":users , "trabajos":trabaja })





    


#########################    Views de Diagnosticos    #######################


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



def diagnosticoCrear(request, idMascota):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    form = DiagnosticoForm(request.POST)
    clinicas = Clinica.objects.all()


    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if form.is_valid():
            print('Formulario ok')
            new_diagnostico = Diagnostico.objects.create(
                    usuario = User.objects.get(pk=request.user.id),
                    mascota = Mascota.objects.get(pk=idMascota),
                    clinica = form.cleaned_data["clinica"],
                    titulo = form.cleaned_data["titulo"],
                    descripcion = form.cleaned_data["descripcion"],
                    
                )
            new_diagnostico.save()
            print('diagnostico guardado')
            #return render(request, 'index.html', {})   
            return redirect('/diagnosticos/listado/'+str(idMascota))

        else:
            print('formulario no valido')
            form = DiagnosticoForm()

    return render(request, 'diagnosticos/crear.html', { 'form': form, 'clinicas':clinicas })



def diagnosticoEditar(request, idDiagnostico):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    diagnosticoFound = Diagnostico.objects.get(id=idDiagnostico)
    form = DiagnosticoForm(request.POST)
    clinicas = Clinica.objects.all()
    idMascota = diagnosticoFound.mascota.id

    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if form.is_valid():

            diagnosticoFound.titulo = form.cleaned_data["titulo"]
            diagnosticoFound.descripcion = form.cleaned_data["descripcion"]
            diagnosticoFound.clinica = form.cleaned_data["clinica"]
            diagnosticoFound.save()
 
            return redirect('/diagnosticos/listado/'+str(idMascota))

        else:
            form = DiagnosticoForm()

    
    return render(request, 'diagnosticos/editar.html', { 'form': form, 'diagnostico': diagnosticoFound, 'clinicas':clinicas })




def diagnosticoEliminar(request,idDiagnostico):
    diagnosticoFound = Diagnostico.objects.get(id=idDiagnostico)
    idMascota = diagnosticoFound.mascota.id
    diagnosticoFound.delete()
    print('Id de la mascota: '+str(idMascota))
    return redirect('/diagnosticos/listado/'+str(idMascota))


def diagnosticoListadoAll(request):
    diagnosticos = Diagnostico.objects.all()
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'diagnosticos/diagnosticos.html', {"diagnosticos":diagnosticos})




###############    Views de Usuarios


def PerfilUsuario(request):
    return render(request, 'registration/profile.html', {})

def salir(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')