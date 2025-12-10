from rest_framework import serializers
from .models import LogActividad
from usuarios.models import Usuario


class LogActividadSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source="usuario.username", read_only=True)

    class Meta:
        model = LogActividad
        fields = [
            "id",
            "usuario",
            "usuario_username",
            "accion",
            "modelo",
            "objeto_id",
            "descripcion",
            "ip_address",
            "creado_en",
        ]
        read_only_fields = ["id", "creado_en"]
