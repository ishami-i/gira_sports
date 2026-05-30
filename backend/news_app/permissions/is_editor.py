from rest_framework import BasePermission

#  the permission for the editor user, he has permission to create news, edit and delete his news and the news of other author news but he can't access to user, changing user role and delete or edit the news of other users

class IsEditor(BasePermission):
    # This permission class allows access only to users with the 'editor' role.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_editor
    
    # This method checks object-level permissions, ensuring that the user has the 'editor' role and is either the owner of the news object or has permission to edit news objects to access specific objects.
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.is_editor and (obj.author == request.user or obj.author.is_author)
    
    # This method checks permissions for actions that do not involve specific objects, ensuring that the user has the 'editor' role to perform such actions.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_editor