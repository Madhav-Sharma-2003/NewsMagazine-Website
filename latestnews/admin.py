from django.contrib import admin

# Register your models here.
from latestnews.models import LatestNews
class LatestNewsAdmin(admin.ModelAdmin):
    list_display = ('LatestNews_title', 'LatestNews_authorname', 'LatestNews_date', 'LatestNews_image')
admin.site.register(LatestNews, LatestNewsAdmin)