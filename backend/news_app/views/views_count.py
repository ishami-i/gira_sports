# import the necessary libraries and modules
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from news_app.models import news_article

# setting the view to only accept POST requests
@api_view(['POST'])

# view function to track article views
def track_article_view(request, article_id):
    try:
        # increment the views_count field of the specified article by 1
        updated = news_article.objects.filter(id=article_id).update(views_count=F('views_count') + 1)
        if updated:
            return Response({'message': 'view recorded'}, status=status.HTTP_200_OK)
        # if no article was updated, it means the article was not found
        return Response({'error': 'article not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        # if any error occurs during the process, return a 500 Internal Server Error response with the error message
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)