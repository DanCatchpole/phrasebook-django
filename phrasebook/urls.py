
# phrasebook URLs
from django.conf.urls import url

from . import views
from .views import auth, general, language, category, word

app_name = "phrasebook"
urlpatterns = [
    url(r'^$', general.index, name="index"),
    url(r'^login/$', auth.login, name="login"),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^register/$', auth.register, name="register"),
    url(r'^first_login/$', general.first_login, name="first_login"),
    url(r'^app/$', general.app, name="app"),

    url(r'^language/register/$', language.register_user_language, name="register_user_language"),
    url(r'^language/change/$', general.lang_pick, name="lang_pick"),
    url(r'^language/change/(?P<flag_name>[a-z]+)/$', language.change_language, name="change_language"),
    url(r'^category/(?P<id>[0-9]+)/$', category.get_category, name="get_category"),
    url(r'^category/(?P<id>[0-9]+)/update/$', category.update_words, name="update_words"),
    url(r'^category/(?P<id>[0-9]+)/notes/$', category.category_notes, name="category_notes"),
    url(r'^category/(?P<id>[0-9]+)/notes/update/$', category.update_notes, name="update_notes"),
    url(r'^category/all/$', category.all_categories, name="all_categories"),
    url(r'^category/new/$', category.new_category, name="new_category"),
    url(r'^category/pin/(?P<id>[0-9]+)/$', category.pin_category, name="pin_category"),


    url(r'^word/new/(?P<cid>[0-9]+)/$', word.new_word, name="new_word"),
    url(r'^word/star/$', word.star_word, name="star_word"),
    url(r'^word/search/$', word.search_word, name="search_word"),
    url(r'^word/update/$', word.update_word, name="update_word"),
    url(r'^word/(?P<word_id>[0-9]+)/move/(?P<category_id>[0-9]+)/$', word.move_category, name="move_category"),

]
