from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = "home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    login_url = "/login/"  # si luego agregas un login propio, actualizar aquí

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        usuario = self.request.user

        # Ejemplo simple de menú dinámico según rol
        roles_menus = {
            "ADMIN": [
                ("Usuarios", "/api/usuarios/"),
                ("Clientes", "/api/clientes/"),
                ("Planes", "/api/planes/"),
                ("Suscripciones", "/api/suscripciones/"),
                ("Pagos", "/api/pagos/"),
                ("Captación", "/api/captacion/"),
                ("Auditoría", "/api/auditoria/"),
            ],
            "ENCARGADO": [
                ("Clientes", "/api/clientes/"),
                ("Suscripciones", "/api/suscripciones/"),
                ("Pagos", "/api/pagos/"),
                ("Captación", "/api/captacion/"),
            ],
            "CAPTADOR": [
                ("Sesiones de Captación", "/api/captacion/sesiones/"),
            ],
            "DONANTE": [
                ("Mi Perfil", "/api/usuarios/me/"),
                ("Mis Suscripciones", "/api/suscripciones/"),
            ],
        }

        context["menu_items"] = roles_menus.get(usuario.rol, [])

        return context
