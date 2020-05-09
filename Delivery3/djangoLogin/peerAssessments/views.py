# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Instructor
from .models import Course

# Create your views here.

def allAssessments(request): 
    return render(request,"templates/allAssessments.html", {})

def createAssessment(request): 
    return render(request,"templates/createAssessment.html", {})

def instructorHome(request):
    obj = Instructor.objects.get(iid=1)
    context = {
        'object': obj
    }
    return render(request,"home.html", context)

