from django.urls import path
from .views import (
    SubscripcionListCreateView,
    SubscripcionDetailView
)

urlpatterns = [
    path('', SubscripcionListCreateView.as_view(), name='subs-list'),
    path('<int:pk>/', SubscripcionDetailView.as_view(), name='subs-detail'),
]
