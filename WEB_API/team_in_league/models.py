from django.db import models

from leagues.models import League
from team.models import Team


class TeamLeague(models.Model):
    team = models.ForeignKey(Team, on_delete=True, verbose_name='تیم')
    league = models.ForeignKey(League, on_delete=True, verbose_name='لیگ')
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')
    active = models.BooleanField(default=False, verbose_name='در حال برگزاری مسابقات')

    def __str__(self):
        return "{} ({})".format(str(self.team), self.league)

    class Meta:
        ordering = ('-created_date_time', 'team', 'league')
        verbose_name = 'حضور تیم در لیگ'
        verbose_name_plural = 'حضور تیم ها در لیگ ها'
