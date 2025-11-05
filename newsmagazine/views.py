from django.shortcuts import render
from datetime import datetime
def index(request):
    today = datetime.now()
    formatted_date = today.strftime("%a. %d %b %Y")
    return render(request, 'index.html',{'formatted_date': formatted_date})

def detail(request):
     today = datetime.now()
     formatted_date = today.strftime("%a. %d %b %Y")
     return render(request,'detail-page.html', {'formatted_date': formatted_date})


def page_404(request):
    today = datetime.now()
    formatted_date = today.strftime("%a. %d %b %Y")
    return render(request,'404.html',{'formatted_date': formatted_date})