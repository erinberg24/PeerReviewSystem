# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 04:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessments', '0008_instructor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='user',
        ),
    ]
