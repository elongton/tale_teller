from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.context_processors import csrf
from news.models import Article
# Create your views here.




def articles(request):
    article = Article.objects.all()
    return article
