# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

SEMESTER_CHOICES =  (("Fall", "F"), ("Spring", "S"))

# Create your models here.
class Course(models.Model):
    cid = models.IntegerField(primary_key=True)
    courseName = models.CharField(max_length = 30)
    code = models.IntegerField()
    section = models.IntegerField()
    year = models.IntegerField()
    semester = models.CharField(max_length= 8, choices=SEMESTER_CHOICES, default="FALL")

    def __str__(self):
        return self.courseName

class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length = 15)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20, unique=True)
    eagleid = models.IntegerField(unique=True)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.fname + " " + self.lname

class Instructor(models.Model):
    iid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length = 15)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20, unique=True)
    eagleid = models.IntegerField(unique=True)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.fname + " " + self.lname

class PeerAssessment(models.Model):
    pid = models.IntegerField(primary_key=True)
    questions = models.TextField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    iid = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    cid = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.pid

#in admin.py
#from .models import Course
# admin.site.register(Course)

#in terminal python manage.py makemigrations appname