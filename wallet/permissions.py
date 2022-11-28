from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS




class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.user.is_authenticated and request.user.is_staff:
            return True