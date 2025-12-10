from rest_framework import generics, permissions
from .models import Plan
from .serializers import PlanSerializer


class PlanListCreateView(generics.ListCreateAPIView):
    """
    GET  → Lista todos los planes activos/inactivos
    POST → Crea un nuevo plan de aportes
    """
    queryset = Plan.objects.all().order_by('id')
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    → Detalle de un plan (incluye beneficios)
    PUT    → Actualiza plan completo
    PATCH  → Actualiza parcialmente
    DELETE → Elimina el plan
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAuthenticated]
