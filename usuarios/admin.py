from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'rut', 'rol', 'is_active')
    list_filter = ('rol', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'rut')
    ordering = ('username',)

    fieldsets = (
        ("Información básica", {
            "fields": ("username", "password")
        }),
        ("Información personal", {
            "fields": ("first_name", "last_name", "email", "rut", "telefono")
        }),
        ("Rol y permisos", {
            "fields": ("rol", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
    )
