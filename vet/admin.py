from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from . import models

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'rol', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('email', 'username', 'rol', 'is_staff', 'is_active',)
    fieldsets = (
        ('General', {'fields': ('email', 'username', 'rol', 'password', 'profile_pic')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'rol', 'profile_pic', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(models.Clinica)
admin.site.register(models.Mascota)
admin.site.register(models.Diagnostico)
admin.site.register(models.Trabaja)