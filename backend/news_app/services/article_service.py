from datetime import timedelta
from django.utils import timezone

from news_app.models.article import news_article

# checking if an article is trending or not based on the number of views and the published date
def is_trending_article(article):
    """
    Check if a single article is trending.
    """

    one_week_ago = timezone.now() - timedelta(days=7)

    if article.published_at >= one_week_ago and article.views > 100:
        return True

    return False

# getting all the trending articles
def get_trending_articles():
    """
    Get all trending articles.
    """

    one_week_ago = timezone.now() - timedelta(days=7)

    return news_article.objects.filter(
        published_at__gte=one_week_ago,
        views__gt=100
    ).order_by("-views")[:10]

# getting all the articles ordered by published date
def get_all_articles():
    """
    Get all articles.
    """
    return news_article.objects.all().order_by("-published_at")

# adding a new article to the database
def add_article(title, content, author):
    """
    Add a new article to the database.
    """
    article = news_article.objects.create(
        title=title,
        content=content,
        author=author
    )
    return article