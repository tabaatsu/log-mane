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

class EventForm(forms.ModelForm):

        class Meta:
            model = Event
            fields = ('event', 'date')
            labels = {
                'event': '大会名',
                'date': '日付'
            }

class EventRecordsForm(forms.ModelForm):

        athlete_id = forms.ModelChoiceField(queryset=Athlete.objects.all(), empty_label='選手名')
        event = forms.ModelChoiceField(queryset=Event.objects.all(), empty_label='大会名')
        division = forms.ModelChoiceField(queryset=Division.objects.all(), empty_label='区分')
        discipline = forms.ModelChoiceField(queryset=Discipline.objects.all(), empty_label='種目')
        stage = forms.ModelChoiceField(queryset=Stage.objects.all(), empty_label='ステージ')
        class Meta:
            model = Event_records
            fields = ('athlete_id', 'event', 'division', 'discipline', 'stage', 'heat', 'place', 'record','wind')
            labels = {
                    'record': '記録',
                    'heat': '組',
                    'place': '順位',
                    'wind': '風速',
                }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['athlete_id'].queryset = Athlete.objects.all()
            self.fields['athlete_id'].empty_label = '選手名'
            self.fields['discipline'].queryset = Discipline.objects.all()
            self.fields['discipline'].empty_label = '種目'
            self.fields['event'].queryset = Event.objects.all()
            self.fields['event'].empty_label = '大会名'
            self.fields['stage'].queryset = Stage.objects.all()
            self.fields['stage'].empty_label = 'ラウンド'
            self.fields['division'].queryset = Division.objects.all()
            self.fields['division'].empty_label = '区分'
