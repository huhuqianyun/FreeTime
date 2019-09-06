# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-28 13:13
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nick_name', models.CharField(default='', max_length=25, verbose_name='昵称')),
                ('real_name', models.CharField(default='', max_length=10, verbose_name='真实姓名')),
                ('student_id', models.CharField(default='', max_length=12, verbose_name='学号')),
                ('college_the_class', models.CharField(default='', max_length=50, verbose_name='学院班级')),
                ('phone_number', models.CharField(default='', max_length=11, verbose_name='手机号')),
                ('password', models.CharField(default='123456', max_length=12, verbose_name='密码')),
                ('qq', models.CharField(default='', max_length=13, verbose_name='QQ')),
                ('intergral', models.IntegerField(blank=True, default=0, verbose_name='积分')),
                ('credit_score', models.IntegerField(blank=True, default=5, verbose_name='信用分')),
                ('activity_state', models.CharField(choices=[('ing_activity', '正在参加活动'), ('no_activity', '未参加活动')], default='no_activity', max_length=50)),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6)),
                ('avator', models.ImageField(default='avator/default.jpg', upload_to='avator/%Y%M%D/', verbose_name='头像')),
                ('avator_sm', models.ImageField(default='avator/default.70x70.jpg', upload_to='avator/%Y%m%d/', verbose_name='头像缩略图')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]