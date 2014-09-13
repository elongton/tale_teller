from django.contrib import admin
from projects.models import Project, Draft, Comment
# Register your models here.
admin.site.register(Project)
admin.site.register(Draft)
admin.site.register(Comment)