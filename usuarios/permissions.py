from rest_framework.permissions import BasePermission


# ------------------------------
#  PERMISOS POR ROLES
# ------------------------------

class IsAdmin(BasePermission):
    """Permite acceso solo a usuarios con rol ADMIN."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'ADMIN'


class IsCoordinador(BasePermission):
    """Permite acceso a coordinadores generales o de captadores."""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.rol in ['COORDINADOR', 'GENERAL']
        )


class IsEncargado(BasePermission):
    """Permite acceso a encargados de área."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'ENCARGADO'


class IsCaptador(BasePermission):
    """Permite acceso a captadores."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'CAPTADOR'


class IsDonante(BasePermission):
    """
    Permite acceso a donantes para ver solo su perfil.
    (Pensado para vistas donde se use object-level permission).
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'DONANTE'

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and
            request.user.rol == 'DONANTE' and
            obj.id == request.user.id
        )


class AllowRoles(BasePermission):
    """
    Permite acceso según una lista de roles aceptados.
    Uso en las views:
        permission_classes = [AllowRoles(['ADMIN', 'ENCARGADO'])]
    o dinámicamente desde get_permissions().
    """

    def __init__(self, roles_permitidos):
        self.roles_permitidos = roles_permitidos

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.rol in self.roles_permitidos
        )
