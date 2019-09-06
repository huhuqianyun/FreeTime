from django.db import models
from accounts.models import User

# Create your models here.
class Challenge_books(models.Model):
    challenge_id = models.AutoField(primary_key=True, verbose_name='挑战书ID')
    challenge_theme = models.CharField(max_length=50, verbose_name="主题", default='')
    challenge_brief = models.TextField(verbose_name='简介', default='', blank=True)
    challenge_rule = models.TextField(verbose_name='规则', default='', blank=True)
    challenge_status = models.CharField(max_length=25,choices=(("cha_ing",u"正在挑战"),("cha_end",u"挑战结束")),default="cha_ing")
    challenge_time = models.CharField(max_length=100, verbose_name="时间段", default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.challenge_id}"

    class Meta:
        verbose_name = "挑战书表"
        verbose_name_plural = verbose_name

