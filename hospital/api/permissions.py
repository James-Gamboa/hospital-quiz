from rest_framework.permissions import BasePermission

class IsInGroup(BasePermission):
    """Permiso para verificar si un usuario pertenece a un grupo específico."""

    def has_permission(self, request, view):
        required_groups = getattr(view, 'required_groups', [])
        if not required_groups:
            return True

        return request.user.is_authenticated and request.user.groups.filter(name__in=required_groups).exists()