from django.conf.urls import url

from . import views


urlpatterns = [
    url('allAssessments/', views.allAssessments, name='allAssessments')
]