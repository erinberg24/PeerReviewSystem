# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Instructor
from .models import Student
from .models import Course
from .models import PeerAssessment
from .forms import PeerAssessmentForm

from django.contrib.auth.decorators import login_required
# Create your views here.



def allAssessments(request): 
    return render(request,"templates/allAssessments.html", {})

def createPeerAssessment(request): 
    current_user = request.user.email
    if request.method == 'POST':
        form = PeerAssessmentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            teacher = Instructor.objects.get(email=current_user)
            instance.iid = teacher
            instance.save()
            #newdata = models.PeerAssessment.objects.get(name=instance.name) # get it back
        else:
            print(form.errors)
#        return HttpResponseRedirect('/home/')
    else:
        form = PeerAssessmentForm()

    return render(request,"createPeerAssessment.html", {'form': form})

# def enterQuestions(request):
#     #if request.method == 'POST':
#         #form = EnterQuestionsForm(request.POST)
#         #if form.is_valid():
#          #   for i
#     #data= request.POST.get('name')
#     #
#     #    numString += '3'
#     # obj = PeerAssessment.objects.get(pid=1)
#     # context = {
#     #     'object': obj,
#     #     'loopc': '123456789'
#     # }
#     if request.method == 'POST':
#         form = EnterQuestionsForm(request.POST or None)
#         if form.is_valid():
#             myQuestions = form.save()
#             myQuestions.private_field = "2"
#             myQuestions.save()
#             return HttpResponseRedirect('/home/')
#     else:
#         form = EnterQuestionsForm()
    
#     return render(request,"enterQuestions.html", {'form': form})

@login_required
def studentTeacherLinking(request):
    isTeacher = request.user.is_teacher
    current_user = request.user.email
    print current_user

    if (isTeacher == True):
        obj = Instructor.objects.get(email=current_user)
        pas = PeerAssessment.objects.filter(iid=obj.iid)
        context = {
            'object': obj,
            'pas': pas
        }
        return render(request,"home.html", context)
    else:
        obj = Student.objects.get(email=current_user)
        context = {
            'object': obj
        }
        return render(request,"home.html", context)



def takePeerAssessment(request):
    if request.method == 'POST':
        form = StudentResponse(request.POST)
        if form.is_valid():
            form.save()
        context = {
            'form': form
        }
        return HttpResponseRedirect('home')
    else:     
        obj = PeerAssessment.objects.get(pid=1)
        form = StudentResponse()
        context = {
            'object': obj,
            'form': form
        }
    return render(request,"takePeerAssessment.html", context)


# this needs to be updated
# def studentResults(request):
#     obj = studentResults.objects.get(pid=1)
#     context = {
#         'object': obj
#     }
#     return render(request,"",context)

