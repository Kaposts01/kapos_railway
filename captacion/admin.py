from django.contrib import admin
from .models import PuntoCaptacion, RegistroCaptacion

@admin.register(PuntoCaptacion)
class PuntoCaptacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'direccion', 'activo')
    list_filter = ('ciudad', 'activo')
    search_fields = ('nombre', 'ciudad')

@admin.register(RegistroCaptacion)
class RegistroCaptacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'captador', 'punto', 'fecha')
    list_filter = ('punto', 'captador')
    search_fields = ('cliente__nombre', 'captador__username')
    autocomplete_fields = ('cliente', 'captador', 'punto')
