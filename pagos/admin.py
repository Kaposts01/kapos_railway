from django.contrib import admin
from .models import Banco, Mandato, AporteMensual

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')
    search_fields = ('nombre', 'codigo')


@admin.register(Mandato)
class MandatoAdmin(admin.ModelAdmin):
    list_display = ('suscripcion', 'tipo', 'banco', 'cuenta')
    list_filter = ('tipo', 'banco')
    search_fields = ('suscripcion__cliente__nombre', 'cuenta')
    autocomplete_fields = ('suscripcion', 'banco')


@admin.register(AporteMensual)
class AporteMensualAdmin(admin.ModelAdmin):
    list_display = ('suscripcion', 'fecha', 'monto', 'exito')
    list_filter = ('exito',)
    search_fields = ('suscripcion__cliente__nombre',)
    autocomplete_fields = ('suscripcion',)
