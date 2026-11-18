from rest_framework.permissions import BasePermission


class IsStaffOrReadOnly(BasePermission):
    """Allow read-only access for anyone, write access only for staff users."""

    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return request.user.is_authenticated and request.user.is_staff
