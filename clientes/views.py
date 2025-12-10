from rest_framework import generics, permissions
from .models import Cliente
from .serializers import (
    ClienteListSerializer,
    ClienteDetailSerializer,
    ClienteCreateSerializer,
    ClienteUpdateSerializer
)


class ClienteListCreateView(generics.ListCreateAPIView):

    queryset = Cliente.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ClienteListSerializer
        return ClienteCreateSerializer


class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Cliente.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ClienteDetailSerializer
        return ClienteUpdateSerializer
