from django.urls import path

from . import views

app_name = 'logmaneapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('athlete/', views.AthleteListView.as_view(), name='athlete_list'),
    path('athlete/<int:pk>/', views.AthleteDetailView.as_view(), name='athlete_detail'),
    path('athlete/create/', views.athlete_form, name='athlete_create'),
    path('athlete/records/', views.athlete_records_form, name='athlete_records'),
    path('athlete/<int:pk>/delete/', views.AthleteDelete.as_view(), name='athlete_delete'),
    path('athlete/<int:pk>/update/', views.AthleteUpdate.as_view(), name='athlete_update'),
    path('athlete/records/<int:pk>/delete/', views.AthleteRecordsDelete.as_view(), name='athlete_records_delete'),
    path('athlete/records/<int:pk>/update/', views.AthleteRecordsUpdate.as_view(), name='athlete_records_update'),
    path('event/create/', views.event_form, name='event_create'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
    path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event_update'),
    path('event/', views.EventListView.as_view(), name='event_list'),
    path('event/records/', views.EventRecordsListView.as_view(), name='event_records_list'),
    path('event/records/create/', views.event_records_form, name='event_records_create'),
    path('event/records/<int:pk>/delete/', views.EventRecordsDelete.as_view(), name='event_records_delete'),
    path('event/records/<int:pk>/update/', views.EventRecordsUpdate.as_view(), name='event_records_update'),
]
