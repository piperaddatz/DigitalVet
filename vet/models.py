from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

# USUARIO CUSTOM
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=264)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    rol = models.CharField(max_length=12,default="cliente")
    profile_pic = models.ImageField(upload_to='user_profile',blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# CLÍNICA
class Clinica(models.Model): 
    nombre = models.CharField(max_length=50) 
    direccion = models.TextField() 
    email = models.EmailField(max_length=50) 
    fono = models.CharField(max_length=15) 
    profile_pic = models.ImageField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.nombre 

# MASCOTA
class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='mascot_profile', blank=True)
    user_id = models.ForeignKey('vet.CustomUser',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# REGISTRO DE TRABAJO PARA MÉDICOS
class Trabaja(models.Model):
    fecha = models.DateField() 
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE) 
    created_at = models.DateField(auto_now_add=True)  

    def __str__(self): 
        return "Médico trabajador" 

# DIAGNÓSTICO
class Diagnostico(models.Model): 
    titulo = models.CharField(max_length=50) 
    descripcion = models.TextField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE) 
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE) 
    created_at = models.DateField(auto_now_add=True)
 
    def __str__(self): 
        return self.titulo     