from django.db import models

from leagues.models import League
from player.models import Player
from team.models import Team
from team_in_league.models import TeamLeague


class PlayerTeam(models.Model):
    player = models.ForeignKey(Player, on_delete=True, verbose_name='بازیکن')
    teamLeague = models.ForeignKey(TeamLeague, on_delete=True, verbose_name='تیم در لیگ')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} ({})".format(self.player, self.teamLeague.__str__())

    class Meta:
        ordering = ('-created_date_time', 'player',)
        verbose_name = 'حضور بازیکن در تیم'
        verbose_name_plural = 'حضور بازیکن ها در تیم ها'
