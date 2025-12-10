from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from .serializers import (
    UsuarioSerializer,
    UsuarioCreateSerializer
)

Usuario = get_user_model()


# ============================
# LISTAR Y CREAR USUARIOS
# ============================

class UsuarioListCreateView(generics.ListCreateAPIView):
    """
    GET → Lista de usuarios
    POST → Crear un usuario nuevo
    """
    queryset = Usuario.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UsuarioCreateSerializer
        return UsuarioSerializer

    # permisos básicos (luego agregaremos roles)
    permission_classes = [permissions.AllowAny]


# ============================
# DETALLE, ACTUALIZAR y ELIMINAR
# ============================

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET → Obtener usuario
    PUT/PATCH → Actualizar usuario
    DELETE → Eliminar usuario
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]
