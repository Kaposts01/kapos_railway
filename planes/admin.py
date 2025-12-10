from django.contrib import admin
from .models import Plan, BeneficioPlan


class BeneficioPlanInline(admin.TabularInline):
    model = BeneficioPlan
    extra = 1


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'monto_mensual', 'moneda', 'frecuencia', 'minimo_meses', 'activo', 'es_destacado')
    list_filter = ('frecuencia', 'moneda', 'activo', 'es_destacado')
    search_fields = ('nombre', 'codigo')
    ordering = ('nombre',)

    inlines = [BeneficioPlanInline]
