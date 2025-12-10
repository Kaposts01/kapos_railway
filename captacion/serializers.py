from rest_framework import serializers
from .models import (
    CaptadorProfile,
    PuntoCaptacion,
    SesionCaptacion,
    RegistroCaptacion
)
from usuarios.models import Usuario
from clientes.models import Cliente


# -----------------------------
# CAPTADOR
# -----------------------------
class CaptadorSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source="usuario.username", read_only=True)
    usuario_email = serializers.CharField(source="usuario.email", read_only=True)

    class Meta:
        model = CaptadorProfile
        fields = [
            "id",
            "usuario",
            "usuario_username",
            "usuario_email",
            "codigo_interno",
            "fecha_ingreso",
            "activo",
            "supervisor",
            "observaciones",
        ]
        read_only_fields = ["id"]


# -----------------------------
# PUNTO DE CAPTACIÓN
# -----------------------------
class PuntoCaptacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoCaptacion
        fields = [
            "id",
            "nombre",
            "tipo",
            "direccion",
            "ciudad",
            "region",
            "activo",
        ]
        read_only_fields = ["id"]


# -----------------------------
# SESIÓN DE CAPTACIÓN
# -----------------------------
class SesionCaptacionSerializer(serializers.ModelSerializer):
    captador_codigo = serializers.CharField(source="captador.codigo_interno", read_only=True)

    class Meta:
        model = SesionCaptacion
        fields = [
            "id",
            "captador",
            "captador_codigo",
            "punto",
            "fecha_inicio",
            "fecha_fin",
            "total_contactados",
            "total_interesados",
            "total_suscripciones",
            "notas",
        ]
        read_only_fields = ["id"]


# -----------------------------
# REGISTRO INDIVIDUAL DE CAPTACIÓN
# -----------------------------
class RegistroCaptacionSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source="cliente.nombre", read_only=True)

    class Meta:
        model = RegistroCaptacion
        fields = [
            "id",
            "sesion",
            "cliente",
            "cliente_nombre",
            "resultado",
            "comentario",
            "creado_en",
        ]
        read_only_fields = ["id", "creado_en"]
