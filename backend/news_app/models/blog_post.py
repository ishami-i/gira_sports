from django.db import models
from .user import users

# table for blog posts by community members
class blog_post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='draft')  # draft, published, archived
    # the author will be foreign key from users table
    author = models.ForeignKey(users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title