from django.db import models


class User(models.Model):
    class Role(models.TextChoices):
        VIEWER = 'VIEWER', 'Viewer'
        AUTHOR = 'AUTHOR', 'Author'
        EDITOR = 'EDITOR', 'Editor'
        CHIEF_EDITOR = 'CHIEF_ED', 'Chief Editor'

    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.VIEWER
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.role}"
    
    @property
    def is_viewer(self):
        return self.role == self.Role.VIEWER

    @property
    def is_author(self):
        return self.role == self.Role.AUTHOR

    @property
    def is_editor(self):
        return self.role == self.Role.EDITOR

    @property
    def is_chief_editor(self):
        return self.role == self.Role.CHIEF_EDITOR