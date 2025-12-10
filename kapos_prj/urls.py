from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/usuarios/', include('usuarios.urls')),
    path('api/clientes/', include('clientes.urls')),
    path('api/planes/', include('planes.urls')),
    path('api/suscripciones/', include('suscripciones.urls')),
    path('api/captacion/', include('captacion.urls')),
    path('api/pagos/', include('pagos.urls')),
    path('api/auditoria/', include('auditoria.urls')),
]
