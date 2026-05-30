import re
from django.contrib.auth.hashers import make_password
from ..models.user import User

# Service functions for users

# get all users
def get_all_users():
    """
    Get all users.
    """
    return User.objects.all()

# get a user by id
def get_user_by_id(user_id):
    """
    Get a user by id.
    """
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None
    
# update a user's role
def update_user_role(user_id, new_role):
    """
    Update a user's role.
    """
    try:
        user_to_update = User.objects.get(id=user_id)
        user_to_update.role = new_role
        user_to_update.save()
        return user_to_update
    except User.DoesNotExist:
        return None
    
# delete a user
def delete_user(user_id):
    """
    Delete a user.
    """
    try:
        user_to_delete = User.objects.get(id=user_id)
        user_to_delete.delete()
        return True
    except User.DoesNotExist:
        return False
    
# create a new user
def create_user(name, email, phone_number, raw_password, role=user.Role.VIEWER):
    """
    Create a new user.
    """ 
    new_user = User(
        name=name,
        email=email,
        phone_number=phone_number,

    )
