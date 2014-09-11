from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.context_processors import csrf
from projects.models import Project, Draft, Comment
# Create your views here.


def project(request):
    user = request.user
    project = Project.objects.filter(client=user.id)
    return project

def draft(request):
    user = request.user
    draft = Draft.objects.filter(client=user.id)
    return draft


def comment(request):
    user = request.user
    comment = Comment.objects.filter(client=user.id)
    return comment