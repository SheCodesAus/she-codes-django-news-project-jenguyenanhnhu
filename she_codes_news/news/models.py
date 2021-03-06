from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete = models.CASCADE
        )
    date = models.DateTimeField()
    content = models.TextField()
    image = models.FileField(upload_to='images', default='static/news/images/placeholder-1.jpg')
    caption = models.CharField(max_length=250, default='')
