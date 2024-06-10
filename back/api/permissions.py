from rest_framework.permissions import BasePermission


class AllowDocsPermission(BasePermission):
    def has_permission(self, request, view):
        if request.path.startswith("/docs/"):
            return True
        return request.user and request.user_is_authenticated
