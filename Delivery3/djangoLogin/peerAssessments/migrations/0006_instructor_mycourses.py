# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-09 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessments', '0005_auto_20200509_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='mycourses',
            field=models.ManyToManyField(to='peerAssessments.Course'),
        ),
    ]
