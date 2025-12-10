from django.db import models
from django.conf import settings
from clientes.models import Cliente


class CaptadorProfile(models.Model):
    """
    Perfil de captador asociado a un Usuario con rol 'CAPTADOR'.
    """

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_captador'
    )

    codigo_interno = models.CharField(max_length=50, unique=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='captadores_supervisados'
    )

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.codigo_interno} - {self.usuario.username}"


class PuntoCaptacion(models.Model):
    """
    Lugares en donde se realiza captación (calle, mall, evento, etc.)
    """

    TIPOS = (
        ('CALLE', 'Calle'),
        ('MALL', 'Mall / Centro comercial'),
        ('EVENTO', 'Evento'),
        ('OTRO', 'Otro'),
    )

    nombre = models.CharField(max_length=150)
    tipo = models.CharField(
        max_length=10,
        choices=TIPOS,
        default='CALLE'
    )

    direccion = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"


class SesionCaptacion(models.Model):
    """
    Sesión específica de captación realizada por un captador en un punto.
    """

    captador = models.ForeignKey(
        CaptadorProfile,
        on_delete=models.CASCADE,
        related_name='sesiones'
    )

    punto = models.ForeignKey(
        PuntoCaptacion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sesiones'
    )

    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField(blank=True, null=True)

    total_contactados = models.PositiveIntegerField(default=0)
    total_interesados = models.PositiveIntegerField(default=0)
    total_suscripciones = models.PositiveIntegerField(default=0)

    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Sesión #{self.id} - {self.captador} - {self.fecha_inicio.date()}"


class RegistroCaptacion(models.Model):
    """
    Registro detallado de un contacto captado en una sesión específica.
    """

    RESULTADOS = (
        ('CONVERTIDO', 'Convertido en suscripción'),
        ('INTERESADO', 'Interesado, contacto futuro'),
        ('NO_INTERESADO', 'No interesado'),
    )

    sesion = models.ForeignKey(
        SesionCaptacion,
        on_delete=models.CASCADE,
        related_name='registros'
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='registros_captacion'
    )

    resultado = models.CharField(
        max_length=15,
        choices=RESULTADOS
    )

    comentario = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sesion} - {self.get_resultado_display()}"
