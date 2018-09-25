
# phrasebook URLs
from django.urls import path

from .views import auth, general, language, category, word

app_name = "phrasebook"
urlpatterns = [
    path('', general.index, name="index"),
    path('login/', auth.login, name="login"),
    path('logout/', auth.logout, name='logout'),
    path('register/', auth.register, name="register"),
    path('first_login/', general.first_login, name="first_login"),
    path('app/', general.app, name="app"),
    path('all/', word.all, name="all_words"),
    path('profile/', general.profile, name="profile"),

    path('api/language/register/', language.register_user_language, name="register_user_language"),
    path('language/registerfirst/', language.first_login, name="registerfirst"),
    path('language/change/', general.lang_pick, name="lang_pick"),
    path('language/change/<str:flag_name>/', language.change_language, name="change_language"),
    path('category/<int:id>/', category.get_category, name="get_category"),
    path('category/<int:id>/update/', category.update_words, name="update_words"),
    path('category/<int:id>/getlink/', category.share_link, name="share_link"),
    path('category/<int:id>/notes/', category.category_notes, name="category_notes"),
    path('category/<int:id>/notes/update/', category.update_notes, name="update_notes"),
    path('category/all/', category.all_categories, name="all_categories"),
    path('category/new/', category.new_category, name="new_category"),
    path('category/pin/<int:id>/', category.pin_category, name="pin_category"),

    path('c/<str:id>/', category.shared_category, name="shared_category"),


    path('word/new/<int:cid>/', word.new_word, name="new_word"),
    path('word/star/', word.star_word, name="star_word"),
    path('word/search/', word.search_word, name="search_word"),
    path('word/update/', word.update_word, name="update_word"),
    path('word/<int:word_id>/move/<int:category_id>/', word.move_category, name="move_category"),


]
