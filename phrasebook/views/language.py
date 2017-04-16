from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect

from phrasebook.models import Language, UserLanguage
from ..sessiontools import update_session


@login_required()
def register_user_language(request):
    if request.method == "GET":
        lang = request.GET.get('langVal')
    elif request.method == "POST":
        lang = request.POST.get('langVal')
    else:
        return JsonResponse({"error": "Not a valid method"})

    language = Language.objects.get(flag_name=lang)
    user_lang = UserLanguage(user=request.user, language=language)
    user_lang.save()
    request.session.__setitem__('current_language', user_lang.language.flag_name)
    update_session(request)
    return JsonResponse({"success": language.english_name + " saved successfully"})

@login_required()
def change_language(request, flag_name):
    try:
        user_lang = UserLanguage.objects.get(user=request.user, language__flag_name=flag_name)
        request.session.__setitem__('current_language', user_lang.language.flag_name)
        return redirect('phrasebook:app')
    except ObjectDoesNotExist:
        return JsonResponse({"status": "error"})
