from django.db import models

# category of the news article like sports, fixtures, scores, transfers, and other will be added through development
class category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name