from rest_framework import serializers
from .models import Banco, Mandato, Pago
from suscripciones.models import Suscripcion


# ----------------------------
# BANCO
# ----------------------------
class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = [
            'id',
            'nombre',
            'codigo_sbif',
            'swift',
            'activo',
        ]
        read_only_fields = ['id']


# ----------------------------
# MANDATO
# ----------------------------
class MandatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mandato
        fields = [
            'id',
            'suscripcion',
            'tipo',
            'banco',
            'numero_cuenta',
            'tipo_cuenta',
            'fecha_firma',
            'codigo_mandato',
            'vigente',
        ]
        read_only_fields = ['id']


# ----------------------------
# PAGO LIST
# ----------------------------
class PagoListSerializer(serializers.ModelSerializer):
    suscripcion_cliente = serializers.CharField(source='suscripcion.cliente.nombre', read_only=True)
    suscripcion_plan = serializers.CharField(source='suscripcion.plan.nombre', read_only=True)

    class Meta:
        model = Pago
        fields = [
            'id',
            'suscripcion',
            'suscripcion_cliente',
            'suscripcion_plan',
            'fecha_programada',
            'monto',
            'estado',
            'moneda',
        ]


# ----------------------------
# PAGO DETALLE
# ----------------------------
class PagoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = [
            'id',
            'suscripcion',
            'fecha_programada',
            'fecha_pago',
            'monto',
            'moneda',
            'estado',
            'medio_pago',
            'codigo_transaccion',
            'mensaje_error',
            'creado_en',
        ]
        read_only_fields = ['id', 'creado_en']


# ----------------------------
# PAGO CREATE
# ----------------------------
class PagoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = [
            'suscripcion',
            'fecha_programada',
            'monto',
            'moneda',
            'medio_pago',
        ]

    def validate_suscripcion(self, suscripcion):
        if suscripcion.estado not in ["ACTIVA", "PENDIENTE", "PAUSADA"]:
            raise serializers.ValidationError(
                "No se pueden generar pagos para suscripciones canceladas o finalizadas."
            )
        return suscripcion

    def create(self, validated_data):
        return Pago.objects.create(**validated_data)


# ----------------------------
# PAGO UPDATE
# ----------------------------
class PagoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = [
            'estado',
            'fecha_pago',
            'codigo_transaccion',
            'mensaje_error',
        ]

    def validate(self, attrs):
        estado = attrs.get("estado")

        # Reglas de negocio
        if estado == "PAGADO":
            if "fecha_pago" not in attrs:
                raise serializers.ValidationError("Un pago marcado como PAGADO debe incluir fecha_pago.")

        if estado == "RECHAZADO":
            if "mensaje_error" not in attrs:
                raise serializers.ValidationError("Debe registrar mensaje_error al rechazar un pago.")

        return attrs

    def update(self, instance, validated_data):
        # Si se marca como pagado, registrar fecha de pago si no viene
        if validated_data.get("estado") == "PAGADO" and not validated_data.get("fecha_pago"):
            from datetime import date
            validated_data["fecha_pago"] = date.today()

        return super().update(instance, validated_data)
