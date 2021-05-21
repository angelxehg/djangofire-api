from rest_framework import permissions
from projectmin.models import Project, Task


class IsOwner(permissions.BasePermission):
    message = "No eres owner del objeto"

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            # Interceptar metodo POST
            return False
        if isinstance(obj, Project):
            # Si la instancia es Project
            return obj.owner == request.user
        if isinstance(obj, Task):
            # Si la instancia es Project
            return obj.project.owner == request.user
        return False
