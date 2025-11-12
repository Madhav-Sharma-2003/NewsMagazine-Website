from django.shortcuts import render
from datetime import datetime
from latestnews.models import LatestNews
from mostviewnews.models import MostViewNews
def index(request):
    today = datetime.now()
    formatted_date = today.strftime("%a. %d %b %Y")
    ournewsData = LatestNews.objects.all()
    mostviewnewsData = MostViewNews.objects.all()
    data = {
         'formatted_date': formatted_date,
        'ournewsData': ournewsData,
        'mostviewnewsData': mostviewnewsData
    }
    return render(request, 'index.html', data)

def detail(request):
     today = datetime.now()
     formatted_date = today.strftime("%a. %d %b %Y")
     return render(request,'detail-page.html', {'formatted_date': formatted_date})


def page_404(request):
    today = datetime.now()
    formatted_date = today.strftime("%a. %d %b %Y")
    return render(request,'404.html',{'formatted_date': formatted_date})
