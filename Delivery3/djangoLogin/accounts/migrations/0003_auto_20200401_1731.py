# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-01 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200401_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='Are they a Teacher?'),
        ),
    ]
