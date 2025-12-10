from rest_framework import serializers
from .models import Plan, BeneficioPlan


class BeneficioPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficioPlan
        fields = [
            'id',
            'titulo',
            'descripcion',
            'orden',
        ]
        read_only_fields = ['id']


class PlanSerializer(serializers.ModelSerializer):
    """
    Serializer único para listar, crear, ver detalle y actualizar planes.
    Incluye los beneficios asociados (solo lectura).
    """
    beneficios = BeneficioPlanSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = [
            'id',
            'nombre',
            'codigo',
            'descripcion',
            'monto_mensual',
            'moneda',
            'frecuencia',
            'minimo_meses',
            'activo',
            'es_destacado',
            'beneficios',
            'creado_en',
            'actualizado_en',
        ]
        read_only_fields = ['id', 'creado_en', 'actualizado_en']
