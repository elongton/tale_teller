from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 200)
    date = models.DateField(auto_now_add = False, blank = False)
    description = models.TextField(max_length = 100)
    client = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

class Draft(models.Model):
    name = models.CharField(max_length = 200)
    date = models.DateField(auto_now_add = False, blank = False)
    description = models.TextField()
    project = models.ForeignKey(Project)
    client = models.ForeignKey(User, blank=True, null=True)
    draft_file = models.FileField(upload_to = 'drafts')

    def __unicode__(self):
        return unicode(self.name)


class Comment(models.Model):

    body = models.TextField()
    date = models.DateField(auto_now_add = False, blank = False)
    client = models.ForeignKey(User, blank=True, null=True)
    author = models.CharField(max_length = 100)
    project = models.ForeignKey(Project)
    draft = models.ForeignKey(Draft)
    edited_file = models.FileField(upload_to = 'revisions', blank=True)

    def __unicode__(self):
        return unicode(self.draft)



admin.site.register(Project)
admin.site.register(Draft)
admin.site.register(Comment)

