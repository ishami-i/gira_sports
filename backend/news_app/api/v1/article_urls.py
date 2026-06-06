from django.urls import path
from news_app.views.article_views import trending_articles, get_all_articles, add_article, update_article, delete_article

urlpatterns = [
    path('trending/', trending_articles, name='trending-articles'),
    path('all/', get_all_articles, name='all-articles'),
    path('add/', add_article, name='add-article'),
    path('update/<int:article_id>/<int:author_id>/', update_article, name='update-article'),
    path('delete/<int:article_id>/<int:author_id>/', delete_article, name='delete-article'),
]