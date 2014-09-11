from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# from PIL import Image as PImage
from os.path import join as pjoin
from django.forms import ModelForm
from forum.models import Forum, Thread, Post
from tale_teller.settings import MEDIA_ROOT, MEDIA_URL
from django.core.context_processors import csrf

from forum.views import main, forum, thread, post
from profiles.views import description, services
from profiles.models import Description, Transaction
from news.views import articles
from projects.views import project, draft, comment
from projects.models import Project, Draft, Comment
import datetime


def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d



@login_required(login_url = '/accounts/login/')
def client_news(request):
    return render_to_response('clientnews.html')

@login_required(login_url = '/accounts/login/')
def client_message(request):
    return render_to_response('clientmessage.html')

@login_required(login_url = '/accounts/login/')
def client_authorpage(request):
    return render_to_response('clientauthorpage.html')


""" Forum Code """
@login_required(login_url = '/accounts/login/')
def forums(request):
    return render_to_response('forums.html', main(request))

@login_required(login_url = '/accounts/login/')
def topics(request, pk):
    return render_to_response('topics.html', forum(request, pk))

@login_required(login_url = '/accounts/login/')	
def threads(request, pk):
    return render_to_response('threads.html', thread(request, pk))


@login_required(login_url = '/accounts/login/')
def posts(request, ptype, pk):
    return render_to_response('posts.html', post(request, ptype, pk))


def new_thread(request, pk):
    p = request.POST
    if p['subject'] and p['body']:
        forum = Forum.objects.get(pk=pk)
        thread= Thread.objects.create(forum=forum, title=p['subject'], creator= request.user)
        Post.objects.create(thread=thread, title=p['subject'], body=p['body'], creator = request.user)
    return HttpResponseRedirect(reverse('clients.views.topics', args=[pk]))


def reply(request, pk):
    p = request.POST
    if p['body']:
        thread = Thread.objects.get(pk=pk)
        post = Post.objects.create(thread=thread, title=p['subject'], body = p['body'], creator = request.user)
    return HttpResponseRedirect(reverse('clients.views.threads', args=[pk]) + '?page=last')

"""End Forum Code """

"""Profile Code """
@login_required(login_url = '/accounts/login/')
def client_profile(request):
    des = {}
    if description is not None:
        des['transaction'] = services(request)
        des['user_des'] = description(request)
    return render_to_response('clientprofile.html', des)


@login_required(login_url = '/accounts/login/')
def profilepost(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('profilepost.html', c)

@login_required(login_url = '/accounts/login/')
def newprofile(request):
    p = request.POST
    g = request.FILES
    profile = Description.objects.get(creator = request.user)
    profile.about = p['descrip']
    profile.thumbnail = g['profilepic']
    profile.save()
    return HttpResponseRedirect(reverse('clients.views.client_profile'))


"""Projects Code """
@login_required(login_url = '/accounts/login/')
def client_projects(request):
    des = {}
    des['user_des'] = description(request)
    des['project'] = project(request)
    des['draft'] = draft(request)
    des['comment'] = comment(request)
    des['MEDIA_URL'] = MEDIA_URL
    return render_to_response('clientprojects.html', des)


@login_required(login_url = '/accounts/login/')
def projpost(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('projpost.html', c)

@login_required(login_url = '/accounts/login/')
def newproj(request):
    p = request.POST
    post = Project.objects.create(name=p['projname'], description = p['descrip'], date = datetime.date.today(), client = request.user)
    return HttpResponseRedirect(reverse('clients.views.client_projects'))


@login_required(login_url = '/accounts/login/')
def draftpost(request, pk):
    c = {}
    c.update(csrf(request))
    c['pk'] = pk
    return render_to_response('draftpost.html', c)

@login_required(login_url = '/accounts/login/')
def newdraft(request, pk):
    p = request.POST
    g = request.FILES
    post = Draft.objects.create(name = p['draftname'], date = datetime.date.today(), description = p['descrip'], draft_file = g['draftfile'], client = request.user, project = Project.objects.get(pk=pk))
    post.save()
    return HttpResponseRedirect(reverse('clients.views.client_projects'))

@login_required(login_url = '/accounts/login/')
def commpost(request, pk):
    c = {}
    c.update(csrf(request))
    c['pk'] = pk
    return render_to_response('commpost.html', c)

@login_required(login_url = '/accounts/login/')
def newcomm(request, pk):
    p = request.POST
    g = request.FILES
    dr = Draft.objects.get(pk=pk)
    post = Comment.objects.create(body = p['comment'], date = datetime.date.today(), client = request.user, project = dr.project, draft = dr, author=request.user)
    return HttpResponseRedirect(reverse('clients.views.client_projects'))



"""News Code """
@login_required(login_url = '/accounts/login/')
def client_news(request):
    des = {}
    des['article'] = articles(request)
    return render_to_response('clientnews.html', des)