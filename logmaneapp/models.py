from django.db import models

class Athlete(models.Model):
    class Meta:
        db_table = 'athlete'

    athlete_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, verbose_name='選手名')
    gender = models.CharField(max_length=10, verbose_name='性別')
    grade = models.CharField(max_length=10, verbose_name='学年')
    group = models.CharField(max_length=10, verbose_name='パート', null=True)

    def __str__(self):
        return self.name


class Discipline(models.Model):
    class Meta:
        db_table = 'discipline'

    discipline_id = models.AutoField(primary_key=True, unique=True)
    discipline = models.CharField(max_length=100, verbose_name='種目')

    def __str__(self):
        return self.discipline


class Athlete_records(models.Model):

    athlete_id = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)
    personal_best = models.DecimalField(verbose_name='自己ベスト', max_digits=10, decimal_places=2)
    university_best = models.DecimalField(verbose_name='大学ベスト', max_digits=10, decimal_places=2)
    valid_record = models.DecimalField(verbose_name='有効記録', max_digits=10, decimal_places=2)
    athlete_records_id = models.AutoField(primary_key=True, unique=True)

    class Meta:
        db_table = 'athlete_records'
        constraints = [
            models.UniqueConstraint(fields=['athlete_id', 'discipline'], name='athlete_records_unique')
        ]

    def __str__(self):
        return str(self.athlete_records_id)


class Event(models.Model):
    class Meta:
        db_table = 'event'

    event_id = models.AutoField(primary_key=True, unique=True)
    event = models.CharField(max_length=100, verbose_name='大会名')
    date = models.DateField(verbose_name='日付')

    def __str__(self):
        return self.event


class Stage(models.Model):
    class Meta:
        db_table = 'stage'

    stage_id = models.AutoField(primary_key=True, unique=True)
    stage = models.CharField(max_length=100, verbose_name='ラウンド')

    def __str__(self):
        return self.stage


class Division(models.Model):
    class Meta:
        db_table = 'division'

    division_id = models.AutoField(primary_key=True, unique=True)
    division = models.CharField(max_length=100, verbose_name='区分')

    def __str__(self):
        return self.division


class Event_records(models.Model):


    athlete_id = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)
    stage = models.ForeignKey(Stage, on_delete=models.PROTECT)
    record = models.DecimalField(verbose_name='記録', max_digits=10, decimal_places=2)
    wind = models.DecimalField(verbose_name='風速', max_digits=2, decimal_places=1)
    heat = models.CharField(max_length=10, verbose_name='組')
    place = models.CharField(max_length=100, verbose_name='順位')
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    event_records_id = models.AutoField(primary_key=True, unique=True)

    class Meta:
        db_table = 'event_records'
        constraints = [
            models.UniqueConstraint(fields=['athlete_id', 'event', 'discipline', 'stage'], name='event_records_unique')
        ]

    def __str__(self):
        return str(self.athlete_id.athlete_id)
