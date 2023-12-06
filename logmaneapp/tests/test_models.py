from django.test import TestCase

from logmaneapp.models import Athlete, Athlete_records, Event_records

class AthleteModelTests(TestCase):

    def test_is_empty(self):
        '''データベースが空かどうかをテストする'''
        athlete = Athlete.objects.all()
        self.assertEqual(athlete.count(), 0)

    def test_is_count_one(self):
        '''データベースにデータが一つあるかどうかをテストする'''
        athlete = Athlete(
            name='test',
            gender='test',
            grade='test',
            group='test')
        athlete.save()
        athlete = Athlete.objects.all()
        self.assertEqual(athlete.count(), 1)

    def test_save_and_retrieving_athete(self):
        '''データベースにデータを保存し、取得するテスト'''
        athlete = Athlete()
        name='test'
        gender='gender'
        grade='grade'
        group='group'

