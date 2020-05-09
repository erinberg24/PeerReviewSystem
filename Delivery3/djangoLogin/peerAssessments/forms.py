class PeerAssessmentForm(forms.ModelForm):
    title = forms.CharField(required=True)
    cid = forms.FloatField()
    startdate = forms.DateField(required=True)
    enddate = forms.DateField(required=True)
    number = forms.FloatField()
    question = forms.CharField()
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = Question.objects.filter(
            pid=self.instance
        )
        for i in range(len(questions)+1):
            field_name = 'question_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)

