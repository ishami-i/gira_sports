from django.shortcuts import render
from django.http import JsonResponse
from ..services.article_service import get_trending_articles
# from rest_framework import generics

# Create your views here.
# get trending articles

def trending_articles(request):
    articles = get_trending_articles()
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