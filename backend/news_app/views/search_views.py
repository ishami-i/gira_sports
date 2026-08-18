from django.shortcuts import render
from django.http import JsonResponse
from ..services.search_service import search_articles, search_forum_posts

# Create your views here.
# search for articles based on a query string and the similarity of the query string to the article title using trigram similarity.
def search_articles_view(request):
    query = request.GET.get('query', '')
    articles = search_articles(query)
    data = []
    for article in articles:
        data.append({
            'title': article.title,
            'slug': article.slug,
            'content': article.content,
            'published_at': article.published_at,
            'views': article.views,
            'status': article.status,
            'author': article.author.name,
            'category': article.category.name
        })
    return JsonResponse(data, safe=False)

# search through the forum posts based on a query string and the similarity of the query string to the forum post title using trigram similarity.
def search_forum_posts_view(request):
    query = request.GET.get('query', '')
    forum_posts = search_forum_posts(query)
    data = []
    for forum_post in forum_posts:
        data.append({
            'title': forum_post.title,
            'content': forum_post.content,
            'created_at': forum_post.created_at,
            'author': forum_post.author.name
        })
    return JsonResponse(data, safe=False)