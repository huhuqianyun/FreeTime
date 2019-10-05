from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Index(View):
    def get(self, request):
        category = Category.objects.all().values("id", "name")
        grades = Questions.DIF_CHOICES
        search = request.GET.get("search","")
        kwgs = {"category":category, "grades":grades,"search_key":search}
        return render(request, 'freeapp/index.html', kwgs)

def about(request):
    pk_url_kwarg = 'id'
    template_name = "question_detail.html"
    # 默认名：object
    context_object_name = "object"

    # 额外传递my_answer
    def get_context_data(self, **kwargs):
        # kwargs：字典、字典中的数据返回给html页面
        # self.get_object() => 获取当前id的数据（问题）
        question = self.get_object()  # 当前这道题目
        kwargs["my_answer"] = Answers.objects.filter(question=question, user=self.request.user)
        return super().get_context_data(**kwargs)

def attend_activities(request):
    return render(request, 'freeapp/attend_activities.html')

def organize_activities(request):
    return render(request, 'freeapp/organize_activities.html')

def myhome(request):
    def get(self, request):
        return render(request, "uc_profile.html")

    def post(self, request):
        ret_info = {"code": 200, "msg": "修改成功"}
        try:
            if request.POST.get("email"):
                request.user.email = request.POST.get("email")
            if request.POST.get("mobile"):
                print('change mobile')
                request.user.mobile = request.POST.get("mobile")
            if request.POST.get("qq"):
                request.user.qq = request.POST.get("qq")
            if request.POST.get("realname"):
                request.user.realname = request.POST.get("realname")
            request.user.save()
        except Exception as ex:
            ret_info = {"code": 200, "msg": "修改失败"}
        return render(request, "uc_profile.html", {"ret_info":ret_info})


class ChangePasswdView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "uc_change_passwd.html")

    def post(self, request):
        # from表单提交的数据
        old_password = request.POST.get("oldpassword")
        new_password1 = request.POST.get("newpassword1")
        new_password2 = request.POST.get("newpassword2")

        ## 前端验证 new_password1 == new_password2 才能提交

        if new_password1 != new_password2:
            ret_info = {"code":400, "msg":"新密码不一致"}
        else:
            user = auth.authenticate(username=request.user.username, password=old_password)
            if user:
                user.set_password(new_password1)
                user.save()
                auth.logout(request)
                # auth.update_session_auth_hash(request, user)
                ret_info = {"code":200, "msg":"修改成功"}
            else:
                ret_info = {"code": 400, "msg": "旧密码不正确"}
        return render(request, "uc_change_passwd.html", {"ret_info":ret_info})

    class Pays(LoginRequiredMixin, View):
        def get(self, request):
            """获取交租单信息"""
            today = datetime.date.today()
            # query_dict用于回传给html
            query_dict = request.GET
            contract_status = dict(Contract.CONTRACT_STATUS_CHOICES)
            # 查出所有待交，且实付大于0的交租单
            rentals = Rental.objects.filter(Q(rental_start_date__lte=today) | Q(rental_pay_amount__gt=0))
            # 根据交租时间、关键字等进一步筛选交租单
            start_date = request.GET.get("start")
            if start_date: rentals = rentals.filter(rental_pay_date__gte=start_date)
            end_date = request.GET.get("end")
            if end_date: rentals = rentals.filter(rental_pay_date__lte=end_date)
            keywords = request.GET.get("keywords")
            if keywords: rentals = rentals.filter(Q(contract__contract_shop_name__icontains=keywords) |
                                                  Q(contract__operator__operator_name__icontains=keywords) |
                                                  Q(contract__shop__shop_address__icontains=keywords))
            contract_status_id = request.GET.get("contract_status", 0)
            if contract_status_id and contract_status_id != "None":
                rentals = rentals.filter(contract__contract_status=contract_status_id)
            for item in rentals:
                item.contract_status = contract_status[item.contract.contract_status]