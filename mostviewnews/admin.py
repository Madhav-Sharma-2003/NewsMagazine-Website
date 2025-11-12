from django.contrib import admin
from .models import MostViewNews
# Register your models here.
class MostViewNewsAdmin(admin.ModelAdmin):
    list_display = ('MostViewNews_title', 'MostViewNews_authorname', 'MostViewNews_date','MostViewNews_image')
admin.site.register(MostViewNews, MostViewNewsAdmin)