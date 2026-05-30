from rest_framework import BasePermission

# the permission for the viewer user, he has permission to view news only and create a blog posts and forum posts

class IsViewer(BasePermission):
    # This permission class allows access only to users with the 'viewer' role.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_viewer
    
    # This method checks object-level permissions, ensuring that the user has the 'viewer' role to access specific objects.
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.is_viewer
    
    # This method checks permissions for actions that do not involve specific objects, ensuring that the user has the 'viewer' role to perform such actions.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_viewer