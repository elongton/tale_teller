from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from forum.models import Forum, Thread, Post
from django.core.paginator import Paginator
from django.core.context_processors import csrf


from tale_teller.settings import MEDIA_ROOT, MEDIA_URL



def main(request):
    """Main listing."""
    forums = Forum.objects.all()
    return dict(forums = forums, user = request.user)
	
	
def add_csrf(request, ** kwargs):
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def mk_paginator(request, items, num_items):
    """Create and return a paginator."""
    paginator = Paginator(items, num_items)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        items = paginator.page(page)
    except (InvalidPage, EmptyPage):
        items = paginator.page(paginator.num_pages)
    return items

def forum(request, pk):
    """Listing of threads in a forum."""
    threads = Thread.objects.filter(forum=pk).order_by("-created")
    threads = mk_paginator(request, threads, 20)
    forum_name = Forum.objects.get(pk=pk)
    return add_csrf(request, threads=threads, forum_name=forum_name, pk=pk)



def thread(request, pk):
    """Listing of posts in a thread."""
    posts = Post.objects.filter(thread=pk).order_by("created")
    posts = mk_paginator(request, posts, 15)
    title = Thread.objects.get(pk=pk).title
    t = Thread.objects.get(pk=pk)
    return add_csrf(request,posts=posts, pk=pk, title=t.title, forum_pk=t.forum.pk)



def post(request, ptype, pk):
    """Display a post form."""
    action = reverse('clients.views.%s' % ptype, args=[pk])
    if ptype == 'new_thread':
        title = 'Start New Thread'
        subject = ''
    elif ptype == 'reply':
        title = 'Reply'
        subject = 'Re: ' + Thread.objects.get(pk=pk).title
    return add_csrf(request, subject=subject, action=action, title=title)

def new_thread(request, pk):
    # """Start a new thread."""
    p = request.POST
    if p['subject'] and p['body']:
        forum = Forum.objects.get(pk=pk)
        thread=Thread.objects.create(forum=forum, title=p['subject'], creator= request.user)
        Post.objects.create(thread=thread, title=p['subject'], body=p['body'], creator = request.user)
    return HttpResponseRedirect(reverse('forum.views.forum', args=[pk]))


def reply(request, pk):
    # """Reply to a thread."""
    p = request.POST
    if p['body']:
        thread = Thread.objects.get(pk=pk)
        post = Post.objects.create(thread=thread, title=p['subject'], body = p['body'], creator = request.user)
    return HttpResponseRedirect(reverse('forum.views.thread', args=[pk]) + '?page=last')
