from django.urls import path
from . import views

urlpatterns = [
    path('json/', views.print_json, name='print_json'),
    path('api/live/', views.get_live_news, name='get_live_news'),
]
