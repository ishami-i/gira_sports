from rest_framework import BasePermission

# the permission for the chief editor user, he has permission to create news, edit and delete all news but he can't access to user, changing user role and delete or edit the news of other users
class IsAdmin(BasePermission):
    # This permission class allows access only to users with the 'chief editor' role.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_chief_editor
    
    # This method checks object-level permissions, ensuring that the user has the 'chief editor' role to access specific objects.
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.is_chief_editor