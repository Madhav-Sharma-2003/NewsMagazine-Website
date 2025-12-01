from django.contrib import admin
from .models import LatestNews

@admin.register(LatestNews)
class LatestNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'authorname', 'date', 'image']  # ← FIXED
    list_filter = ['date']
