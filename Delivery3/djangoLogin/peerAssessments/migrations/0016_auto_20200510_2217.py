# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessments', '0015_student_completedassessments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='course',
            new_name='theCourse',
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='teams',
            field=models.ManyToManyField(to='peerAssessments.Team'),
        ),
    ]
