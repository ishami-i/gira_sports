import re
from datetime import datetime
from django.utils import timezone
from django.contrib.postgres.search import TrigramSimilarity
from news_app.models.article import news_article

# the regex pattern to match
query_pattern = re.compile(r'^[a-zA-Z0-9\s]{6, }$')
# searching for articles based on a query string
def search_articles(query):
    """
    Search for articles based on a query string
    and the similarity of the query string to the article title using trigram similarity.
    """
    if not query_pattern.match(query):
        return []
    articles = news_article.objects.all()

    if query:
        articles = news_article.annotate(
            similarity = TrigramSimilarity('title', query)
        ).filter(
            similarity__gt=0.3
        ).order_by(
            '-similarity'
        )
    else:
        print('no articles found')


    return articles

# searching through the forum posts based on a query string and the similarity of the query string to the forum post title using trigram similarity.
def search_forum_posts(query):
    """
    Search through the forum posts based on a query string and the similarity of the query string to the forum post title using trigram similarity.
    """
    if not query_pattern.match(query):
        return []
    from news_app.models.forum_post import ForumPost
    forum_posts = ForumPost.objects.all()

    if query:
        forum_posts = ForumPost.annotate(
            similarity = TrigramSimilarity('title', query)
        ).filter(
            similarity__gt=0.3
        ).order_by(
            '-similarity'
        )
    else:
        print('no forum posts found')

    return forum_posts

