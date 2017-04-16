from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
    update_session(request)
    return JsonResponse({"success": language.english_name + " saved successfully"})
