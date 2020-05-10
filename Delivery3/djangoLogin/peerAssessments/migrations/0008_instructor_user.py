# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 01:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peerAssessments', '0007_auto_20200509_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]