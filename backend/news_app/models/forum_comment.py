from django.db import models
from .user import users
from .forum_post import forum_post

# table for forum post comments by community members
class forum_comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # the author will be foreign key from users table
    author = models.ForeignKey(users, on_delete=models.CASCADE)
    # the forum post will be foreign key from forum_post table
    forum_post = models.ForeignKey(forum_post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author.name} on {self.forum_post.title}'