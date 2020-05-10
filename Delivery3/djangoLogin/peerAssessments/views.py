# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Instructor
from .models import Course
from .models import PeerAssessment
from .models import Question
from .forms import PeerAssessmentForm
from .forms import EnterQuestionsForm

# Create your views here.

def allAssessments(request): 
    return render(request,"templates/allAssessments.html", {})

def createAssessment(request): 

    form = PeerAssessmentForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    # if request.method == 'POST':

    #     form = PeerAssessmentForm(request.POST)

    #     if form.is_valid():
    #         startdate = request.POST.get('startdate', '') 
    #         enddate = request.POST.get('enddate', '')
    #         title = request.POST.get('title', '')
    #         cid = request.POST.get('cid', '')
    #         number = request.POST.get('number', '')
    #         number = int(number)
    #         #for each question, make a question model and then add them all to questions.
    #         #request.session['number'] = number
    #         pa_obj = PeerAssessment(startdate = startdate, enddate = enddate, cid=cid)
    #         pa.obj.save()

    #         return HttpResponseRedirect('enterQuestions') #Redirect after POST
    # else:
    #     form = PeerAssessmentForm()

    return render(request,"createPeerAssessment.html", context)

def enterQuestions(request):
    #if request.method == 'POST':
        #form = EnterQuestionsForm(request.POST)
        #if form.is_valid():
         #   for i
    #data= request.POST.get('name')
    #number = request.session['number']
    #    numString += '3'
    # obj = PeerAssessment.objects.get(pid=1)
    # context = {
    #     'object': obj,
    #     'loopc': '123456789'
    # }

    form = EnterQuestionsForm(request.POST or None)
    if form.is_valid():
        myQuestions = form.save()
        myQuestions.private_field = "2"
        myQuestions.save()

    context = {
        'form': form
    }
    #context= {'data':data}
    return render(request,"enterQuestions.html", context)

def instructorHome(request):
    obj = Instructor.objects.get(iid=1)
    context = {
        'object': obj
    }
    return render(request,"home.html", context)

