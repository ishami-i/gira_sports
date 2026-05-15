from django.db import models
from .user import users
from .article import news_article
from .category import category

# table for comments on news article
class comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # the author will be foreign key from users table
    author = models.ForeignKey(users, on_delete=models.CASCADE)
    # the news article will be foreign key from news_article table
    news_article = models.ForeignKey(news_article, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author.name} on {self.news_article.title}'