from django.urls import path

from . import views

app_name = 'logmaneapp'
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('athlete/', views.AthleteListView.as_view(), name='athlete_list'),
    path('athlete/<int:pk>/', views.AthleteDetailView.as_view(), name='athlete_detail'),
    path('athlete/create/', views.athlete_form, name='athlete_create'),
    path('athlete/records/', views.athlete_records_form, name='athlete_records'),
    path('athlete/<int:pk>/delete/', views.AthleteDelete.as_view(), name='athlete_delete'),
    path('athlete/<int:pk>/update/', views.AthleteUpdate.as_view(), name='athlete_update'),
    path('athlete/<int:pk>/records/delete/', views.AthleteRecordsDelete.as_view(), name='athlete_records_delete'),
    path('athlete/<int:pk>/records/update/', views.AthleteRecordsUpdate.as_view(), name='athlete_records_update'),
    path('event/create/', views.event_form, name='event_create'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
]
