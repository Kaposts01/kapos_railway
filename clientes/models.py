from django.db import models
from django.conf import settings


class Cliente(models.Model):
    """
    Representa a un donante/cliente del sistema.
    Puede estar vinculado o no a un Usuario (cuenta web).
    """

    TIPO_CLIENTE = (
        ('PERSONA', 'Persona natural'),
        ('EMPRESA', 'Empresa / Razón social'),
    )

    ESTADOS = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
    )

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cliente'
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE,
        default='PERSONA'
    )

    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    razon_social = models.CharField(max_length=200, blank=True, null=True)

    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)

    fecha_nacimiento = models.DateField(blank=True, null=True)

    direccion = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, default='Chile')

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='ACTIVO'
    )

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.tipo == 'EMPRESA' and self.razon_social:
            return f"{self.razon_social} ({self.rut})"
        return f"{self.nombre} {self.apellido} ({self.rut})".strip()


class Direccion(models.Model):

    TIPO_DIRECCION = (
        ('PRINCIPAL', 'Principal'),
        ('FACTURACION', 'Facturación'),
        ('OTRA', 'Otra'),
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='direcciones'
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_DIRECCION,
        default='PRINCIPAL'
    )

    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, default='Chile')
    codigo_postal = models.CharField(max_length=20, blank=True, null=True)

    es_principal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente} - {self.direccion}"


class ContactoExtra(models.Model):

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='contactos_extras'
    )

    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.cliente})"
