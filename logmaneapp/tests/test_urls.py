from django.test import TestCase
from django.urls import reverse, resolve
from logmaneapp.views import *

class TestUrls(TestCase):
    ''' indexのクラスが呼び出せているかテスト '''
    def test_index_url(self):
        url = reverse('logmaneapp:index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    ''' athlete一覧ページへのリダイレクトをテスト'''
    def test_athlete_list_url(self):
        url = reverse('logmaneapp:athlete_list')
        self.assertEqual(resolve(url).func.view_class, AthleteListView)

    ''' athlete詳細ページへのリダイレクトをテスト'''
    def test_athlete_detail_url(self):
        url = reverse('logmaneapp:athlete_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, AthleteDetailView)

    ''' athlete作成ページへのリダイレクトをテスト'''
    def test_athlete_create_url(self):
        url = reverse('logmaneapp:athlete_create')
        self.assertEqual(resolve(url).func, athlete_form)

    ''' athlete削除ページへのリダイレクトをテスト'''
    def test_athlete_delete_url(self):
        url = reverse('logmaneapp:athlete_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, AthleteDelete)

    ''' athlete更新ページへのリダイレクトをテスト'''
    def test_athlete_update_url(self):
        url = reverse('logmaneapp:athlete_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, AthleteUpdate)

    ''' athlete_records作成ページへのリダイレクトをテスト'''
    def test_athlete_records_url(self):
        url = reverse('logmaneapp:athlete_records')
        self.assertEqual(resolve(url).func, athlete_records_form)


    ''' athlete_records削除ページへのリダイレクトをテスト'''
    def test_athlete_records_delete_url(self):
        url = reverse('logmaneapp:athlete_records_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, AthleteRecordsDelete)

    ''' athlete_records更新ページへのリダイレクトをテスト'''
    def test_athlete_records_update_url(self):
        url = reverse('logmaneapp:athlete_records_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, AthleteRecordsUpdate)

    ''' event作成ページへのリダイレクトをテスト'''
    def test_event_create_url(self):
        url = reverse('logmaneapp:event_create')
        self.assertEqual(resolve(url).func, event_form)

    ''' event削除ページへのリダイレクトをテスト'''
    def test_event_delete_url(self):
        url = reverse('logmaneapp:event_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, EventDelete)

    ''' event更新ページへのリダイレクトをテスト'''
    def test_event_update_url(self):
        url = reverse('logmaneapp:event_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, EventUpdate)

    ''' event一覧ページへのリダイレクトをテスト'''
    def test_event_list_url(self):
        url = reverse('logmaneapp:event_list')
        self.assertEqual(resolve(url).func.view_class, EventListView)

    ''' event_records一覧ページへのリダイレクトをテスト'''
    def test_event_records_list_url(self):
        url = reverse('logmaneapp:event_records_list')
        self.assertEqual(resolve(url).func.view_class, EventRecordsListView)

    ''' event_records作成ページへのリダイレクトをテスト'''
    def test_event_records_create_url(self):
        url = reverse('logmaneapp:event_records_create')
        self.assertEqual(resolve(url).func, event_records_form)

    ''' event_records削除ページへのリダイレクトをテスト'''
    def test_event_records_delete_url(self):
        url = reverse('logmaneapp:event_records_delete', args=[1])
        self.assertEqual(resolve(url).func.view_class, EventRecordsDelete)

    ''' event_records更新ページへのリダイレクトをテスト'''
    def test_event_records_update_url(self):
        url = reverse('logmaneapp:event_records_update', args=[1])
        self.assertEqual(resolve(url).func.view_class, EventRecordsUpdate)
