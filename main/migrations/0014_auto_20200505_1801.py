# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-05-05 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200505_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='img/users/'),
        ),
    ]
