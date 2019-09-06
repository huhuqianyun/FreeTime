from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from accounts.models import User
from django.contrib.auth.hashers import check_password as auth_check_password


# 用户登录
class LoginForm(forms.ModelForm):

    class Meta:
        #将在model中定义的User类
        model = User
        fields = ['student_id', 'password']
        # exclude = ()这个表示所有字段都用上

        widgets = {
            'student_id': widgets.TextInput(attrs={"class":"form-control", "placeholder": "学号"}),
            'password': widgets.PasswordInput(attrs={"class":"form-control", "placeholder": "密 码"}),
        }

# 密码检测
    def check_password(self):
        print('check password')
        student_id = self.cleaned_data['student_id']
        password = self.cleaned_data['password']
        try:
            student_id = User.objects.get(student_id=student_id)
            return student_id, auth_check_password(password, student_id.password)
        except:
            return None, False



# 用户注册
class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length="24",widget=widgets.TextInput(attrs={"class":"form-control", "placeholder": "请输入用户名"}))
    mobile = forms.CharField(label="手机号", max_length="24",widget=widgets.TextInput(attrs={"class":"form-control", "placeholder": "请输入手机号"}))
    password = forms.CharField(label="密 码", widget=widgets.PasswordInput(attrs={"class":"form-control", "placeholder": "请输入密码"}))
    password2 = forms.CharField(label="密 码2", widget=widgets.PasswordInput(attrs={"class":"form-control", "placeholder": "请再输入密码"}))
    mobile_captcha = forms.CharField(label="验证码", widget=widgets.TextInput(attrs={"style":"width: 160px;padding: 10px", "placeholder":"验证码", "error_messages": {"invalid": "验证码错误"}}))

    def clean_username(self):
        ret = User.objects.filter(username=self.cleaned_data.get("username"))
        if not ret:
            return self.cleaned_data.get("username")
        else:
            raise ValidationError("用户名已注册")

    def clean_mobile(self):
        ret = User.objects.filter(mobile=self.cleaned_data.get("mobile"))
        if not ret:
            return self.cleaned_data.get("mobile")
        else:
            raise ValidationError("手机号已绑定")

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if not data.isdigit():
            return self.cleaned_data.get("password")
        else:
            raise ValidationError("密码不能全是数字")

    def clean(self):
        if self.cleaned_data.get("password") == self.cleaned_data.get("password2"):
            return self.cleaned_data
        else:
            raise ValidationError("两次密码不一致")
