from django.db import models
from django.conf import settings
from clientes.models import Cliente
from planes.models import Plan


class Suscripcion(models.Model):
    """
    Representa una suscripción activa de un cliente a un plan.
    """

    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('ACTIVA', 'Activa'),
        ('PAUSADA', 'Pausada'),
        ('CANCELADA', 'Cancelada'),
        ('FINALIZADA', 'Finalizada'),
    )

    METODOS_PAGO = (
        ('PAC', 'PAC'),
        ('PAT', 'PAT'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('WEBPAY', 'Webpay'),
        ('OTRO', 'Otro'),
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='suscripciones'
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        related_name='suscripciones'
    )

    estado = models.CharField(
        max_length=15,
        choices=ESTADOS,
        default='PENDIENTE'
    )

    metodo_pago = models.CharField(
        max_length=20,
        choices=METODOS_PAGO,
        default='PAC'
    )

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)

    dia_cobro = models.PositiveSmallIntegerField(
        default=5,
        help_text="Día del mes en que se intenta el cobro recurrente."
    )

    monto_actual = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Monto vigente de la suscripción."
    )

    creada_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='suscripciones_creadas'
    )

    comentario = models.TextField(blank=True, null=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Suscripción #{self.id} - {self.cliente} - {self.plan.nombre}"


class HistorialEstadoSuscripcion(models.Model):
    """
    Historial de cambios de estado de una suscripción.
    """

    suscripcion = models.ForeignKey(
        Suscripcion,
        on_delete=models.CASCADE,
        related_name='historial_estados'
    )

    estado_anterior = models.CharField(max_length=15)
    estado_nuevo = models.CharField(max_length=15)

    fecha_cambio = models.DateTimeField(auto_now_add=True)

    cambiado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    motivo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.suscripcion} {self.estado_anterior} → {self.estado_nuevo}"


class CambioPlanSuscripcion(models.Model):
    """
    Registro de cambios de plan dentro de una suscripción.
    """

    suscripcion = models.ForeignKey(
        Suscripcion,
        on_delete=models.CASCADE,
        related_name='cambios_plan'
    )

    plan_anterior = models.ForeignKey(
        Plan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cambios_desde'
    )

    plan_nuevo = models.ForeignKey(
        Plan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cambios_hacia'
    )

    fecha_cambio = models.DateTimeField(auto_now_add=True)

    cambiado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    motivo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.suscripcion} {self.plan_anterior} → {self.plan_nuevo}"
