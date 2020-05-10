# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from .models import Student
from .models import Instructor
from .models import PeerAssessment
from .models import Team

from django.contrib import admin

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(PeerAssessment)
admin.site.register(Team)