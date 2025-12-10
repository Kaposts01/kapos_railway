from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

from .serializers import (
    UsuarioSerializer,
    UsuarioCreateSerializer,
)
from .permissions import AllowRoles

Usuario = get_user_model()


class MeView(APIView):
    """
    Devuelve la información del usuario autenticado.
    GET /api/usuarios/me/
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)


class UsuarioListCreateView(generics.ListCreateAPIView):
    """
    GET → Lista usuarios (solo Admin / Encargado / General)
    POST → Crear usuario (solo Admin)
    """
    queryset = Usuario.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UsuarioCreateSerializer
        return UsuarioSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            # Solo ADMIN puede crear usuarios
            return [AllowRoles(['ADMIN'])]
        # Lista solo visible para ciertos roles "de gestión"
        return [AllowRoles(['ADMIN', 'ENCARGADO', 'GENERAL'])]


class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET → Usuario puede verse a sí mismo, o perfiles vistos por roles de gestión.
    PUT/PATCH/DELETE → Solo Admin puede modificar/eliminar usuarios.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        user = self.request.user

        # Donante y Captador solo pueden ver/modificar su propio perfil
        if user.rol in ['DONANTE', 'CAPTADOR'] and obj.id != user.id:
            raise PermissionDenied("No puedes ver o modificar otros usuarios.")

        # Para métodos de escritura, solo ADMIN puede modificar/eliminar
        if self.request.method in ['PUT', 'PATCH', 'DELETE'] and user.rol != 'ADMIN':
            raise PermissionDenied("Solo un administrador puede modificar usuarios.")

        # Para otros roles (ENCARGADO, GENERAL, COORDINADOR, ADMIN) la lectura está permitida
        return obj
