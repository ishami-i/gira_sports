from datetime import timedelta
from django.utils import timezone

from news_app.models.article import news_article


def is_trending_article(article):
    """
    Check if a single article is trending.
    """

    one_week_ago = timezone.now() - timedelta(days=7)

    if article.published_at >= one_week_ago and article.views > 100:
        return True

    return False


def get_trending_articles():
    """
    Get all trending articles.
    """

    one_week_ago = timezone.now() - timedelta(days=7)

    return news_article.objects.filter(
        published_at__gte=one_week_ago,
        views__gt=100
    ).order_by("-views")[:10]