from rest_framework import generics, permissions
from .models import Pago
from .serializers import (
    PagoListSerializer,
    PagoDetailSerializer,
    PagoCreateSerializer,
    PagoUpdateSerializer
)


class PagoListCreateView(generics.ListCreateAPIView):
    """
    GET  → Lista todos los pagos
    POST → Crea un pago programado asociado a una suscripción
    """
    queryset = Pago.objects.all().order_by('-creado_en')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PagoListSerializer
        return PagoCreateSerializer


class PagoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    → Detalle de pago
    PUT    → Actualizar (estado, mensaje_error, cod transacción)
    PATCH  → Actualización parcial
    DELETE → Eliminar
    """
    queryset = Pago.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PagoDetailSerializer
        return PagoUpdateSerializer
