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

# updating an existing article in the database
def update_article(article_id, title=None, content=None):
    """
    Update an existing article in the database.
    """
    try:
        article = news_article.objects.get(id=article_id)
        if title:
            article.title = title
        if content:
            article.content = content
        article.save()
        return article
    except news_article.DoesNotExist:
        return None
    

# deleting an article from the database
def delete_article(article_id):
    """
    Delete an article from the database.
    """
    try:
        article = news_article.objects.get(id=article_id)
        article.delete()
        return True
    except news_article.DoesNotExist:
        return False

# incrementing the view count of an article
def increment_article_views(article_id):
    """
    Increment the view count of an article.
    """
    try:
        article = news_article.objects.get(id=article_id)
        article.views += 1
        article.save()
        return article
    except news_article.DoesNotExist:
        return None

# getting a single article by its id
def get_article_by_id(article_id):
    """
    Get a single article by its id.
    """
    try:
        return news_article.objects.get(id=article_id)
    except news_article.DoesNotExist:
        return None

# getting articles by a specific author
def get_articles_by_author(author):
    """
    Get articles by a specific author.
    """
    return news_article.objects.filter(author=author).order_by("-published_at")

# getting articles published within a specific date range
def get_articles_by_date_range(start_date, end_date):
    """
    Get articles published within a specific date range.
    """
    return news_article.objects.filter(
        published_at__gte=start_date,
        published_at__lte=end_date
    ).order_by("-published_at")

# getting articles that contain a specific keyword in the title or content
def get_articles_by_keyword(keyword):
    """
    Get articles that contain a specific keyword in the title or content.
    """
    return news_article.objects.filter(
        Q(title__icontains=keyword) | Q(content__icontains=keyword)
    ).order_by("-published_at")