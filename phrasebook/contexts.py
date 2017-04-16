from django.db.models import Count

from phrasebook.models import UserLanguage, Language, Category


def get_sidebar_args(request, extras):
    # print(request.session.)
    userlangs = list(UserLanguage.objects.filter(user=request.user))
    langs = [lang.language for lang in userlangs]
    lang = Language.objects.get(flag_name=request.session['current_language'])
    cats = list(Category.objects.filter(user=request.user, language=lang, pinned=True).order_by('name').annotate(num_words=Count('word')))
    ctx = {'name': request.user.first_name + " " + request.user.last_name[0:1] + ".",
           'first_name': request.user.first_name,
           'current_language': lang,
           'languages': langs, "languages_len": langs.__len__(),
           'username': request.user.username,
           'pinned_categories': cats}
    ctx.update(extras)
    return ctx
