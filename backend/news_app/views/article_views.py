from django.shortcuts import render
from django.http import JsonResponse
from ..services.article_service import get_trending_articles, get_all_articles, add_article, update_article, delete_article, increment_article_views
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

# get all articles
def all_articles(request):
    articles = get_all_articles()
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

# adding a new article to the database
def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_id = request.POST.get('author_id')
        category_id = request.POST.get('category_id')
        article = add_article(title, content, author_id, category_id)
        data = {
            'title': article.title,
            'slug': article.slug,
            'content': article.content,
            'published_at': article.published_at,
            'views': article.views,
            'status': article.status,
            'author': article.author.name,
            'category': article.category.name
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    

# updating an existing article in the database
def update_article(request, article_id, author_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author_id')
        article = update_article(article_id, title, content, author)
        if article:
            data = {
                'title': article.title,
                'slug': article.slug,
                'content': article.content,
                'published_at': article.published_at,
                'views': article.views,
                'status': article.status,
                'author': article.author.name,
                'category': article.category.name
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Article not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
# deleting an article from the database
def delete_article(request, article_id):
    if request.method == 'DELETE':
        success = delete_article(article_id)
        if success:
            return JsonResponse({'message': 'Article deleted successfully'})
        else:
            return JsonResponse({'error': 'Article not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)