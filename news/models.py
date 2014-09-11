from django.db import models
from django.contrib import admin

# Create your models here.
class Article(models.Model):
    LEFT = 'L'
    RIGHT = 'R'

    CHOICES = (
        (RIGHT, 'Right'),
        (LEFT, 'Left'),
    )

    title = models.CharField(max_length = 200)
    body = models.TextField()
    date = models.DateField(auto_now_add = False, blank = False)
    creator = models.CharField(max_length = 200)
    picture = models.FileField(upload_to = '%Y_%m_%d')
    caption = models.CharField(max_length = 200)
    leftright = models.CharField(max_length = 1,
                                 choices = CHOICES,
                                 default = RIGHT)

    def __unicode__(self):
        return self.title




admin.site.register(Article)