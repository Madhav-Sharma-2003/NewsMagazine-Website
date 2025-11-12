from django.db import models

# Create your models here.
class LatestNews(models.Model):
    LatestNews_title = models.CharField(max_length=200)
    LatestNews_authorname = models.CharField(max_length=100)
    LatestNews_date = models.DateField()
    LatestNews_image = models.FileField(upload_to='latestnews',max_length=255, null=True, default=None)