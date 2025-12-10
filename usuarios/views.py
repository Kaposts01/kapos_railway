from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer

# Lista y crea usuarios
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


# Detalle, actualización y eliminación
class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
