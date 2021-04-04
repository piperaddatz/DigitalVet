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

        # MÉDICO
        path('medicos/listado', views.medicosListado, name="medicos-list"),

        # DIAGNÓSTICO
        path('diagnosticos/listado/<int:pk>/', views.diagnosticoListado, name="diagnostico-list"),
        path('diagnostico/detalle/<int:pk>', views.diagnosticoDetalle, name="diagnostico-detalle"),
        path('diagnostico/crear/<int:idMascota>', views.diagnosticoCrear, name="diagnostico-crear"),
        path('diagnostico/editar/<int:idDiagnostico>', views.diagnosticoEditar, name="diagnostico-editar"),
        path('diagnostico/eliminar/<int:idDiagnostico>', views.diagnosticoEliminar, name="diagnostico-eliminar"),

        # PERFIL
        path('accounts/profile/', views.PerfilUsuario, name='perfil'),
        path('accounts/salir/', views.salir, name='salir'),
]
