# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-05-09 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200509_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='img/1.jpg', upload_to='img/', verbose_name='Изображение'),
        ),
    ]
