
# phrasebook URLs
from django.conf.urls import url

from . import views

app_name = "phrasebook"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/?$', views.login, name="login"),
    url(r'^logout/?$', views.logout, name='logout'),
    url(r'^register/?$', views.register, name="register"),
    url(r'^app/?$', views.app, name="app")
]
