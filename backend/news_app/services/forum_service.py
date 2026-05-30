from datetime import datetime
from django.utils import timezone
from ..models.forum_post import ForumPost

# getting all the forum posts
def get_all_forum_posts():
    """
    Get all forum posts.
    """
    return ForumPost.objects.all().order_by("-created_at")

# adding a new forum post to the database
def add_forum_post(title, content, author):
    """
    Add a new forum post to the database.
    """
    forum_post = ForumPost.objects.create(
        title=title,
        content=content,
        author=author,
        created_at=timezone.now()
    )
    return forum_post