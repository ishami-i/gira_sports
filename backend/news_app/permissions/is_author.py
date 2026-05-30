from rest_framework import permissions

# the permission for the author user, he has permission to create news, edit and delete his news only
class IsAuthorUser(permissions.BasePermission):
    # This permission class allows access only to users with the 'author' role.
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_author
    
    # This method checks object-level permissions, ensuring that the user has the 'author' role and is the owner of the news object to access specific objects.
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.is_author and obj.author == request.user