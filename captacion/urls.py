from django.urls import path
from .views import (
    CaptadorListCreateView,
    CaptadorDetailView,
    PuntoCaptacionListCreateView,
    PuntoCaptacionDetailView,
    SesionCaptacionListCreateView,
    SesionCaptacionDetailView,
    RegistroCaptacionListCreateView,
    RegistroCaptacionDetailView,
)

urlpatterns = [
    # CAPTADORES
    path("captadores/", CaptadorListCreateView.as_view(), name="captadores-list"),
    path("captadores/<int:pk>/", CaptadorDetailView.as_view(), name="captadores-detail"),

    # PUNTOS
    path("puntos/", PuntoCaptacionListCreateView.as_view(), name="puntos-list"),
    path("puntos/<int:pk>/", PuntoCaptacionDetailView.as_view(), name="puntos-detail"),

    # SESIONES
    path("sesiones/", SesionCaptacionListCreateView.as_view(), name="sesiones-list"),
    path("sesiones/<int:pk>/", SesionCaptacionDetailView.as_view(), name="sesiones-detail"),

    # REGISTROS
    path("registros/", RegistroCaptacionListCreateView.as_view(), name="registros-list"),
    path("registros/<int:pk>/", RegistroCaptacionDetailView.as_view(), name="registros-detail"),
]
