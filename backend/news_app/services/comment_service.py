from datetime import datetime
from django.utils import timezone

# import the serilized data of the comment model
from news_app.serializers import CommentSerializer

# getting all the comments of a specific article
def get_comments_by_article(article):
    """
    Get all comments of a specific article.
    """
    comments = article.comments.all().order_by("-created_at")
    return CommentSerializer(comments, many=True).data

# adding a new comment to a specific article
def add_comment_to_article(article, content, author):
    """
    Add a new comment to a specific article.
    """
    comment = article.comments.create(
        content=content,
        author=author,
        created_at=timezone.now()
    )
    return CommentSerializer(comment).data