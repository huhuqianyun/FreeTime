from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^get_captcha/$', views.get_captcha,name='get_captcha'),

]