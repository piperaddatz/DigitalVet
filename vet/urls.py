from django.urls import path
from .views import views

app_name='vet'

urlpatterns = [
        path(r'', views.index, name="index"),
        path('mascotas/listado', views.mascotasListado, name="mascotas-list"),
        path('mascotas/mismascotas', views.mascotaCliente, name="mascotas-cliente"), 
        path('clinica/listado', views.clinicaListado, name="clinica-list"),
        path('medicos/listado', views.medicosListado, name="medicos-list"),
        path('diagnosticos/listado/<int:pk>/', views.diagnosticoListado, name="diagnostico-list"),
        path('diagnostico/detalle/<int:pk>', views.diagnosticoDetalle, name="diagnostico-detalle"),
        path('accounts/profile/', views.PerfilUsuario, name='perfil'),
        path('accounts/salir/', views.salir, name='salir'),
]
