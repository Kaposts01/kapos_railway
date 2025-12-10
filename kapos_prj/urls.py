from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    path('api/usuarios/', include('usuarios.urls')),
    path('api/planes/', include('planes.urls')),
    path('api/suscripciones/', include('suscripciones.urls')),
    path('api/clientes/', include('clientes.urls')),
    path('api/pagos/', include('pagos.urls')),
    path('api/captacion/', include('captacion.urls')),
    path('api/auditoria/', include('auditoria.urls')),  # si usaremos endpoints de logs
]
