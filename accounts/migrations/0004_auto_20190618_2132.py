# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-18 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190503_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=124, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='real_name',
            field=models.CharField(max_length=32, verbose_name='真实姓名'),
        ),
    ]
