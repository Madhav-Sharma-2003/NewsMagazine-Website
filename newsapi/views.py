from django.shortcuts import render
from .services import NewsAPIService
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import NewsAPIService
def print_json(request):
    service = NewsAPIService()
    articles = service.get_latest_news(category='technology', country='in', limit=10)
    context = {
        'articles': articles,
        'total_results': len(articles),
    }
    return render(request, 'print_json.html', context)

@api_view(['GET'])
def get_live_news(request):
    service = NewsAPIService()
    articles = service.get_latest_news('technology', 'in', 10)
    return Response(articles)


# Create your views here.
