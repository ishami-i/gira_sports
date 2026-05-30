import re
from django.contrib.auth.hashers import make_password
from ..models.user import User

# Service functions for users
# setting up a regex pattern for validating email, phone number, and name
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^\+?1?\d{9,15}$'
NAME_REGEX = r'^[a-zA-Z\s]+$'
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
    if not re.match(NAME_REGEX, name):
        raise ValueError("Invalid name format. Only letters and spaces are allowed.")
    if not re.match(EMAIL_REGEX, email):
        raise ValueError("Invalid email format.")
    if not re.match(PHONE_REGEX, phone_number):
        raise ValueError("Invalid phone number format.")
    
    new_user = User(
        name=name,
        email=email,
        phone_number=phone_number,
        password=make_password(raw_password),
        role=role
    )
    new_user.save()
    return new_user