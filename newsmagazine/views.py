from urllib import request, response
from django.shortcuts import render
from datetime import datetime
from latestnews.models import LatestNews
from mostviewnews.models import MostViewNews
from leave_comment.models import Comment
from django.core.exceptions import FieldDoesNotExist

def index(request):
    today = datetime.now()
    formatted_date = today.strftime("%a. %d %b %Y")

    ournewsData = LatestNews.objects.all()
    mostviewnewsData = MostViewNews.objects.all()

    categories = [
        ('sports', 'Sports'),
    ]
    source_model = None
    try:
        LatestNews._meta.get_field('category')
        source_model = LatestNews
    except FieldDoesNotExist:
        try:
            MostViewNews._meta.get_field('category')
            source_model = MostViewNews
        except FieldDoesNotExist:
            source_model = None

    tabs = []
    if source_model:
        for slug, name in categories:
            qs = source_model.objects.filter(category__iexact=name).order_by('-date')
            hero = qs.first() if qs.exists() else None
            items = qs[1:6] if qs.exists() and qs.count() > 1 else []
            tabs.append({'slug': slug, 'name': name, 'hero': hero, 'items': items})
    else:
        
        qs_all = MostViewNews.objects.order_by('-date')
        for i, (slug, name) in enumerate(categories):
            start = i * 5
            hero = qs_all[start] if len(qs_all) > start else None
            items = qs_all[start + 1:start + 5] if len(qs_all) > start + 1 else []
            tabs.append({'slug': slug, 'name': name, 'hero': hero, 'items': items})


    data = {
        'formatted_date': formatted_date,
        'ournewsData': ournewsData,
        'mostviewnewsData': mostviewnewsData,
        'tabs': tabs,   
    }
    return render(request, 'index.html', data)

def detail(request):
    today = datetime.now()
    formatted_date = today.strftime("%a. %d %b %Y")

    msg = ""
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment')
        comment = Comment(full_name=full_name, email=email, comment=comment_text)
        comment.save()
        msg = "Your comment has been submitted successfully."

    
    latest_news = LatestNews.objects.all()[:5]  
    sidebar_news = MostViewNews.objects.all()[:4]  
    all_comments = Comment.objects.all().order_by('-id')[:10] 

    context = {
        'formatted_date': formatted_date,
        'msg': msg,
        'latest_news': latest_news,      
        'sidebar_news': sidebar_news,    
        'all_comments': all_comments,   
    }
    return render(request, 'detail-page.html', context)



def page_404(request):
    today = datetime.now()
    formatted_date = today.strftime("%a. %d %b %Y")
    return render(request,'404.html',{'formatted_date': formatted_date})
