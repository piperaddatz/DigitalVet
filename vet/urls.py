from django.urls import path
from .views import views

app_name='vet'

urlpatterns = [
        # INICIO
        path(r'', views.index, name="index"),

        # MASCOTA
        path('mascotas/listado/<str:sort>', views.mascotasListado, name="mascotas-list"),
        path('mascotas/mismascotas', views.mascotaCliente, name="mascotas-cliente"),
        path('mascotas/crear', views.mascotasCrear, name="mascotas-crear"),
        path('mascotas/detalle/<int:idMascota>', views.mascotasDetalle, name="mascotas-detalle"),
        path('mascotas/editar/<int:idMascota>', views.mascotasEditar, name="mascotas-editar"),
        path('mascotas/eliminar/<int:idMascota>', views.mascotasEliminar, name="mascotas-eliminar"),

        # CLÍNICA
        path('clinica/listado', views.clinicaListado, name="clinica-list"),
        path('clinica/crear', views.clinicaCrear, name="clinica-crear"),
        path('clinica/editar/<int:idClinica>', views.clinicaEditar, name="clinica-editar"),
        path('clinica/detalle/<int:idClinica>', views.clinicaDetalle, name="clinica-detalle"),
        path('clinica/eliminar/<int:idClinica>', views.clinicaEliminar, name="clinica-eliminar"),

        # MÉDICO
        path('medicos/listado', views.medicosListado, name="medicos-list"),
        path('medicos/Clinica', views.medicosColegas, name="medicos-clinica"),
        path('medicos/crear', views.medicoCrear, name="medico-crear"),
        path('medicos/detalle/<int:idMedico>', views.medicoDetalle, name="medico-detalle"),
        path('medicos/editar/<int:idMedico>', views.medicoEditar, name="medico-editar"),
        path('medicos/eliminar/<int:idUser>', views.medicoEliminar, name="medico-eliminar"),
        path('medicos/colegas', views.medicosColegas, name="medicos-colega"),

        # DIAGNÓSTICO
        path('diagnosticos/listado/<int:pk>/', views.diagnosticoListado, name="diagnostico-list"),
        path('diagnostico/detalle/<int:pk>', views.diagnosticoDetalle, name="diagnostico-detalle"),
        path('diagnostico/crear/<int:idMascota>', views.diagnosticoCrear, name="diagnostico-crear"),
        path('diagnostico/editar/<int:idDiagnostico>', views.diagnosticoEditar, name="diagnostico-editar"),
        path('diagnostico/eliminar/<int:idDiagnostico>', views.diagnosticoEliminar, name="diagnostico-eliminar"),
        path('diagnosticos/listado/', views.diagnosticoListadoAll, name="diagnosticos-list-all"),

        # PERFIL
        path('accounts/profile/', views.PerfilUsuario, name='perfil'),
        path('accounts/edit/<int:idUser>', views.EditarUsuario, name='editar-perfil'),
        path('accounts/salir/', views.salir, name='salir'),
]
