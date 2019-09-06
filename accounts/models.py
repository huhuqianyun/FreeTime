
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.files import ImageFieldFile
import os
from freetime.settings import MEDIA_ROOT,THUMB_SIZE
from libs.images import make_thumb
# from freeapp.models import ActivityPart

# Create your models here.


class User(AbstractUser):
    # userid = models.IntegerField(max_length=25, primary_key=True,verbose_name="用户编号")
    student_id = models.CharField(max_length=12,primary_key=True, verbose_name="学号",default='')
    real_name = models.CharField(max_length=32, verbose_name="真实姓名")
    phone_number = models.CharField(max_length=11, verbose_name="手机号")
    password = models.CharField(max_length=32, verbose_name="密码", default='123456')
    email = models.EmailField(max_length=124,verbose_name="邮箱", default='')
    nick = models.CharField(max_length=32,verbose_name="昵称",default='')
    college_the_class = models.CharField(max_length=50,verbose_name="学院班级",default='')
    qq = models.CharField(max_length=13,verbose_name="QQ",default='')
    intergral = models.IntegerField(verbose_name="积分",blank=True,default=0)
    credit_score = models.IntegerField(verbose_name="信用分",blank=True,default=5)
    activity_state = models.CharField(max_length=50,choices=(("ing_activity",u"正在参加活动"),("no_activity",u"未参加活动")),default="no_activity")
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default="female")
    avator = models.ImageField(upload_to="avator/%Y%M%D/", default="avator/default.jpg", verbose_name="头像")
    avator_sm = models.ImageField("头像缩略图", upload_to="avator/%Y%m%d/", default='avator/default.70x70.jpg')
    # 上传学生卡
    # activity_part_form = models.ForeignKey(ActivityPart,on_delete=models.CASCADE,default=' ')


    def __str__(self):
        return f"{self.student_id}"

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


    def save(self, *args, **kwargs):
        # 将上传的图片先保存
        super().save()
        #如果没有上传图片，使用的是默认图片则不生成缩略图
        if self.avator.name == 'avator/default.jpg':
            return
        base, ext = os.path.splitext(self.avator.name)
        # 从头像中生成缩略图
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.avator.name), size=THUMB_SIZE)
        # 缩略图的保存文件全路径
        thumb_path = os.path.join(MEDIA_ROOT, base + f'.{THUMB_SIZE}x{THUMB_SIZE}' + ext)
        # 缩略图相对路径
        relate_thumb_path = os.path.join('/'.join(self.avator.name.split('/')[:-1]), os.path.basename(thumb_path))
        relate_thumb_path = base + f'.{THUMB_SIZE}x{THUMB_SIZE}' + ext
        # 保存缩略图
        thumb_pixbuf.save(thumb_path)
        # 保存字段值
        self.avator_sm = ImageFieldFile(self, self.avator_sm, relate_thumb_path)
        super().save() # 再保存一下，包括缩略图等



