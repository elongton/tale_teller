from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from info_form.models import User_input
from info_form.forms import User_inputForm
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated():
        loggedin = True
    else:
        loggedin = False
    return render_to_response('home.html', {'loggedin':loggedin})

def bio(request):
    if request.user.is_authenticated():
        loggedin = True
    else:
        loggedin = False
    return render_to_response('credentials.html', {'loggedin':loggedin})

def testimonials(request):
    if request.user.is_authenticated():
        loggedin = True
    else:
        loggedin = False
    return render_to_response('testimonials.html', {'loggedin':loggedin})

def services(request):
    if request.user.is_authenticated():
        loggedin = True
    else:
        loggedin = False

    args = {}



    if request.method == 'POST':
        form = User_inputForm(request.POST, request.FILES)
        if form.is_valid():
            submitted = 1
            request.session['submitted'] = submitted
            args['submitted'] = request.session['submitted']
            form.save()

            # return HttpResponseRedirect('/services/')
    else:
        form = User_inputForm()
        args['submitted'] = 'none'
    args.update(csrf(request))
    args['form'] = form
    args['loggedin'] = loggedin
    return render_to_response('services.html', args)

def resources(request):

    if request.user.is_authenticated():
        loggedin = True
    else:
        loggedin = False
    return render_to_response('resources.html', {'loggedin':loggedin})


def kaylynnespauls(request):
    return render_to_response('kaylynnespauls.html')



def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username' , '')
    password = request.POST.get('password' , '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin(request):
    return HttpResponseRedirect('/clients/')
    # return render_to_response('loggedin.html',
                                # {'full_name': request.user.username})
def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')








# def create(request):
	# c = {}
	# c.update(csrf(request))
	# return render_to_response('create.html', c)

# def user_creation(request):
	# username = request.POST.get('username', '')
	# firstname = request.POST.get('firstname', '')
	# lastname = request.POST.get('lastname', '')
	# email = request.POST.get('email', '')
	# password = request.POST.get('password', '')
	# confirm_password = request.POST.get('password2')
	
	# user = User.objects.create_user(username, email, password)
	# user.last_name = lastname
	# user.first_name = firstname
	# user.is_active = True
	# user.save()
	# return render_to_response('creationsuccess.html', 
								# {'firstname': firstname})
	
