from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LatestNews
from .serializers import LatestNewsSerializer

@api_view(['GET'])
def get_latest_news(request):
    news = LatestNews.objects.all()
    serializer = LatestNewsSerializer(news, many=True)
    return Response(serializer.data)
