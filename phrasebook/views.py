from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
from django.template import loader

from phrasebook.contexts import get_sidebar_args


def index(request):
    return render(request, 'phrasebook/index.html')


# LOGIN STUFF

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            # ctx = RequestContext(request, {})
            return render(request, 'phrasebook/login.html')
        elif request.method == 'POST':
            return loginPost(request)
    else:
        return redirect('phrasebook:app')


def loginPost(request):
    print(request.POST)
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is None:
        return render(request, 'phrasebook/login.html', context={'error': 'Sorry, incorrect username or password '})
    else:
        auth_login(request, user)
        return redirect('phrasebook:app')


# REGISTER STUFF

def register(request):
    if request.method == 'GET':
        template = loader.get_template('phrasebook/register.html')
        ctx = {}
        return HttpResponse(template.render(ctx, request))
    elif request.method == 'POST':
        registerPost(request)


def registerPost(request):
    print(request.POST)


@login_required()
def app(request):
    return render(request, 'phrasebook/app.html', context=get_sidebar_args(request))


def logout(request):
    auth_logout(request)
    return redirect('phrasebook:index')


