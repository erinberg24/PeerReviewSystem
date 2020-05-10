# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-10 18:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peerAssessments', '0009_remove_instructor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedAssessments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer1', models.TextField()),
                ('answer2', models.TextField()),
                ('answer3', models.FloatField()),
                ('answer4', models.FloatField()),
                ('answer5', models.FloatField()),
                ('answer6', models.FloatField()),
                ('answer7', models.FloatField()),
                ('answer8', models.FloatField()),
                ('answer9', models.FloatField()),
                ('answer10', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peerAssessments.Course')),
                ('students', models.ManyToManyField(to='peerAssessments.Student')),
            ],
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question1Text',
            field=models.CharField(default='Question Text', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question1Type',
            field=models.CharField(choices=[('Multiple Choice', 'MC'), ('TEXT', 'T')], default='Multiple Choice', max_length=20),
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question2Text',
            field=models.CharField(default='Question Text', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question2Type',
            field=models.CharField(choices=[('Multiple Choice', 'MC'), ('TEXT', 'T')], default='Multiple Choice', max_length=20),
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question3Text',
            field=models.CharField(default='Question Text', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question3Type',
            field=models.CharField(choices=[('Multiple Choice', 'MC'), ('TEXT', 'T')], default='Multiple Choice', max_length=20),
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question4Text',
            field=models.CharField(default='Question Text', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question4Type',
            field=models.CharField(choices=[('Multiple Choice', 'MC'), ('TEXT', 'T')], default='Multiple Choice', max_length=20),
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question5Text',
            field=models.CharField(default='Question Text', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='peerassessment',
            name='question5Type',
            field=models.CharField(choices=[('Multiple Choice', 'MC'), ('TEXT', 'T')], default='Multiple Choice', max_length=20),
        ),
        migrations.AddField(
            model_name='completedassessments',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peerAssessments.PeerAssessment'),
        ),
        migrations.AddField(
            model_name='completedassessments',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peerAssessments.Student'),
        ),
    ]