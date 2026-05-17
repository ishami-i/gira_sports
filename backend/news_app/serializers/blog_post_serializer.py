from rest_framework import serializers
from news_app.models import blog_post

# Serializer for the blog post model
class BlogPostSerializer(serializers.ModelSerializer):
    # calling the blog post model and all its fields
    class Meta:
        model = blog_post
        fields = '__all__'