from rest_framework import serializers
from news_app.models import user

# Serializer for the user model
class UserSerializer(serializers.ModelSerializer):
    # calling the user model and all its fields
    class Meta:
        model = user
        fields = '__all__'