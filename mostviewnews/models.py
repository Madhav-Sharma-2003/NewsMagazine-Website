# ...existing code...
from django.db import models

class MostViewNews(models.Model):
    CATEGORY_CHOICES = [
        ('Sports', 'Sports')
    ]

    title = models.CharField(max_length=200)
    authorname = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='mostviewnews/')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, null=True, blank=True)  # NEW
    def __str__(self):
        return self.title
# ...existing code...