from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
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

    telefono = models.CharField(max_length=20, blank=True, null=True)
    rut = models.CharField(max_length=15, blank=True, null=True, unique=True)

    # Mantener compatibilidad con grupos/permisos
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

    def __str__(self):
        return f"{self.username} ({self.rol})"
