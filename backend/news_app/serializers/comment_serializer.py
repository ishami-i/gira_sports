from rest_framework import serializers
from news_app.models import comment

# Serializer for the comment model
class CommentSerializer(serializers.ModelSerializer):
    # calling the comment model and all its fields
    class Meta:
        model = comment
        fields = '__all__'