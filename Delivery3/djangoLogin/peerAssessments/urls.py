from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import enterQuestions, allAssessments


urlpatterns = [
    url('allAssessments/', views.allAssessments, name='allAssessments'),  
]