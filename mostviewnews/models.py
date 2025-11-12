from django.db import models

# Create your models here.
class MostViewNews(models.Model):
    MostViewNews_title = models.CharField(max_length=200)
    MostViewNews_authorname = models.CharField(max_length=100)
    MostViewNews_date = models.DateField()
    MostViewNews_image = models.FileField(upload_to='mostviewnews',max_length=255, null=True, default=None)