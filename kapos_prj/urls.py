from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', include('interfaz.urls')),
    path('admin/', admin.site.urls),

    # JWT Auth
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API
    path('api/usuarios/', include('usuarios.urls')),
    path('api/planes/', include('planes.urls')),
    path('api/suscripciones/', include('suscripciones.urls')),
    path('api/clientes/', include('clientes.urls')),
    path('api/pagos/', include('pagos.urls')),
    path('api/captacion/', include('captacion.urls')),
    # path('api/auditoria/', include('auditoria.urls')),

    

]
