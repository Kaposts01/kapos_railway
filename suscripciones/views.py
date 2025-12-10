from rest_framework import generics, permissions
from .models import Suscripcion
from .serializers import (
    SuscripcionListSerializer,
    SuscripcionDetailSerializer,
    SuscripcionCreateSerializer,
    SuscripcionUpdateSerializer
)


class SubscripcionListCreateView(generics.ListCreateAPIView):
    queryset = Suscripcion.objects.all().order_by('-creado_en')
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SuscripcionListSerializer
        return SuscripcionCreateSerializer

    def perform_create(self, serializer):
        serializer.save(creada_por=self.request.user)


class SubscripcionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Suscripcion.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SuscripcionDetailSerializer
        return SuscripcionUpdateSerializer
