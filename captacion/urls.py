from django.urls import path
from .views import (
    CaptadorListCreateView,
    CaptadorDetailView,
    PuntoCaptacionListCreateView,
    PuntoCaptacionDetailView
)

urlpatterns = [
    path('captadores/', CaptadorListCreateView.as_view(), name='captadores-list'),
    path('captadores/<int:pk>/', CaptadorDetailView.as_view(), name='captadores-detail'),

    path('puntos/', PuntoCaptacionListCreateView.as_view(), name='puntos-list'),
    path('puntos/<int:pk>/', PuntoCaptacionDetailView.as_view(), name='puntos-detail'),
]
