from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import decorator_from_middleware

from phrasebook.contexts import get_sidebar_args
from phrasebook.middleware import FirstLoginMiddleware
from phrasebook.models import *


def index(request):
    return render(request, 'phrasebook/index.html')


@login_required()
@decorator_from_middleware(FirstLoginMiddleware)
def app(request):
    words = Word.objects.filter(category__user=request.user).order_by("-created_on")[:10]
    return render(request, 'phrasebook/app.html',
                  context=get_sidebar_args(request,
                                           {"words": words, "words__len": words.__len__(), "page_app": "active"}))


@login_required()
def first_login(request):
    user_languages = UserLanguage.objects.filter(user=request.user)
    if user_languages.__len__() > 0:
        return redirect('phrasebook:app')
    else:
        languages = list(Language.objects.all().order_by('english_name'))
        return render(request, 'phrasebook/firstlogin.html', context={'languages': languages})


@login_required()
def lang_pick(request):
    return render(request, 'phrasebook/changelanguage.html', context=get_sidebar_args(request, {}))


@login_required()
def profile(request):
    ctx = get_sidebar_args(request, {})
    ctx.update({'extra_langs': ctx['languages_len'] - 5, 'last_name': request.user.last_name})

    return render(request, 'phrasebook/profile.html', context=ctx)
