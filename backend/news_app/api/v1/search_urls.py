from django.urls import path
from news_app.views.search_views import search_articles, search_forum_posts

urlpatterns = [
    path('articles/', search_articles, name='search-articles'),
    path('forum-posts/', search_forum_posts, name='search-forum-posts'),
]