from django.db import models
from .user import user
from .category import category

# Create your models here.

# table for news article
class news_article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='draft')  # draft, published, archived
    # the author will be foreign key from users table
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    # the category will be foreign key from category table
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




