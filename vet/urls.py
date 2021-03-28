from django.urls import path
from . import views

app_name='users'

urlpatterns = [
        path(r'', views.index, name="index"),
        path('mascotas/listado', views.mascotasListado, name="mascotas"),
        path('accounts/profile/', views.PerfilUsuario, name='perfil'),
        path('accounts/salir/', views.salir, name='salir'),
]
