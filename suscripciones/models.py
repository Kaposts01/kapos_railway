from django.db import models
from clientes.models import Cliente
from planes.models import Plan
from usuarios.models import Usuario
from django.utils import timezone

class Suscripcion(models.Model):

    ESTADOS = (
        ('ACTIVA', 'Activa'),
        ('PAUSADA', 'Pausada'),
        ('CANCELADA', 'Cancelada'),
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='suscripciones')
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVA')

    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(blank=True, null=True)

    creado_por = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        related_name='suscripciones_creadas'
    )

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)

        EventoSuscripcion.objects.create(
            suscripcion=self,
            tipo="CREADA" if creating else "ACTUALIZADA"
        )

    def __str__(self):
        return f"Suscripción {self.id} - {self.cliente.nombre}"

class EventoSuscripcion(models.Model):
    TIPO = (
        ('CREADA', 'Creada'),
        ('ACTUALIZADA', 'Actualizada'),
        ('PAUSADA', 'Pausada'),
        ('CANCELADA', 'Cancelada'),
        ('CAMBIO_PLAN', 'Cambio de plan'),
        ('CAMBIO_FECHA', 'Cambio de fecha'),
    )

    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE, related_name='eventos')
    tipo = models.CharField(max_length=30, choices=TIPO)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} ({self.fecha})"
