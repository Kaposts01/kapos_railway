from rest_framework import generics, permissions
from .models import LogActividad
from .serializers import LogActividadSerializer


class LogListView(generics.ListAPIView):
    """
    Lista de logs de auditoría, con filtros opcionales:
    ?modelo=Cliente
    ?accion=CREAR
    ?usuario=15
    """
    queryset = LogActividad.objects.all().order_by("-creado_en")
    serializer_class = LogActividadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        modelo = self.request.query_params.get("modelo")
        accion = self.request.query_params.get("accion")
        usuario = self.request.query_params.get("usuario")

        if modelo:
            qs = qs.filter(modelo=modelo)

        if accion:
            qs = qs.filter(accion=accion)

        if usuario:
            qs = qs.filter(usuario_id=usuario)

        return qs
