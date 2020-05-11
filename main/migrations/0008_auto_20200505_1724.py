# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-05-05 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_reception_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterusl',
            name='master',
        ),
        migrations.AddField(
            model_name='master',
            name='uslugi',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.MasterUsl', verbose_name='Услуги'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reception',
            name='uslugi',
            field=models.CharField(max_length=100, verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='media/img/users/1.jpg', upload_to='media/img/users', verbose_name='Изображение'),
        ),
    ]
