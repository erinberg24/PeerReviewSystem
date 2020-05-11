# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator

SEMESTER_CHOICES =  (("Fall", "F"), ("Spring", "S"))
QUESTION_TYPES = (("Multiple Choice", "MC"), ("TEXT", "T"))

# Create your models here.

class PeerAssessment(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField() 
    iid = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    cid = models.ForeignKey('Course', on_delete=models.CASCADE)
    question1Text = models.CharField(max_length=500)
    question1Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice") 
    question2Text = models.CharField(max_length=500)
    question2Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice") 
    question3Text = models.CharField(max_length=500)
    question3Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice") 
    question4Text = models.CharField(max_length=500)
    question4Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice") 
    question5Text = models.CharField(max_length=500)
    question5Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice")
    question6Text = models.CharField(max_length=500)
    question6Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice")
    question7Text = models.CharField(max_length=500)
    question7Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice")
    question8Text = models.CharField(max_length=500)
    question8Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice")
    question9Text = models.CharField(max_length=500)
    question9Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice")
    question10Text = models.CharField(max_length=500)
    question10Type = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice")

    def __str__(self):
        title = str(self.name)
        return title

class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length = 15)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20, unique=True)
    eagleid = models.IntegerField(unique=True)
    password = models.CharField(max_length = 20)
    #courses = models.ManyToManyField(Course)
    completedAssessments = models.ManyToManyField(PeerAssessment)

    def __str__(self):
        return self.fname + " " + self.lname

class Team(models.Model):
    tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    theCourse = models.ForeignKey('Course', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    livePAs = models.ManyToManyField(PeerAssessment)

    def __str__(self):
        title = str(self.name)
        return title

class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length = 30)
    code = models.CharField(max_length=20)
    section = models.IntegerField()
    year = models.IntegerField()
    semester = models.CharField(max_length= 8, choices=SEMESTER_CHOICES, default="FALL")
    iid = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.courseName

class Instructor(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True) 
    iid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length = 15)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20, unique=True)
    eagleid = models.IntegerField(unique=True)
    password = models.CharField(max_length = 20)
    mycourses = models.ManyToManyField(Course)

    def __str__(self):
        return self.fname + " " + self.lname


class CompletedAssessments(models.Model):
    sid = models.ForeignKey('Student', on_delete=models.CASCADE)
    pid = models.ForeignKey('PeerAssessment', on_delete=models.CASCADE)
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    answer4 = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    answer5 = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    answer6 = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    answer7 = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    answer8 = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    answer9 = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    answer10 = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self):
         title = self.sid
         return title



#in admin.py
#from .models import Course
# admin.site.register(Course)

#in terminal python manage.py makemigrations appname