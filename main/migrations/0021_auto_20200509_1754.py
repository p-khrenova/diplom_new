# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-05-09 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200509_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='img/users/1.jpg', upload_to='img/users/', verbose_name='Изображение'),
        ),
    ]
