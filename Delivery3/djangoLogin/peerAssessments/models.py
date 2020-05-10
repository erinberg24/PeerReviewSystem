# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    iid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length = 15)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20, unique=True)
    eagleid = models.IntegerField(unique=True)
    password = models.CharField(max_length = 20)
    mycourses = models.ManyToManyField(Course)

    def __str__(self):
        return self.fname + " " + self.lname

class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    qType = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice")
    questionText = models.CharField(max_length=500)
    pid = models.ForeignKey('PeerAssessment', on_delete=models.CASCADE)

    def __str__(self):
        title = self.questionText
        return title

class PeerAssessment(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField() 
    number = models.IntegerField()
    questions = models.ManyToManyField(Question)
    iid = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    cid = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        title = str(self.pid)
        return title
    
# class Team(models.Model):
#     tid = models.AutoField(primary_key=True)

# class Answers(models.Model):
#     qid = models.AutoField(primary_key=True)
#     aType = models.CharField(max_length= 20, choices=QUESTION_TYPES, default="Multiple Choice")
#     answerText = models.CharField(max_length=500)
#     pid = models.ForeignKey('PeerAssessment', on_delete=models.CASCADE)
#     sid = models.ForeignKey('Student', on_delete=models.CASCADE)

#     def __str__(self):
#         title = self.questionText
#         return title

# class CompletedAssessments(model.Model):
#     mcAnswers = models.ManyToManyField(Answers)
#     textAnswers = models.ManyToManyField(Answers)
#     sid = models.ForeignKey('Student', on_delete=models.CASCADE)
#     pid = models.ForeignKey('PeerAssessment', on_delete=models.CASCADE)



#in admin.py
#from .models import Course
# admin.site.register(Course)

#in terminal python manage.py makemigrations appname