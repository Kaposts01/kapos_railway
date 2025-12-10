from rest_framework import serializers
from .models import Cliente, Direccion, ContactoExtra


# -----------------------------
#  DIRECCIONES
# -----------------------------
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = [
            'id',
            'tipo',
            'direccion',
            'comuna',
            'ciudad',
            'region',
            'pais',
            'codigo_postal',
            'es_principal',
        ]
        read_only_fields = ['id']


# -----------------------------
#  CONTACTOS EXTRA
# -----------------------------
class ContactoExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoExtra
        fields = [
            'id',
            'nombre',
            'telefono',
            'email',
            'nota',
        ]
        read_only_fields = ['id']


# -----------------------------
#  CLIENTE LISTA
# -----------------------------
class ClienteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'nombre',
            'apellido',
            'razon_social',
            'rut',
            'estado',
            'creado_en',
            'actualizado_en',
        ]
        read_only_fields = fields


# -----------------------------
#  CLIENTE DETALLE
# -----------------------------
class ClienteDetailSerializer(serializers.ModelSerializer):

    direcciones = DireccionSerializer(many=True, read_only=True)
    contactos_extras = ContactoExtraSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = [
            'id',
            'usuario',
            'tipo',
            'nombre',
            'apellido',
            'razon_social',
            'rut',
            'email',
            'telefono',
            'fecha_nacimiento',
            'direccion',
            'ciudad',
            'region',
            'pais',
            'estado',
            'direcciones',
            'contactos_extras',
            'creado_en',
            'actualizado_en',
        ]
        read_only_fields = ['id', 'creado_en', 'actualizado_en']


# -----------------------------
#  CLIENTE CREATE
# -----------------------------
class ClienteCreateSerializer(serializers.ModelSerializer):

    direcciones = DireccionSerializer(many=True, required=False)
    contactos_extras = ContactoExtraSerializer(many=True, required=False)

    class Meta:
        model = Cliente
        fields = [
            'id',
            'usuario',
            'tipo',
            'nombre',
            'apellido',
            'razon_social',
            'rut',
            'email',
            'telefono',
            'fecha_nacimiento',
            'direccion',
            'ciudad',
            'region',
            'pais',
            'estado',
            'direcciones',
            'contactos_extras',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):

        direcciones_data = validated_data.pop('direcciones', [])
        contactos_data = validated_data.pop('contactos_extras', [])

        cliente = Cliente.objects.create(**validated_data)

        for d in direcciones_data:
            Direccion.objects.create(cliente=cliente, **d)

        for c in contactos_data:
            ContactoExtra.objects.create(cliente=cliente, **c)

        return cliente


# -----------------------------
#  CLIENTE UPDATE
# -----------------------------
class ClienteUpdateSerializer(serializers.ModelSerializer):

    direcciones = DireccionSerializer(many=True, required=False)
    contactos_extras = ContactoExtraSerializer(many=True, required=False)

    class Meta:
        model = Cliente
        fields = [
            'tipo',
            'nombre',
            'apellido',
            'razon_social',
            'rut',
            'email',
            'telefono',
            'fecha_nacimiento',
            'direccion',
            'ciudad',
            'region',
            'pais',
            'estado',
            'direcciones',
            'contactos_extras',
        ]

    def update(self, instance, validated_data):

        direcciones_data = validated_data.pop('direcciones', [])
        contactos_data = validated_data.pop('contactos_extras', [])

        # Actualizar campos simples
        for campo, valor in validated_data.items():
            setattr(instance, campo, valor)
        instance.save()

        # Reemplazar direcciones
        if direcciones_data:
            instance.direcciones.all().delete()
            for d in direcciones_data:
                Direccion.objects.create(cliente=instance, **d)

        # Reemplazar contactos
        if contactos_data:
            instance.contactos_extras.all().delete()
            for c in contactos_data:
                ContactoExtra.objects.create(cliente=instance, **c)

        return instance
