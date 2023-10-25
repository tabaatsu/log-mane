from django.urls import path

from . import views

app_name = 'logmaneapp'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('athlete/', views.AthleteListView.as_view(), name='athlete_list'),
    path('athlete/<int:pk>/', views.AthleteDetailView.as_view(), name='athlete_detail'),
    path('athlete/create/', views.athleteForm, name='athlete_create'),
]
