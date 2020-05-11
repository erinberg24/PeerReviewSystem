from django.forms import ModelForm
from django import forms

from .models import PeerAssessment
from .models import CompletedAssessments
from .models import Team
from .models import Course
from .models import Student

class PeerAssessmentForm(forms.ModelForm):
    class Meta:
        model = PeerAssessment
        exclude = ["iid"]
        fields = [
            'name', 
            'cid', 
            'startDate', 
            'endDate', 
            'question1Type',
            'question1Text',
            'question2Type',
            'question2Text',
            'question3Type',
            'question3Text',
            'question4Type',
            'question4Text',
            'question5Type',
            'question5Text',
            'question6Type',
            'question6Text',
            'question7Type',
            'question7Text',
            'question8Type',
            'question8Text',
            'question9Type',
            'question9Text',
            'question10Type',
            'question10Text'
        ]
        widgets = {
        'startDate': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'endDate': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
    }

class StudentResponseForm(forms.ModelForm):
    class Meta:
        model = CompletedAssessments
        fields = [
            'sid',
            'pid',
            'answer1',
            'answer2',
            'answer3',
            'answer4',
            'answer5',
            'answer6',
            'answer7',
            'answer8',
            'answer9',
            'answer10'
        ]
        widgets = {
            'answer3': forms.NumberInput(attrs={'style': 'width:10ch'}),
            'answer4': forms.NumberInput(attrs={'style': 'width:10ch'}),
            'answer5': forms.NumberInput(attrs={'style': 'width:10ch'}),
            'answer6': forms.NumberInput(attrs={'style': 'width:10ch'}),
            'answer7': forms.NumberInput(attrs={'style': 'width:10ch'}),
            'answer8': forms.NumberInput(attrs={'style': 'width:10ch'}),
            'answer9': forms.NumberInput(attrs={'style': 'width:10ch'}),
            'answer10': forms.NumberInput(attrs={'style': 'width:10ch'}),
        }

class createTeamsForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'tid',
            'name',
            'theCourse',
            'students'
        ]
    def __init__(self, *args, **kwargs):
        super(createTeamsForm, self).__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.filter(courses=2)


    # name = forms.CharField()
    # cid = forms.IntegerField()
    # startdate = forms.DateField()
    # enddate = forms.DateField()
    # number = forms.IntegerField()
        

    # def __init__(self, *args, **kwargs):
    #     super(self).__init__(*args, **kwargs)
    #     questions = Question.objects.filter(
    #         pid=self.instance
    #     )
    #     for i in range(len(questions)+1):
    #         field_name = 'question_%s' % (i,)
    #         self.fields[field_name] = forms.CharField(required=False)

    #         try:
    #             self.initial[field_name] = questions[i].question
    #         except IndexError:
    #             self.initial[field_name] = ""
    #         #create an extra blank field 
    #         field_name = 'question_%s' % (i+1,)
    #         self.fields[field_name] = forms.CharField(required=False)
    
    # def clean(self):
    #     questions = set()
    #     i = 0
    #     field_name = 'question_%s' % (i,)
    #     while self.cleaned_data.get(field_name):
    #         question = self.cleaned_data[field_name]
    #         questions.add(question)
    #         i+=1
    #         field_name = 'question_%s' % (i,)
    #     self.cleaned_data["questions"] = questions

    # def save(self):
    #     pid = self.instance
    #     pid.question_set.all().delete()
    #     for question in self.cleaned_data["questions"]:
    #         PeerAssessment.objects.create(
    #             pid=pid,
    #             questions=question
    #         )



