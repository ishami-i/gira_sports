from rest_framework import serializers
from news_app.models import forum_post

# Serializer for the forum post model
class ForumPostSerializer(serializers.ModelSerializer):
    # calling the forum post model and all its fields
    class Meta:
        model = forum_post
        fields = '__all__'
