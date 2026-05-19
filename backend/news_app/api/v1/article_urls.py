from django.urls import path
from news_app.views.article_views import trending_articles, get_all_articles

urlpatterns = [
    path('trending/', trending_articles, name='trending-articles'),
    path('all/', get_all_articles, name='all-articles'),
]