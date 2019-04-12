from rest_framework.permissions import BasePermission


class IsAuthenticatedForDelete(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'DELETE' and not (request.user and request.user.is_authenticated):
            return False
        return True
