from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class Usuario(AbstractUser):
    """
    Modelo central de usuarios en el sistema KAPOS.
    Extiende AbstractUser e incluye RUT, teléfono y roles específicos.
    """

    # Roles del sistema
    ROLES = (
        ('DONANTE', 'Donante'),
        ('CAPTADOR', 'Captador'),
        ('COORDINADOR', 'Coordinador de Captadores'),
        ('GENERAL', 'Coordinador General'),
        ('ENCARGADO', 'Encargado de Área'),
        ('ADMIN', 'Administrador'),
    )

    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default='DONANTE'
    )

    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Teléfono de contacto"
    )

    rut = models.CharField(
        max_length=12,
        blank=True,
        null=True,
        unique=True,
        help_text="RUT validado con dígito verificador"
    )

    # Validación opcional de formato email
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False
    )

    # Permisos extendidos (necesarios al sobrescribir AbstractUser)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_permissions_set',
        blank=True
    )

    # Indicador de activo (ya existe en AbstractUser pero lo mantenemos)
    is_active = models.BooleanField(default=True)

    # Auditoría básica
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.rol})"

    class Meta:
        ordering = ['id']
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
