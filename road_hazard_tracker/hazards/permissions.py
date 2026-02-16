# hazards/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReporterOrAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        # Anyone can read
        if request.method in SAFE_METHODS:
            return True

        # Admin can do anything
        if request.user.is_staff:
            return True

        # Only reporter can update/delete
        return obj.reporter == request.user