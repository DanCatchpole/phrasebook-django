from .models import *


def update_session(request):
    """
    Will be run on:
     - Login
     - Add category
     - Add word
     - Reorganise category
     - Pin category
    """
    # get languages for this user
    userlangs = list(UserLanguage.objects.filter(user=request.user))
    langs = [lang.language.flag_name for lang in userlangs]
    print(langs)
    request.session.__setitem__('user_languages', langs)
