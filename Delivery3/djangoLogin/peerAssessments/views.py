# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def allAssessments(request): 
    return render(request,"templates/allAssessments.html")