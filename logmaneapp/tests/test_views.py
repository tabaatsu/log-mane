from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from logmaneapp.models import Athlete, Athlete_records, Event_records


class LoggedInTestCase(TestCase):
    '''各テストクラスで共通の事前準備処理をオーバーライド'''

    def setUp(self) -> None:
        '''テストメソッド実行前の事前設定'''
        #テストユーザーの作成
        self.password = 'testpass1234'
        self.test_user = get_user_model().objects.create_user(
            username='test_user',
            email='test@email.com',
            password=self.password
        )
        #テストユーザーでログインする
        self.client.login(username=self.test_user.username, email=self.test_user.email, password=self.password)

class IndexTests(LoggedInTestCase):

    def test_index_view_status_code(self):
        '''indexページへのアクセスが成功するかどうかをテストする'''
        url = reverse('logmaneapp:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class AthleteListViewTests(LoggedInTestCase):
    '''athlete_listページのテストクラス'''

    def test_athlete_list_view_status_code(self):
        '''athlete_listページへのアクセスが成功するかどうかをテストする'''
        url = reverse('logmaneapp:athlete_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
