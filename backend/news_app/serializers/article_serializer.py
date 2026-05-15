from rest_framework import serializers
from news_app.models import news_article as article

# Serializer for the article model
class ArticleSerializer(serializers.ModelSerializer):
    # calling the article model and all its fields
    class Meta:
        model = article
        fields = '__all__'

