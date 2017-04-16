from django.contrib.auth.decorators import login_required
from django.core.exceptions import FieldDoesNotExist, ObjectDoesNotExist
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import decorator_from_middleware

from phrasebook.contexts import get_sidebar_args
from phrasebook.middleware import FirstLoginMiddleware
from phrasebook.models import Category, Word, Language


@login_required()
@decorator_from_middleware(FirstLoginMiddleware)
def get_category(request, id):
    try:
        cat = Category.objects.get(id=id)
    except ObjectDoesNotExist:
        cat = None
    words = Word.objects.filter(category=cat).order_by('-starred', 'foreign')
    if cat is not None and cat.user == request.user:
        return render(request, "phrasebook/category.html",
                      context=get_sidebar_args(request, {"category": cat,
                                                         "words": words,
                                                         "category__len": words.count,
                                                         "current_category_id": cat.id}))
    else:
        return redirect("phrasebook:all_categories")


@login_required()
@decorator_from_middleware(FirstLoginMiddleware)
def all_categories(request):
    cats = list(Category.objects.filter(user=request.user).order_by('-pinned', 'name').annotate(num_words=Count('word')))
    return render(request, "phrasebook/allcategories.html",
                  context=get_sidebar_args(request, {"categories": cats, "all_categories": "active"}))


@login_required()
@decorator_from_middleware(FirstLoginMiddleware)
def new_category(request):
    if request.method == "GET":
        return render(request, "phrasebook/newcategory.html",
                      context=get_sidebar_args(request, {"new_category": "active"}))
    elif request.method == "POST":
        name = request.POST.get('category')
        shortened = request.POST.get('shortened')[:3]
        current_language = Language.objects.get(flag_name=request.session['current_language'])
        new_cat = Category(name=name, shortened=shortened, language=current_language, user=request.user)
        new_cat.save()
        return redirect("phrasebook:all_categories")
    else:
        return redirect("phrasebook:app")


def pin_category(request, id):
    category = Category.objects.get(id=id)
    if category.user == request.user:
        if category is not None:
            category.pinned = not category.pinned
            category.save()
            return redirect("phrasebook:get_category", id)
        else:
            return redirect("phrasebook:app")
    else:
        return redirect("phrasebook:app")
