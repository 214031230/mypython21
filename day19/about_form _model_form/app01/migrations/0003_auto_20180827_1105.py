# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 03:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180827_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者管理', 'verbose_name_plural': '作者管理'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书管理', 'verbose_name_plural': '图书管理'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版社管理', 'verbose_name_plural': '出版社管理'},
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='app01.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='address',
            field=models.TextField(verbose_name='出版社地址'),
        ),
    ]
