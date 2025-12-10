from django.urls import path
from .views import PagoListCreateView, PagoDetailView

urlpatterns = [
    path('', PagoListCreateView.as_view(), name='pagos-list'),
    path('<int:pk>/', PagoDetailView.as_view(), name='pagos-detail'),
]
