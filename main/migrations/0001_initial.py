# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-05-04 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('specialization', models.CharField(max_length=300, verbose_name='Специализация')),
                ('info', models.CharField(max_length=10000, verbose_name='Инфо о мастере')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата приема ')),
                ('time', models.CharField(max_length=5, verbose_name='Время приема ')),
                ('patient_name', models.CharField(max_length=300, verbose_name='ФИО ')),
                ('patient_info', models.CharField(max_length=10000, verbose_name='Инфо о клиенте ')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Master', verbose_name='Мастер ')),
            ],
            options={
                'verbose_name': 'Прием',
                'verbose_name_plural': 'Приемы',
            },
        ),
    ]
