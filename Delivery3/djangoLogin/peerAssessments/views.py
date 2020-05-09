# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Instructor
from .models import Course
from .models import PeerAssessment
from .models import Question

# Create your views here.

def allAssessments(request): 
    return render(request,"templates/allAssessments.html", {})

def createAssessment(request): 
    if request.method == 'POST':

        form = PeerAssessmentForm(request.POST)
        if form.is_valid():
            startdate = request.POST.get('startdate', '') 
            enddate = request.POST.get('enddate', '')
            title = request.POST.get('title', '')
            cid = request.POST.get('cid', '')

            #for each question, make a question model and then add them all to questions.

            pa_obj = PeerAssessment(startdate = startdate, enddate = enddate, questions = questions, iid=iid, cid=cid)
            pa.obj.save()

            #return HttpResponseRedirect(reverse('jobs:cost')) #Redirect after POST
    else:
        form = PeerAssessmentForm()

    return render(request,"templates/createAssessment.html", {'form': form,})

def instructorHome(request):
    obj = Instructor.objects.get(iid=1)
    context = {
        'object': obj
    }
    return render(request,"home.html", context)

