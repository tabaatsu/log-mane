from django.contrib import admin

from .models import Athlete, Discipline, Athlete_records, Event, Event_records, Stage, Division

admin.site.register(Athlete)
admin.site.register(Discipline)
admin.site.register(Athlete_records)
admin.site.register(Event_records)
admin.site.register(Event)
admin.site.register(Stage)
admin.site.register(Division)
