from django.contrib import admin
from .models import LogActividad

@admin.register(LogActividad)
class LogActividadAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "accion", "modelo", "objeto_id", "creado_en")
    list_filter = ("accion", "modelo", "usuario")
    search_fields = ("modelo", "objeto_id", "descripcion")
    ordering = ("-creado_en",)
