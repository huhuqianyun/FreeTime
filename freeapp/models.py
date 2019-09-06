from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.
'''
blank = True 意味这个字段不是必需的，在客户端不是必填选项。
null = True意味这个数据库里这个字段可以存储为null空值。
Django对于空白的CharField和TextField永远不会存为null空值，而是存储空白字符串''，所以正确的做法是设置default=''。
'''

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True,max_length=30,verbose_name="活动ID")
    manager = models.CharField(max_length=12,verbose_name="活动负责人",default='') # 存储参与人的学号
    relation_qq = models.CharField(max_length=13,verbose_name="联系方式",default='')
    adress_act = models.CharField(max_length=80,verbose_name="活动地点",default='')
    theme = models.CharField(max_length=50,verbose_name="主题",default='')
    content = models.TextField(verbose_name="活动内容",default='')
    time_begin = models.DateTimeField(max_length=12,verbose_name="发起活动时间",default=timezone.now)
    time_end = models.DateTimeField(max_length=12,verbose_name="结束活动时间",default=timezone.now)
    num_min = models.IntegerField(verbose_name="最少参加人数",default=1)
    num_max = models.IntegerField(verbose_name="最多参加人数",default=8)
    cost = models.CharField(max_length=50,choices=(("pay",u"产生费用"),("free",u"免费")),default="free")
    position = models.TextField(verbose_name="职位安排",default='')
    intergral_add = models.IntegerField(verbose_name="所得积分",default=3)
    credit_add = models.IntegerField(verbose_name="所得信用分",default=1)
    user = models.ManyToManyField(User,verbose_name="用户",related_name='+')
    # 活动相册
    def __str__(self):
        return f"{self.activity_id}"

    class Meta:
        verbose_name = "活动表"
        verbose_name_plural = verbose_name

class ActivityPart(models.Model):
    activity_part_id = models.AutoField(primary_key=True,verbose_name='活动参与表ID')
    participant = models.CharField(max_length=12,verbose_name="参与人",default='') # 存储参与人的学号
    activity_ing = models.CharField(max_length=30,verbose_name='正在参加的活动',default='')
    activity_will = models.CharField(max_length=100,verbose_name='将要参加的活动',default='')
    activity_end = models.TextField(verbose_name='参加过的活动',default='',blank=True,)
    now_integer = models.IntegerField(verbose_name='积分',default=3)
    now_credit = models.IntegerField(verbose_name='信用分',default=1)
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    def __str__(self):
        return f"{self.activity_part_id}"

    class Meta:
        verbose_name = "活动参与表"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True,max_length=30,verbose_name='评论表ID')
    participant = models.CharField(max_length=12,verbose_name="参与人",default='') # 存储参与人的学号
    comment = models.TextField(verbose_name='评价',default='',blank=True)
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE)
    activity_part = models.ForeignKey(ActivityPart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.comment_id}"

    class Meta:
        verbose_name = "评论表"
        verbose_name_plural = verbose_name