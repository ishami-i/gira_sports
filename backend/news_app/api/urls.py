from django.urls import path, include

urlpatterns = [
    path('v1/articles/', include('news_app.api.v1.article_urls')),
]