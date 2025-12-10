from django.db import models


class Plan(models.Model):
    """
    Plan de aporte recurrente (PAC/PAT u otro).
    """

    FRECUENCIAS = (
        ('MENSUAL', 'Mensual'),
        ('TRIMESTRAL', 'Trimestral'),
        ('ANUAL', 'Anual'),
    )

    MONEDAS = (
        ('CLP', 'Peso chileno'),
        ('USD', 'Dólar'),
    )

    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    monto_mensual = models.DecimalField(max_digits=12, decimal_places=2)
    moneda = models.CharField(
        max_length=3,
        choices=MONEDAS,
        default='CLP'
    )

    frecuencia = models.CharField(
        max_length=15,
        choices=FRECUENCIAS,
        default='MENSUAL'
    )

    minimo_meses = models.PositiveIntegerField(default=0)

    activo = models.BooleanField(default=True)
    es_destacado = models.BooleanField(default=False)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.monto_mensual} {self.moneda}"


class BeneficioPlan(models.Model):
    """
    Lista de beneficios asociados a un plan (ej: newsletter, informes, etc.)
    """

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name='beneficios'
    )

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    orden = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.plan.nombre} - {self.titulo}"

    class Meta:
        ordering = ['orden']
