from datetime import datetime
from django.utils import timezone

# getting serielized data of the forum model
from news_app.serializers import ForumSerializer

# getting all the forum posts
def get_all_forum_posts():
    """
    Get all forum posts.
    """
    from news_app.models.forum import ForumPost
    forum_posts = ForumPost.objects.all().order_by("-created_at")
    return ForumSerializer(forum_posts, many=True).data

# adding a new forum post to the database
def add_forum_post(title, content, author):
    """
    Add a new forum post to the database.
    """
    from news_app.models.forum import ForumPost
    forum_post = ForumPost.objects.create(
        title=title,
        content=content,
        author=author,
        created_at=timezone.now()
    )
    return ForumSerializer(forum_post).data