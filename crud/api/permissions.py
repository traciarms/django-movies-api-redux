from rest_framework import permissions

class IsOwnerOrSuperReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.owner == request.user:
            return True

        if request.user.is_superuser:
            return True

        # Only return False if none of the other conditions were met
        return False
