from rest_framework import BasePermission

# the permission for the admin user, he has every permission including access to user, changing user role except to change or edit the news
class IsAdminUser(BasePermission):
    # This permission class allows access only to users with the 'admin' role.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_chief_editor
    
    # This method checks object-level permissions, ensuring that the user has the 'admin' role to access specific objects.
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.is_chief_editor
    
    # This method checks permissions for actions that do not involve specific objects, ensuring that the user has the 'admin' role to perform such actions.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_chief_editor