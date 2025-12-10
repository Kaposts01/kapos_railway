from .models import LogActividad


def registrar_log(usuario, accion, modelo, objeto_id=None, descripcion=None, ip=None):
    """
    Registra un log de actividad desde cualquier app.

    Ejemplo:
        registrar_log(request.user, "CREAR", "Cliente", cliente.id)
    """
    LogActividad.objects.create(
        usuario=usuario,
        accion=accion,
        modelo=modelo,
        objeto_id=objeto_id,
        descripcion=descripcion,
        ip_address=ip,
    )
