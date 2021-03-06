from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from . import models
from .models import CustomUser, Mascota, Diagnostico, Clinica, Trabaja



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username', 'rol', 'clinicas')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'rol', 'clinicas')


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ('nombre', 'especie', 'raza', 'profile_pic')
        

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['nombre'].label = 'Nombre de la mascota:'
        self.fields['especie'].label = 'Especie:'
        self.fields['raza'].label = 'Raza:'
        self.fields['profile_pic'].label = 'Foto:'


class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ('titulo', 'descripcion','clinica')


class ClinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = ('nombre','direccion','email','fono','profile_pic')



class MedicoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'profile_pic', 'clinicas')      


class TrabajaForm(forms.ModelForm):
    class Meta:
        model = Trabaja
        fields = ('clinica',)  

'''
class UsuarioForm(forms.ModelForm):
    class Meta:
        fields = ('username','email','password')
        model = models.Usuario

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'})
        }

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Nombre'
        self.fields['email'].label = 'Email'
'''