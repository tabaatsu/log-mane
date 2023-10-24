from django.urls import path

from . import views

app_name = 'logmaneapp'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('athlete/', views.AthleteListView.as_view(), name='athlete_list'),
]
