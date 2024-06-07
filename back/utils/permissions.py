from rest_framework.permissions import BasePermission


class ListAndRetrievePermission(BasePermission):
    def has_permission(self, request, view):
        # Permitir a cualquier usuario realizar una solicitud GET (list o retrieve)
        if view.action == "list" or view.action == "retrieve":
            return True
        # Requiere autenticación para otros métodos
        return request.user and request.user.is_authenticated


class IsAuthenticatedToViewList(BasePermission):
    """
    Custom permission to only allow authenticated users to view the list.
    """

    def has_permission(self, request, view):
        # Allow any user to view individual objects (retrieve action)
        if view.action == "retrieve":
            return True

        # Only allow authenticated users to view the list (list action)
        if view.action == "list":
            return request.user and request.user.is_authenticated

        return False
