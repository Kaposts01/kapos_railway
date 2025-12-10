from django.db import models
from suscripciones.models import Suscripcion


class Banco(models.Model):
    """
    Catálogo de bancos para mandatos PAC/PAT.
    """

    nombre = models.CharField(max_length=150)
    codigo_sbif = models.CharField(max_length=10, blank=True, null=True)
    swift = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Mandato(models.Model):
    """
    Información del mandato firmado por el donante.
    """

    TIPOS = (
        ('PAC', 'PAC'),
        ('PAT', 'PAT'),
    )

    suscripcion = models.OneToOneField(
        Suscripcion,
        on_delete=models.CASCADE,
        related_name='mandato'
    )

    tipo = models.CharField(
        max_length=3,
        choices=TIPOS,
        default='PAC'
    )

    banco = models.ForeignKey(
        Banco,
        on_delete=models.PROTECT,
        related_name='mandatos'
    )

    numero_cuenta = models.CharField(max_length=50)
    tipo_cuenta = models.CharField(max_length=50, blank=True, null=True)

    fecha_firma = models.DateField()
    codigo_mandato = models.CharField(max_length=100, blank=True, null=True)

    vigente = models.BooleanField(default=True)

    def __str__(self):
        return f"Mandato {self.tipo} - {self.suscripcion_id}"


class Pago(models.Model):
    """
    Registro de pagos asociados a una suscripción.
    """

    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('PAGADO', 'Pagado'),
        ('RECHAZADO', 'Rechazado'),
        ('ANULADO', 'Anulado'),
    )

    suscripcion = models.ForeignKey(
        Suscripcion,
        on_delete=models.CASCADE,
        related_name='pagos'
    )

    fecha_programada = models.DateField()
    fecha_pago = models.DateField(blank=True, null=True)

    monto = models.DecimalField(max_digits=12, decimal_places=2)
    moneda = models.CharField(max_length=3, default='CLP')

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='PENDIENTE'
    )

    medio_pago = models.CharField(max_length=50, blank=True, null=True)
    codigo_transaccion = models.CharField(max_length=100, blank=True, null=True)

    mensaje_error = models.TextField(blank=True, null=True)

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago #{self.id} - {self.suscripcion_id} - {self.estado}"
