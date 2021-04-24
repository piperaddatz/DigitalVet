from django.shortcuts import render, redirect
from django import forms
from ..forms import CustomUserCreationForm, MascotaForm, DiagnosticoForm, ClinicaForm, MedicoForm, TrabajaForm, CustomUserChangeForm
from ..models import CustomUser, Mascota, Clinica, Diagnostico, Trabaja
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from pprint import pprint
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
    veterinarios = CustomUser.objects.filter(rol="medico")
    
    for user in users:
        clinicasUser = list(user.clinicas.all())   
        print(clinicasUser)

        clinicasNombres = []
        for c in clinicasUser:
             clinicasNombres.append(c.nombre)
        setattr(user, 'clinicasNombres', clinicasNombres)



    medicos = dict()
    for med in CustomUser.objects.filter(rol="medico"):
        medicos[med] = med.clinicas.all()

    print(medicos)

    if not request.user.is_authenticated:
        return redirect('/accounts/login/')


    return render(request, 'medicos/listado.html', {"users":users , "medicos": medicos })










def medicosClinica(request):
    
    trabaja = Trabaja.objects.get(usuario=request.user.pk) 
    medicos = CustomUser.objects.filter(rol="medico")
    medicosClinicaList = []
    

    for user in medicos:
         trabajaMedicos = Trabaja.objects.get(usuario=user)
         setattr(user, 'clinica', trabajaMedicos.clinica)
         if trabajaMedicos.clinica == trabaja.clinica:
             medicosClinicaList.append(user)



    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    print("USUARIO:", request.user.rol)

    return render(request, 'medicos/listado.html', {"users":medicosClinicaList , "trabajos":trabaja })



def medicosColegas(request):

    Tclinica = Clinica.objects.get(customuser=request.user.pk)
    users = CustomUser.objects.filter(clinicas=Tclinica)
    
    for user in users:
         clinicasUser = list(user.clinicas.all())         
         
         print(clinicasUser)
         clinicasNombres = []
         for c in clinicasUser:
             clinicasNombres.append(c.nombre)
         setattr(user, 'clinicasNombres', clinicasNombres)

    return render(request, 'medicos/colegas.html', {"users":users })

    




    


def medicoCrear(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    form = MedicoForm(request.POST, request.FILES)
    form2 = TrabajaForm(request.POST)

    clinicas = Clinica.objects.all()


    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if form.is_valid():
            print('Formulario ok')
            new_medico = CustomUser.objects.create(
                    email = form.cleaned_data["email"],
                    username = form.cleaned_data["username"],
                    rol = "medico",
                    profile_pic = form.cleaned_data["profile_pic"],                 
                )
         
            # CLINICAS
            clinicasList = form.cleaned_data["clinicas"]
            print("clinicasList:", clinicasList)

            for c in clinicasList:
                print(c)
                #clinicaFound = Clinica.objects.get(pk = c)
                new_medico.clinicas.add(c)

            new_medico.save()

        if form2.is_valid():
            print('Formulario ok')
            new_trabaja = Trabaja.objects.create(
                    usuario = User.objects.last(),
                    clinica = form2.cleaned_data["clinica"],               
                )    
              
            new_trabaja.save()


            print('medico y trabaja guardado')
            #return render(request, 'index.html', {})   
            return redirect('/medicos/listado')

        else:
            print('formulario no valido')
            form = MedicoForm()

 
    return render(request, 'medicos/crear.html', { 'form': form, 'clinicas':clinicas })



def medicoDetalle(request, idUser):
    return redirect('/medicos/listado')




def medicoEditar(request, idMedico):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    medicoFound = CustomUser.objects.get(id=idMedico)
    clinicas = list(Clinica.objects.all())
    clinicasTrabaja = medicoFound.clinicas.all()
    
    form = MedicoForm(request.POST, request.FILES)

    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if (form.is_valid()) or (form.is_valid() == False):

            medicoFound.email = request.POST.get('email')
            medicoFound.username = form.cleaned_data["username"]
            #medicoFound.profile_pic = request.FILES.get('profile_pic')

            # CLINICAS
            clinicasList = form.cleaned_data["clinicas"]
            print("clinicasList:", clinicasList)
            medicoFound.clinicas.set(clinicasList)

            medicoFound.save()
 
            return redirect('/medicos/listado')

        else:
            print("FORM NOT VALID:")
            
    form = MedicoForm()

    
    return render(request, 'medicos/editar.html', { 'form': form, 'medico': medicoFound, 'clinicas':clinicas, 'clinicasTrabaja': clinicasTrabaja })




def medicoEliminar(request, idUser):
    medicoFound = CustomUser.objects.get(id=idUser)

    medicoFound.delete()

    return redirect('/medicos/listado')





















    


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



def EditarUsuario(request, idUser):
    
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    FoundUser = CustomUser.objects.get(id=idUser)

    form = CustomUserChangeForm(request.POST, request.FILES)

    print("USUARIO:", request.user.rol)
     
    if request.method == 'POST':
        if (form.is_valid()) or (form.is_valid() == False):

            FoundUser.username = form.cleaned_data["username"]
            FoundUser.mail = request.POST.get('email')
            FoundUser.profile_pic = request.FILES.get('profile_pic')
            FoundUser.save()
 
            return redirect('/accounts/profile')

        else:
            form = CustomUserChangeForm()
            print('datos no validos')
    
    return render(request, 'registration/edit.html', { 'form': form , 'user': FoundUser })
       