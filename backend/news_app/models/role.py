from django.db import models

# the role table which is either editor, chief editor, admin, or viewer, other will be added through development
class role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name