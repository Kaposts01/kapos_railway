from rest_framework import serializers
from .models import (
    Suscripcion,
    HistorialEstadoSuscripcion,
    CambioPlanSuscripcion
)
from clientes.models import Cliente
from planes.models import Plan


class HistorialEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstadoSuscripcion
        fields = [
            'id',
            'estado_anterior',
            'estado_nuevo',
            'fecha_cambio',
            'motivo',
            'cambiado_por',
        ]


class CambioPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CambioPlanSuscripcion
        fields = [
            'id',
            'plan_anterior',
            'plan_nuevo',
            'fecha_cambio',
            'motivo',
            'cambiado_por',
        ]


class SuscripcionListSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    cliente_rut = serializers.CharField(source='cliente.rut', read_only=True)
    plan_nombre = serializers.CharField(source='plan.nombre', read_only=True)

    class Meta:
        model = Suscripcion
        fields = [
            'id',
            'cliente',
            'cliente_nombre',
            'cliente_rut',
            'plan',
            'plan_nombre',
            'estado',
            'monto_actual',
            'metodo_pago',
            'fecha_inicio',
        ]


class SuscripcionDetailSerializer(serializers.ModelSerializer):
    historial_estados = HistorialEstadoSerializer(many=True, read_only=True)
    cambios_plan = CambioPlanSerializer(many=True, read_only=True)

    class Meta:
        model = Suscripcion
        fields = [
            'id',
            'cliente',
            'plan',
            'estado',
            'metodo_pago',
            'fecha_inicio',
            'fecha_fin',
            'dia_cobro',
            'monto_actual',
            'creada_por',
            'comentario',
            'creado_en',
            'actualizado_en',
            'historial_estados',
            'cambios_plan',
        ]


class SuscripcionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = [
            'cliente',
            'plan',
            'estado',
            'metodo_pago',
            'fecha_inicio',
            'fecha_fin',
            'dia_cobro',
            'monto_actual',
            'comentario',
        ]

    def validate(self, attrs):
        cliente = attrs["cliente"]

        # Evitar múltiples suscripciones activas del mismo cliente al mismo plan
        if Suscripcion.objects.filter(
            cliente=cliente,
            plan=attrs["plan"],
            estado__in=['ACTIVA', 'PENDIENTE']
        ).exists():
            raise serializers.ValidationError(
                "El cliente ya tiene una suscripción activa o pendiente a este plan."
            )

        return attrs

    def create(self, validated_data):
        request = self.context.get("request")
        usuario = request.user if request else None

        suscripcion = Suscripcion.objects.create(
            **validated_data,
            creada_por=usuario
        )

        # Registrar historial inicial
        HistorialEstadoSuscripcion.objects.create(
            suscripcion=suscripcion,
            estado_anterior="---",
            estado_nuevo=suscripcion.estado,
            cambiado_por=usuario
        )

        return suscripcion


class SuscripcionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = [
            'plan',
            'estado',
            'metodo_pago',
            'fecha_fin',
            'dia_cobro',
            'monto_actual',
            'comentario',
        ]

    def update(self, instance, validated_data):
        request = self.context.get("request")
        usuario = request.user if request else None

        # Cambios de estado
        if "estado" in validated_data and validated_data["estado"] != instance.estado:
            HistorialEstadoSuscripcion.objects.create(
                suscripcion=instance,
                estado_anterior=instance.estado,
                estado_nuevo=validated_data["estado"],
                cambiado_por=usuario
            )

        # Cambio de plan
        if "plan" in validated_data and validated_data["plan"] != instance.plan:
            CambioPlanSuscripcion.objects.create(
                suscripcion=instance,
                plan_anterior=instance.plan,
                plan_nuevo=validated_data["plan"],
                cambiado_por=usuario
            )

        return super().update(instance, validated_data)
