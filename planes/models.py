from django.db import models

class Plan(models.Model):

    PERIODICIDAD = (
        ('MENSUAL', 'Mensual'),
        ('TRIMESTRAL', 'Trimestral'),
        ('ANUAL', 'Anual'),
    )

    nombre = models.CharField(max_length=100)
    monto = models.PositiveIntegerField()
    periodicidad = models.CharField(max_length=20, choices=PERIODICIDAD)
    dia_cobro = models.PositiveIntegerField(default=5)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} (${self.monto})"
