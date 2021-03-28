from django.urls import path
from . import views

app_name='vet'

urlpatterns = [
        path(r'', views.index, name="index"),
        path('mascotas/listado', views.mascotasListado, name="mascotas-list"),
        path('clinica/listado', views.clinicaListado, name="clinica-list"),
        path('medicos/listado', views.medicosListado, name="medicos-list"),
        path('accounts/profile/', views.PerfilUsuario, name='perfil'),
        path('accounts/salir/', views.salir, name='salir'),
]
