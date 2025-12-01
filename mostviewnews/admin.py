from django.contrib import admin
from .models import MostViewNews

@admin.register(MostViewNews)
class MostViewNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'authorname', 'date', 'image']  # ← FIXED
    list_filter = ['date']
