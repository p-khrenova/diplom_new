# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-05-10 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200509_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=222, verbose_name='ФИО')),
                ('mail', models.CharField(max_length=200, verbose_name='Email')),
                ('message', models.CharField(max_length=400, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Форма',
                'verbose_name_plural': 'Формы',
            },
        ),
    ]
