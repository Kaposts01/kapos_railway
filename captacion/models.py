from django.db import models
from usuarios.models import Usuario
from clientes.models import Cliente

class PuntoCaptacion(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=100)

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class RegistroCaptacion(models.Model):
    captador = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'CAPTADOR'})
    punto = models.ForeignKey(PuntoCaptacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.captador.username}"
