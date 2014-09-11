from django.db import models
from django.contrib.auth.models import User
from string import join


DEVELOPMENTAL_EDITING = 'DE'
LINE_EDITING = 'LE'
COPY_EDITING = 'CE'
CREATIVE_CONSULTING = 'CC'

EDITING_CHOICES = (
    (DEVELOPMENTAL_EDITING, 'Developmental Editing'),
    (LINE_EDITING, 'Line Editing'),
    (COPY_EDITING, 'Copy Editing'),
    (CREATIVE_CONSULTING, 'Creative Consulting'),
)


# def get_name():
#     return User.get_short_name()
# Create your models here.
class Transaction(models.Model):
    client = models.ForeignKey(User, blank=True, null=True)
    service = models.CharField(max_length=2, choices=EDITING_CHOICES, default=DEVELOPMENTAL_EDITING)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.DecimalField(max_digits=10, decimal_places=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    def __unicode__(self):
        return unicode(self.client) + '_'+str(self.date.month)+ '-'+str(self.date.day)+ '-'+str(self.date.year)


class Description(models.Model):
    about = models.TextField(blank=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thumbnail = models.FileField(upload_to = 'profile_pics', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.creator)