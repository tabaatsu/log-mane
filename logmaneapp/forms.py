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

class AthleteRecordsForm(forms.ModelForm):

    athlete_id = forms.ModelChoiceField(queryset=Athlete.objects.all(), empty_label='選手名')
    discipline = forms.ModelChoiceField(queryset=Discipline.objects.all(), empty_label='種目')
    class Meta:
        model = Athlete_records
        fields = ('athlete_id','discipline', 'personal_best', 'university_best', 'valid_record')
        labels = {
                'personal_best': '自己ベスト',
                'university_best': '大学ベスト',
                'valid_record': '有効記録'
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['athlete_id'].queryset = Athlete.objects.all()
        self.fields['athlete_id'].empty_label = '選手名'
        self.fields['discipline'].queryset = Discipline.objects.all()
        self.fields['discipline'].empty_label = '種目'
