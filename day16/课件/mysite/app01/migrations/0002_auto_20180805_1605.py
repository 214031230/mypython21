# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-05 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
