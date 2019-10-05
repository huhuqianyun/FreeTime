from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.views.generic import View
import logging
from .forms import LoginForm, RegisterForm
from .models import User
logger = logging.getLogger('account')

# Create your views here.

class Login(View):
    def post(self, request):
        student_id = request.POST.get('student_id')
        student_pwd = request.POST.get('student_pwd')
        user = auth.authenticate(username=student_id, password=student_pwd)
        if user is not None and user.is_active:
            auth.login(request, student_id)
            logger.debug("用户{}登录成功".format(user))
            # print(111111111111)
            # print(student_id,student_pwd)
            # print(user)
            return render(request, 'freeapp/index.html')
        else:
            logger.error("用户{}登录失败".format(user))

    def get(self,request):
        print(request)
        return render(request, 'accounts/login.html')

class Register(View):
    def post(self, request):
        student_id = request.POST.get('student_id')
        qq = request.POST.get('qq')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = User.objects.create_user(username=student_id,student_id=student_id,qq=qq,password=password2)
        user.save()
        print(111111111111111,user)
        code = 200
        msg = '添加成功'
        result = {'code': code, 'msg': msg}
        return JsonResponse(result)
        # return render(request, 'accounts/register.html')

    def get(self, request):
        return render(request, 'accounts/register.html',locals())



def unlogin(request):
    return render(request,'accounts/unlogin.html')

def myhome(request):
    return render(request,'accounts/myhome.html')

def logout(request):
    logger.debug('{request.user}退出系统!')
    auth.logout(request)
    return redirect(reverse('accounts:login'))


