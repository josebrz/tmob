from rest_framework import permissions

class ActionBasedPermission(permissions.IsAuthenticatedOrReadOnly):
    """
    Grant or deny access to a view, based on a mapping
    in view.action_permissions
    """

    def has_permission(self, request, view):
        for key_class, actions in getattr(
                view, 'action_permissions', {}).items():
            if view.action in actions:
                permission = getattr(permissions, key_class)
                return permission.has_permission(
                    self, request=request, view=view)
        return False