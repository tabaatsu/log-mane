from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Athlete, Discipline, Athlete_records, Event, Event_records
from .forms import AthleteForm


class IndexView(TemplateView):
    template_name = 'index.html'

class AthleteListView(ListView):
    template_name = 'athlete_list.html'
    model = Athlete

class AthleteDetailView(DetailView):
    template_name = 'athlete_detail.html'
    model = Athlete

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['athlete_records'] = Athlete_records.objects.filter(athlete_id=self.kwargs['pk'])
        context['event_records'] = Event_records.objects.filter(athlete_id=self.kwargs['pk'])
        return context
    
    athlete = Athlete.objects.all()

def athleteForm(request):
    if request.method == 'POST':
        form = AthleteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logmaneapp:athlete_list')
    else:
        form = AthleteForm()
    context = {'form': form}
    return render(request, 'athlete_create.html', context)
