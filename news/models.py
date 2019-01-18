from django.db import models
from realtors.models import Realtor
from datetime import datetime

class Article(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    content = models.TextField(blank=False)
    author = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    is_published = models.BooleanField (default=True)
    published_date = models.DateTimeField (default=datetime.now,blank=True)

    def __str__(self):
        return self.title