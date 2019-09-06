from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^/accounts/login/$', views.login, name='login'),
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^index$', views.Index.as_view(), name="index"),
    url(r'^attend_activities/$', views.attend_activities,name='attend_activities'),
    url(r'^organize_activities/$', views.organize_activities, name='organize_activities'),
    url(r'^myhome/$', views.myhome, name='myhome'),
]