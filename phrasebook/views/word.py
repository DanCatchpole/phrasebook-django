from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.utils.decorators import decorator_from_middleware

from phrasebook.contexts import get_sidebar_args
from phrasebook.middleware import FirstLoginMiddleware
from phrasebook.models import Category, Word


@login_required()
@decorator_from_middleware(FirstLoginMiddleware)
def new_word(request, cid):
    category = Category.objects.get(id=cid)
    if category.user != request.user:
        return redirect('phrasebook:app')

    if request.method == "GET":
        return render(request, 'phrasebook/newword.html',
                      context=get_sidebar_args(request, {"current_category": category}))
    elif request.method == "POST":
        foreign = request.POST.get('foreign')
        english = request.POST.get('english')
        if foreign is not "" and english is not "":
            word = Word(foreign=foreign, english=english, category=category)
            word.save()
            return redirect('phrasebook:get_category', cid)
        else:
            return redirect('phrasebook:app')
    else:
        return redirect('phrasebook:app')


@login_required()
@decorator_from_middleware(FirstLoginMiddleware)
def star_word(request):
    if request.method == "GET":
        return redirect("phrasebook:app")
    elif request.method == "POST":
        category_id = request.POST.get('categoryID')
        word_id = request.POST.get('wordID')
        print(word_id + ", " + category_id)
        if word_id is not "" and category_id is not "":
            try:
                word = Word.objects.get(id=word_id)
            except ObjectDoesNotExist:
                word = None
            if word is not None and word.category_id == int(category_id) and word.category.user == request.user:
                word.starred = not word.starred
                word.save()
                return JsonResponse({"status": "Success, set to: " + str(word.starred)})
            else:
                return JsonResponse({"error": "Not a valid word or not owned by user"})
        else:
            return JsonResponse({"error": "Failed to star - empty catID/wordID/starred"})


@login_required()
def search_word(request):
    if request.method == "GET":
        return redirect("phrasebook:app")
    elif request.method == "POST":
        contains = request.POST.get('search')
        print(contains)
        category_id = request.POST.get('category')
        flag_name = request.POST.get('short')
        if category_id is None:
            # this is a language wide search
            words = list(Word.objects.filter(foreign__icontains=contains,
                                             category__language__flag_name=flag_name,
                                             category__user=request.user)
                         | Word.objects.filter(english__icontains=contains,
                                               category__language__flag_name=flag_name,
                                               category__user=request.user))
        else:
            # category wide search
            words = list(
                Word.objects.filter(foreign__icontains=contains, category_id=category_id, category__user=request.user)
                | Word.objects.filter(english__icontains=contains, category_id=category_id,
                                      category__user=request.user))

        return render(request, "phrasebook/searchresult.html",
                      context={"words": words, "words__len": words.__len__(), "search_param": contains})


@login_required()
def update_word(request):
    if request.method == "GET":
        return redirect("phrasebook:app")
    elif request.method == "POST":
        word_id = request.POST.get('word_id')
        new_foreign = request.POST.get('newWord')
        new_english = request.POST.get('newEnglish')
        category_id = request.POST.get('category')
        try:
            word = Word.objects.get(id=word_id)
        except ObjectDoesNotExist:
            word = None
        if word is not None and word.category_id == int(category_id) and word.category.user == request.user:
            if new_foreign is not "" and new_english is not "":
                word.foreign = new_foreign
                word.english = new_english
                word.save()
                return JsonResponse({"status": "success", "message": "Saved word successfully"})
            else:
                return JsonResponse({"status": "error", "message": "Could not update - 'news are empty'"})
        else:
            return JsonResponse({"status": "error", "message": "Could not update"})


@login_required()
def move_category(request, word_id, category_id):
    try:
        word = Word.objects.get(id=word_id)
        category = Category.objects.get(id=category_id)
        if word.category.user == request.user and category.user == request.user:
            word.category = category
            word.save()
            return redirect("phrasebook:get_category", category.id)
        else:
            return redirect("phrasebook:app")
    except ObjectDoesNotExist:
        return redirect("phrasebook:app")
