from django.contrib import admin
from .models import (
    CaptadorProfile,
    PuntoCaptacion,
    SesionCaptacion,
    RegistroCaptacion
)


@admin.register(CaptadorProfile)
class CaptadorAdmin(admin.ModelAdmin):
    list_display = ("codigo_interno", "usuario", "activo", "fecha_ingreso", "supervisor")
    list_filter = ("activo", "supervisor")
    search_fields = ("codigo_interno", "usuario__username")


@admin.register(PuntoCaptacion)
class PuntoCaptacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'direccion', 'activo')
    list_filter = ('ciudad', 'activo')
    search_fields = ('nombre', 'ciudad')


@admin.register(SesionCaptacion)
class SesionCaptacionAdmin(admin.ModelAdmin):
    list_display = ("captador", "punto", "fecha_inicio", "fecha_fin", "total_contactados")
    list_filter = ("punto", "captador")
    search_fields = ("captador__usuario__username",)


@admin.register(RegistroCaptacion)
class RegistroCaptacionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'captador', 'punto', 'fecha', 'resultado')
    list_filter = ('resultado',)
    autocomplete_fields = ('cliente',)

    def captador(self, obj):
        return obj.sesion.captador

    def punto(self, obj):
        return obj.sesion.punto

    def fecha(self, obj):
        return obj.sesion.fecha_inicio.date()
