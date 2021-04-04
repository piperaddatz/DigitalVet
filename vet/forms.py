from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from . import models
from .models import CustomUser, Mascota, Diagnostico



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username', 'rol')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'rol')


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