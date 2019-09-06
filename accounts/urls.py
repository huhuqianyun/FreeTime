from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^login/$', views.Login.as_view(),name='login'),
    # url(r'^login/$', views.login,name='login'),
    url(r'^register/$', views.Register.as_view(),name='register'),
    # url(r'^register/$', views.register, name='register'),
    url(r'^unlogin/$', views.unlogin, name='unlogin'),
    url(r'^myhome/$', views.myhome, name='myhome'),

    #类视图展示静态模板而不用展示动态内容比较方便——在将form表单渲染到模板上
    # url(r'^login/$', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    # url(r'^register/$', TemplateView.as_view(template_name='accounts/register.html'), name='register'),

]