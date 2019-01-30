from django.db import models
from django.db.models import CASCADE

from game.models import Game
from leagues.models import League
from player.models import Player
from team.models import Team


class TeamLeague(models.Model):
    team = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم')
    league = models.ForeignKey(League, on_delete=CASCADE, verbose_name='لیگ')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')
    result = models.CharField(max_length=31, blank=True, verbose_name='نتیجه')

    def __str__(self):
        return "{} ({})".format(str(self.team), self.league)

    class Meta:
        ordering = ('-created_date_time', 'team', 'league')
        verbose_name = 'حضور تیم در لیگ'
        verbose_name_plural = 'حضور تیم ها در لیگ ها'


class PlayerTeam(models.Model):
    player = models.ForeignKey(Player, on_delete=CASCADE, verbose_name='بازیکن')
    teamLeague = models.ForeignKey(TeamLeague, on_delete=CASCADE, verbose_name='تیم در لیگ')
    num = models.IntegerField(verbose_name='شماره پیراهن')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} ({})".format(self.player, self.teamLeague.__str__())

    class Meta:
        ordering = ('-created_date_time', 'player',)
        verbose_name = 'حضور بازیکن در تیم'
        verbose_name_plural = 'حضور بازیکن ها در تیم ها'


class PlayerGame(models.Model):
    player = models.ForeignKey(Player, on_delete=CASCADE, verbose_name='بازیکن')
    game = models.ForeignKey(Game, on_delete=CASCADE, verbose_name='بازی')
    team = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم')
    fix = models.BooleanField(default=True, verbose_name='بازیکن ثابت')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} ({})".format(self.player.__str__(), self.game.__str__())

    class Meta:
        ordering = ('-created_date_time', 'player',)
        verbose_name = 'حضور بازیکن در بازی'
        verbose_name_plural = 'حضور بازیکن ها در بازی ها'
