from django.db import models
from usuarios.models import Usuario

class Cliente(models.Model):

    ESTADOS = (
        ('ACTIVO', 'Activo'),
        ('PAUSADO', 'Pausado'),
        ('CANCELADO', 'Cancelado'),
    )

    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    captado_por = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="clientes_captados"
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='ACTIVO'
    )

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.rut}"
