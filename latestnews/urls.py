from django.urls import path
from . import views

urlpatterns = [
    path('api/latest/', views.get_latest_news, name='get_latest_news'),
]
