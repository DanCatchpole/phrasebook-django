import json

from django.contrib.auth.decorators import login_required
from django.core.exceptions import FieldDoesNotExist, ObjectDoesNotExist
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
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
                                                         "current_category_id": cat.id,
                                                         "notes": render_dcmarkup(cat.description)}))
    else:
        return redirect("phrasebook:all_categories")


@login_required()
@decorator_from_middleware(FirstLoginMiddleware)
def all_categories(request):
    if request.method == "GET":
        cats = list(
            Category.objects.filter(user=request.user,
                                    language__flag_name=request.session['current_language']).order_by(
                '-pinned', 'name').annotate(num_words=Count('word')))
        return render(request, "phrasebook/allcategories.html",
                      context=get_sidebar_args(request, {"categories": cats, "all_categories": "active"}))
    elif request.method == "POST":
        user_categories = list(
            Category.objects.filter(user=request.user, language__flag_name=request.session['current_language']))
        word_id = request.POST.get('word_id')
        try:
            word = Word.objects.get(id=word_id)
            return render(request, "phrasebook/categorylist.html", context={"categories": user_categories,
                                                                            "word_id": word_id,
                                                                            "word": word})
        except ObjectDoesNotExist:
            return JsonResponse({"status": "error"})


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


@login_required()
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


@login_required()
def category_notes(request, id):
    try:
        cat = Category.objects.get(id=id)
    except ObjectDoesNotExist:
        cat = None
    words = Word.objects.filter(category=cat).order_by('-starred', 'foreign')
    if cat is not None and cat.user == request.user:
        return render(request, "phrasebook/categorynotes.html",
                      context=get_sidebar_args(request, {"category": cat,
                                                         "words": words,
                                                         "category__len": words.count,
                                                         "current_category_id": cat.id,
                                                         "notes": cat.description}))
    else:
        return redirect("phrasebook:all_categories")


@login_required()
def update_notes(request, id):
    if request.method == "GET":
        return redirect("phrasebook:app")
    elif request.method == "POST":
        try:
            cat = Category.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "error", "message": "Category doesn't exist"})

        if cat.user != request.user:
            return JsonResponse({"status": "error", "message": "Category doesn't exist"})
        else:
            replace = request.POST.get('notes')
            render = request.POST.get('renderonly')
            if render == "false":
                cat.description = replace
                cat.save()
            return JsonResponse({"status": "success", "message": render_dcmarkup(replace)})


@login_required()
def update_words(request, id):
    rec = request.body.decode("utf-8")
    # print(rec)
    received_json = json.loads(request.body.decode("utf-8"))
    # print(received_json)
    # print(received_json["removed_words"])
    # print(received_json["updated_words"])

    for word in received_json["updated_words"]:
        w = Word.objects.get(id=word['id'])
        if w.foreign != word['foreign'] or w.english != word['english']:
            w.foreign = word['foreign']
            w.english = word['english']
            if w.category.user == request.user and w.category.id == int(id):
                w.save()
        else:
            continue

    for word in received_json["removed_words"]:
        w = Word.objects.get(id=word)
        if w.category.user == request.user and w.category.id == int(id):
            w.delete()

    for word in received_json['new_words']:
        w = Word(foreign=word['foreign'], english=word['english'], category_id=id)
        w.save()
    return JsonResponse({"status": "success"})


def render_dcmarkup(markup):
    lines = str(markup).split('\n')
    output = ""
    for line in lines:
        if line.startswith("#"):
            output += "<div class='h4'>" + line[1:] + "</div>"
        elif line.startswith("="):
            output += "<p>"
        elif line.startswith("/="):
            output += "</p>"
        else:
            output += line
    return output
