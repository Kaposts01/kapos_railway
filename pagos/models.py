from django.db import models
from suscripciones.models import Suscripcion

class Banco(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

class Mandato(models.Model):
    TIPO = (
        ('PAC', 'PAC'),
        ('PAT', 'PAT'),
    )

    suscripcion = models.OneToOneField(Suscripcion, on_delete=models.CASCADE, related_name='mandato')
    tipo = models.CharField(max_length=5, choices=TIPO)
    banco = models.ForeignKey(Banco, on_delete=models.PROTECT)
    cuenta = models.CharField(max_length=50)
    fecha_firma = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.suscripcion.id}"

class AporteMensual(models.Model):
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE, related_name='aportes')
    fecha = models.DateField()
    monto = models.PositiveIntegerField()
    exito = models.BooleanField(default=True)

    def __str__(self):
        return f"Aporte {self.fecha} - {'OK' if self.exito else 'ERROR'}"
