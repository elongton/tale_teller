from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from profiles.models import Transaction, Description
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.context_processors import csrf

# Create your views here.

def description(request):
    user = request.user
    user_des = Description.objects.get(creator=user.id)
    return user_des

def services(request):
    user = request.user
    trans = Transaction.objects.filter(client=user.id)
    return trans