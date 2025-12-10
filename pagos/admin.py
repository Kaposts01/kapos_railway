from django.contrib import admin
from .models import Banco, Mandato, Pago


@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_sbif', 'activo')
    search_fields = ('nombre', 'codigo_sbif')


@admin.register(Mandato)
class MandatoAdmin(admin.ModelAdmin):
    list_display = ('suscripcion', 'tipo', 'banco', 'numero_cuenta', 'vigente')
    search_fields = ('numero_cuenta', 'codigo_mandato')
    list_filter = ('tipo', 'vigente', 'banco')


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('suscripcion', 'fecha_programada', 'monto', 'estado')
    list_filter = ('estado', 'fecha_programada')
    search_fields = ('codigo_transaccion',)
