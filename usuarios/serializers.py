from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

Usuario = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para listar y editar usuarios sin exponer contraseñas.
    """
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'telefono', 'rut', 'rol', 'is_active',
            'creado_en', 'actualizado_en'
        ]
        read_only_fields = ['id', 'creado_en', 'actualizado_en']


class UsuarioCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para crear usuarios nuevos con:
    - Validación de contraseña
    - Hash automático
    - Validación de email único
    - Validación básica de RUT (placeholder)
    """

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    password2 = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Repita la contraseña"
    )

    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'telefono', 'rut', 'rol',
            'password', 'password2'
        ]
        read_only_fields = ['id']

    ### VALIDACIONES ###

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo ya está registrado.")
        return value

    def validate_rut(self, value):
        # (Más adelante agregamos la validación completa)
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    ### CREACIÓN SEGURA DEL USUARIO ###

    def create(self, validated_data):
        validated_data.pop('password2')

        password = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(password)  # Hash seguro
        usuario.save()

        return usuario
