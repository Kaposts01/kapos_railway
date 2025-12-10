from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'email', 'telefono', 'estado', 'captado_por')
    list_filter = ('estado', 'captado_por')
    search_fields = ('nombre', 'rut', 'email')
    ordering = ('nombre',)
    autocomplete_fields = ('captado_por',)
