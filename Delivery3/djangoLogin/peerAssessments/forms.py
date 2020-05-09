class PeerAssessmentForm(forms.Form):
    title = forms.CharField()
    cid = forms.FloatField()
    startdate = forms.DateField()
    enddate = forms.DateField()
    questions = forms.
