from django.contrib import admin
from .models import Cliente, Direccion, ContactoExtra


class DireccionInline(admin.TabularInline):
    model = Direccion
    extra = 1


class ContactoExtraInline(admin.TabularInline):
    model = ContactoExtra
    extra = 1


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'razon_social', 'rut', 'email', 'telefono', 'estado')
    list_filter = ('estado', 'tipo', 'region')
    search_fields = ('nombre', 'apellido', 'rut', 'email')
    ordering = ('nombre',)

    inlines = [DireccionInline, ContactoExtraInline]
