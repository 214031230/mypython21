# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 09:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180813_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostinfo',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='update_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='update_date',
        ),
    ]