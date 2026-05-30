from datetime import datetime
from django.utils import timezone

from news_app.models.forum_comment import ForumComment

# getting all the comments of a specific forum post
def get_comments_by_forum_post(forum_post):
    """
    Get all comments of a specific forum post.
    """
    comments = forum_post.comments.all().order_by("-created_at")
    return ForumComment(comments, many=True).data

# adding a new comment to a specific forum post
def add_comment_to_forum_post(forum_post, content, author):
    """
    Add a new comment to a specific forum post.
    """
    comment = forum_post.comments.create(
        content=content,
        author=author,
        created_at=timezone.now()
    )
    return ForumComment(comment).data