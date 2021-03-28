from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from .models import CustomUser

from . import models

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username', 'rol')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'rol')




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