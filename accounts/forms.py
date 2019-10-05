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
    student_id = forms.CharField(label="学号", max_length="12",widget=widgets.TextInput(attrs={"class":"form-control", "placeholder": "请输入学号"}))
    qq = forms.CharField(label="QQ号", max_length="24",widget=widgets.TextInput(attrs={"class":"form-control", "placeholder": "请输入QQ号"}))
    password = forms.CharField(label="密 码", widget=widgets.PasswordInput(attrs={"class":"form-control", "placeholder": "请输入密码"}))
    password2 = forms.CharField(label="密 码2", widget=widgets.PasswordInput(attrs={"class":"form-control", "placeholder": "请再输入密码"}))
    # mobile_captcha = forms.CharField(label="验证码", widget=widgets.TextInput(attrs={"style":"width: 160px;padding: 10px", "placeholder":"验证码", "error_messages": {"invalid": "验证码错误"}}))

    def clean_student_id(self):
        ret = User.objects.filter(student_id=self.cleaned_data.get("student_id"))
        if not ret:
            return self.cleaned_data.get("student_id")
        else:
            raise ValidationError("学号已注册")

    def clean_qq(self):
        ret = User.objects.filter(qq=self.cleaned_data.get("qq"))
        if not ret:
            return self.cleaned_data.get("qq")
        else:
            raise ValidationError("QQ号已绑定")

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
