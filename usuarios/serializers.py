from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

Usuario = get_user_model()


class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'rol', 'is_active',
            'creado_en', 'actualizado_en'
        ]
        read_only_fields = fields


class UsuarioDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'telefono', 'rut', 'rol', 'is_active',
            'creado_en', 'actualizado_en'
        ]
        read_only_fields = ['id', 'creado_en', 'actualizado_en']


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer unificado para listar y obtener detalle de usuarios
    en la API. Es el que usan las vistas principales.
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
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'telefono', 'rut', 'rol',
            'password', 'password2'
        ]
        read_only_fields = ['id']

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo ya está registrado.")
        return value

    def validate_rut(self, value):
        if value:
            if Usuario.objects.filter(rut=value).exists():
                raise serializers.ValidationError("Este RUT ya está registrado.")

            # Normalización simple del RUT (la validación completa la podemos
            # implementar luego si quieres traer la función 100% real)
            value = value.replace(".", "").replace("-", "").upper()
            if len(value) < 8:
                raise serializers.ValidationError("RUT inválido.")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()

        return usuario


class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'email', 'first_name', 'last_name',
            'telefono', 'rut', 'rol', 'is_active'
        ]


class CambiarPasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True,
        validators=[validate_password]
    )

    def validate(self, attrs):
        usuario = self.context['request'].user

        if not usuario.check_password(attrs['old_password']):
            raise serializers.ValidationError({"old_password": "Contraseña incorrecta."})

        return attrs

    def save(self):
        usuario = self.context['request'].user
        usuario.set_password(self.validated_data['new_password'])
        usuario.save()
        return usuario
