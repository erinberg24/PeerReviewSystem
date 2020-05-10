# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings



SEMESTER_CHOICES =  (("Fall", "F"), ("Spring", "S"))
QUESTION_TYPES = (("Multiple Choice", "MC"), ("TEXT", "T"))

# Create your models here.
class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length = 30)
    code = models.CharField(max_length=20)
    section = models.IntegerField()
    year = models.IntegerField()
    semester = models.CharField(max_length= 8, choices=SEMESTER_CHOICES, default="FALL")
    iid = models.ForeignKey('Instructor', on_delete=models.CASCADE)

    def __str__(self):
        return self.courseName

class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length = 15)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20, unique=True)
    eagleid = models.IntegerField(unique=True)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return self.fname + " " + self.lname

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
    
class Team(models.Model):
    tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
     

class CompletedAssessments(models.Model):
    sid = models.ForeignKey('Student', on_delete=models.CASCADE)
    pid = models.ForeignKey('PeerAssessment', on_delete=models.CASCADE)
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.FloatField()
    answer4 = models.FloatField()
    answer5 = models.FloatField()
    answer6 = models.FloatField()
    answer7 = models.FloatField()
    answer8 = models.FloatField()
    answer9 = models.FloatField()
    answer10 = models.FloatField()

    def __str__(self):
         title = self.sid
         return title



#in admin.py
#from .models import Course
# admin.site.register(Course)

#in terminal python manage.py makemigrations appname