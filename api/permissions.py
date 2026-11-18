from rest_framework.permissions import BasePermission


class IsStaffOrReadOnly(BasePermission):
    """Allow read-only access for anyone, write access only for staff users."""

    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return request.user.is_authenticated and request.user.is_staff


class IsOwner(BasePermission):
    """Allow access only to the owner of the object."""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user