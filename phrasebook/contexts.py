import math
from django.db.models import Count

from phrasebook.models import UserLanguage, Language, Category, UserProgress


def get_sidebar_args(request, extras):
    # print(request.session.)
    userlangs = list(UserLanguage.objects.filter(user=request.user))
    langs = [lang.language for lang in userlangs]
    lang = Language.objects.get(flag_name=request.session['current_language'])
    userDetails = UserProgress.objects.get(user=request.user)
    lvl_details = calculate_level_percentage(userDetails.xp)
    cats = list(Category.objects.filter(user=request.user, language=lang, pinned=True).order_by('name').annotate(num_words=Count('word')))
    ctx = {'name': request.user.first_name + " " + request.user.last_name[0:1] + ".",
           'first_name': request.user.first_name,
           'current_language': lang,
           'languages': langs, "languages_len": langs.__len__(),
           'five_languages': langs[:5],
           'username': request.user.username,
           'pinned_categories': cats,
           'level': lvl_details['level'],
           'xp_percentage': lvl_details['xp_percentage'],
           'next_level_xp': lvl_details['xp_next'] - lvl_details['xp_prev'],
           'xp_current_relative': userDetails.xp - lvl_details['xp_prev']
           }
    ctx.update(extras)
    return ctx


def calculate_level_percentage(xp):
    level = math.floor((5 + math.sqrt(25 + 20*xp))/10)
    xp_base = 5*level*level - 5*level
    xp_above  = 5*(level+1)*(level+1) - 5*(level+1)
    xp_percentage = (xp - xp_base) * 100/(xp_above - xp_base)
    to_next_level = xp_above - xp
    return {'level': level, 'xp_percentage': xp_percentage, 'next_level': to_next_level, 'xp_next': xp_above, 'xp_prev': xp_base}