from django.contrib.auth import authenticate, login as auth_login, models as auth_models, logout as auth_logout
from django.shortcuts import render, redirect

from ..utils import update_session
from ..models import UserLanguage, UserProgress


# LOGIN STUFF

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            # ctx = RequestContext(request, {})
            return render(request, 'phrasebook/login.html')
        elif request.method == 'POST':
            return login_post(request)
    else:
        return redirect('phrasebook:app')


def login_post(request):
    # print(request.POST)
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is None:
        return render(request, 'phrasebook/login.html', context={'error': 'Sorry, incorrect username or password '})
    else:
        auth_login(request, user)
        langs = UserLanguage.objects.filter(user=request.user).order_by("language__english_name")
        progress = UserProgress.objects.filter(user=request.user)
        if langs.__len__() > 0:
            request.session.__setitem__('current_language', langs.first().language.flag_name)
        if progress.__len__() < 1:
            prog = UserProgress(user=request.user, level=1, xp=0)
            prog.save()
        update_session(request)
        return redirect('phrasebook:app')


# REGISTER STUFF

def register(request):
    if request.method == 'GET':
        return render(request, 'phrasebook/register.html')
    elif request.method == 'POST':
        return register_post(request)


def register_post(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    passwordC = request.POST.get('confirmpassword')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    if password == passwordC and password != "":
        user = auth_models.User.objects.create_user(username=username, password=password, first_name=firstname,
                                                    last_name=lastname, email=email)
        user.save()
        return render(request, 'phrasebook/login.html', context={'success': 'Registration Complete! Please login'})
    else:
        return render(request, 'phrasebook/register.html', context={'error': 'Sorry, passwords don\'t match.'})


def logout(request):
    auth_logout(request)
    return redirect('phrasebook:index')
