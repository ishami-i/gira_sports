from django.db import models

# the users table will be like this:
class user(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password_harsh = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # role will be foreign key from role table
    role = models.ForeignKey('role', on_delete=models.CASCADE)

    def __str__(self):
        return self.name