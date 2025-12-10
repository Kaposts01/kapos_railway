from django.contrib import admin
from .models import LogAccion

@admin.register(LogAccion)
class LogAccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'accion', 'fecha', 'ip')
    list_filter = ('usuario',)
    search_fields = ('accion', 'usuario__username')
