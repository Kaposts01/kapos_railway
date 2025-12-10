from django.contrib import admin
from .models import Suscripcion, EventoSuscripcion

class EventoInline(admin.TabularInline):
    model = EventoSuscripcion
    extra = 0
    readonly_fields = ('tipo', 'fecha')

@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'plan', 'estado', 'fecha_inicio', 'creado_por')
    list_filter = ('estado', 'plan')
    search_fields = ('cliente__nombre', 'cliente__rut')
    autocomplete_fields = ('cliente', 'plan', 'creado_por')
    inlines = [EventoInline]

@admin.register(EventoSuscripcion)
class EventoSuscripcionAdmin(admin.ModelAdmin):
    list_display = ('suscripcion', 'tipo', 'fecha')
    list_filter = ('tipo',)
    search_fields = ('suscripcion__cliente__nombre',)
