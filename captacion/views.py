from rest_framework import generics, permissions
from .models import (
    CaptadorProfile,
    PuntoCaptacion,
    SesionCaptacion,
    RegistroCaptacion
)
from .serializers import (
    CaptadorSerializer,
    PuntoCaptacionSerializer,
    SesionCaptacionSerializer,
    RegistroCaptacionSerializer
)


# -----------------------------
# CAPTADORES
# -----------------------------
class CaptadorListCreateView(generics.ListCreateAPIView):
    queryset = CaptadorProfile.objects.all().order_by("codigo_interno")
    serializer_class = CaptadorSerializer
    permission_classes = [permissions.IsAuthenticated]


class CaptadorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CaptadorProfile.objects.all()
    serializer_class = CaptadorSerializer
    permission_classes = [permissions.IsAuthenticated]


# -----------------------------
# PUNTOS DE CAPTACIÓN
# -----------------------------
class PuntoCaptacionListCreateView(generics.ListCreateAPIView):
    queryset = PuntoCaptacion.objects.all().order_by("nombre")
    serializer_class = PuntoCaptacionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PuntoCaptacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PuntoCaptacion.objects.all()
    serializer_class = PuntoCaptacionSerializer
    permission_classes = [permissions.IsAuthenticated]


# -----------------------------
# SESIONES DE CAPTACIÓN
# -----------------------------
class SesionCaptacionListCreateView(generics.ListCreateAPIView):
    queryset = SesionCaptacion.objects.all().order_by("-fecha_inicio")
    serializer_class = SesionCaptacionSerializer
    permission_classes = [permissions.IsAuthenticated]


class SesionCaptacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SesionCaptacion.objects.all()
    serializer_class = SesionCaptacionSerializer
    permission_classes = [permissions.IsAuthenticated]


# -----------------------------
# REGISTROS DE CAPTACIÓN
# -----------------------------
class RegistroCaptacionListCreateView(generics.ListCreateAPIView):
    queryset = RegistroCaptacion.objects.all().order_by("-creado_en")
    serializer_class = RegistroCaptacionSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegistroCaptacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegistroCaptacion.objects.all()
    serializer_class = RegistroCaptacionSerializer
    permission_classes = [permissions.IsAuthenticated]
