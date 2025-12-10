from django.db import models
from django.conf import settings


class LogActividad(models.Model):
    """
    Registro de actividades relevantes del sistema
    (creación, actualización, eliminación, login, etc.).
    """

    ACCIONES = (
        ('CREAR', 'Crear'),
        ('ACTUALIZAR', 'Actualizar'),
        ('ELIMINAR', 'Eliminar'),
        ('LOGIN', 'Login'),
        ('OTRO', 'Otro'),
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='logs_actividad'
    )

    modelo = models.CharField(max_length=100)
    objeto_id = models.PositiveIntegerField(blank=True, null=True)

    accion = models.CharField(
        max_length=15,
        choices=ACCIONES,
        default='OTRO'
    )

    descripcion = models.TextField(blank=True, null=True)

    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True
    )

    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.accion}] {self.modelo} ({self.objeto_id})"

    class Meta:
        ordering = ['-creado_en']
        verbose_name = "Log de actividad"
        verbose_name_plural = "Logs de actividad"
