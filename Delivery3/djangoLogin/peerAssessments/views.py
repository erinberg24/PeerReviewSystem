# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Instructor
from .models import Student
from .models import Course
from .models import PeerAssessment
from .models import Question
from .forms import PeerAssessmentForm
from .forms import EnterQuestionsForm

from django.contrib.auth.decorators import login_required
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

@login_required
def studentTeacherLinking(request):
    isTeacher = request.user.is_teacher
    current_user = request.user.email
    print current_user

    if (isTeacher == True):
        obj = Instructor.objects.get(email=current_user)
        context = {
            'object': obj
        }
        return render(request,"home.html", context)
    else:
        obj = Student.objects.get(email=current_user)
        context = {
            'object': obj
        }
        return render(request,"home.html", context)




def takePeerAssessment(request):
    obj = PeerAssessment.objects.get(pid=1)
    context = {
        'object': obj
    }
    return render(request,"takePeerAssessment.html", context)