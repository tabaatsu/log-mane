from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Athlete, Discipline, Athlete_records, Event


class IndexView(TemplateView):
    template_name = 'index.html'

class AthleteListView(ListView):
    template_name = 'athlete_list.html'
    model = Athlete
