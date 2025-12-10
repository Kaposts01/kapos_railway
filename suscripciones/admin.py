from django.contrib import admin
from .models import Suscripcion, HistorialEstadoSuscripcion, CambioPlanSuscripcion


@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "plan", "estado", "fecha_inicio", "metodo_pago")
    list_filter = ("estado", "metodo_pago")
    search_fields = ("cliente__nombre", "cliente__apellido", "cliente__rut", "plan__nombre")


@admin.register(HistorialEstadoSuscripcion)
class HistorialEstadoAdmin(admin.ModelAdmin):
    list_display = ("suscripcion", "estado_anterior", "estado_nuevo", "fecha_cambio")
    list_filter = ("estado_anterior", "estado_nuevo")


@admin.register(CambioPlanSuscripcion)
class CambioPlanAdmin(admin.ModelAdmin):
    list_display = ("suscripcion", "plan_anterior", "plan_nuevo", "fecha_cambio")
    list_filter = ("plan_anterior", "plan_nuevo")
