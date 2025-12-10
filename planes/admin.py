from django.contrib import admin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'monto', 'periodicidad', 'dia_cobro', 'activo')
    list_filter = ('periodicidad', 'activo')
    search_fields = ('nombre',)
