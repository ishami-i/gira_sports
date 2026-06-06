from rest_framework import serializers
from news_app.models import forum_comment

# Serializer for the comment model
class ForumCommentSerializer(serializers.ModelSerializer):
    # calling the comment model and all its fields
    class Meta:
        model = forum_comment
        fields = '__all__'