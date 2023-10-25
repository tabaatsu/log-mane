from django import forms
from .models import Athlete, Discipline, Athlete_records, Event, Event_records, Stage, Division

class AthleteForm(forms.ModelForm):
    
    class Meta:
        model = Athlete
        fields = ('name', 'gender', 'grade', 'group')
        labels = {
            'name': '選手名',
            'gender': '性別',
            'grade': '学年',
            'group': 'パート'
        }

