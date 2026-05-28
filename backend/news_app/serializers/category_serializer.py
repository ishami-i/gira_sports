from rest_framework import serializers
from ..models import category

# model serializer for the category model to convert the category model instances into JSON format and vice versa
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'