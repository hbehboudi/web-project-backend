from django.db import models

from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify

from leagues.models import League
from news.models import Tag
from player.models import Player
from team.models import Team


class Game(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
    )

    team1 = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم۱', related_name='host')
    team2 = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم۲', related_name='guest')
    league = models.ForeignKey(League, on_delete=CASCADE, verbose_name='لیگ')

    goals1 = models.IntegerField(verbose_name='گل های تیم ۱')
    goals2 = models.IntegerField(verbose_name='گل های تیم ۲')
    shots1 = models.IntegerField(verbose_name='شوت های تیم ۱')
    shots2 = models.IntegerField(verbose_name='شوت های تیم ۲')
    shots_on_target1 = models.IntegerField(verbose_name='شوت های داخل چارچوب تیم ۱')
    shots_on_target2 = models.IntegerField(verbose_name='شوت های داخل چارچوب تیم ۲')
    possession1 = models.IntegerField(verbose_name='مالکیت توپ تیم ۱')
    possession2 = models.IntegerField(verbose_name='مالکیت توپ تیم ۲')
    passes1 = models.IntegerField(verbose_name='پاس های تیم ۱')
    passes2 = models.IntegerField(verbose_name='پاس های تیم ۲')
    fouls1 = models.IntegerField(verbose_name='خطا های تیم۱')
    fouls2 = models.IntegerField(verbose_name='خطا های تیم۱')
    yellow_cards1 = models.IntegerField(verbose_name='کارت زرد های تیم ۱')
    yellow_cards2 = models.IntegerField(verbose_name='کارت زرد های تیم ۲')
    red_cards1 = models.IntegerField(verbose_name='کارت قرمز های تیم ۱')
    red_cards2 = models.IntegerField(verbose_name='کارت قرمز های تیم ۲')
    offsides1 = models.IntegerField(verbose_name='آفساید های تیم ۱')
    offsides2 = models.IntegerField(verbose_name='آفساید های تیم ۲')
    corners1 = models.IntegerField(verbose_name='کرنر های تیم ۱')
    corners2 = models.IntegerField(verbose_name='کرنر های تیم ۲')
    game_date = models.DateTimeField(verbose_name='تاریخ و ساعت بازی')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True, max_length=255)
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{}-{} ({})_{}".format(self.team1, self.team2, self.league, self.game_date)

    class Meta:
        ordering = ('-created_date_time', 'team1', 'team2', 'league')
        verbose_name = 'بازی'
        verbose_name_plural = 'بازی ها'
        unique_together = ('team1', 'team2', 'league', 'game_date')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__(), allow_unicode=True)
        super(Game, self).save(*args, **kwargs)


class GameSliderImage(models.Model):
    title = models.CharField(max_length=127, verbose_name='عنوان')
    image_url = models.URLField(null=False, verbose_name='آدرس تصویر')
    game = models.ForeignKey(Game, verbose_name='بازی', on_delete=models.CASCADE)

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر اسلایدر بازی'
        ordering = ('-created_date_time', 'title')
        verbose_name_plural = 'تصاویر اسلایدر بازی ها'


class GameReport(models.Model):
    title = models.CharField(unique=True, max_length=127, verbose_name='عنوان')
    image_url = models.URLField(verbose_name='آدرس تصویر')
    game = models.ForeignKey(Game, on_delete=CASCADE, verbose_name='بازی')
    minute = models.IntegerField(verbose_name='دقیقه')
    second = models.IntegerField(verbose_name='ثانیه')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{}({})".format(self.title, self.game)

    class Meta:
        verbose_name = 'گزارش بازی‌'
        verbose_name_plural = 'گزارشات بازی'
        ordering = ('-created_date_time', 'title',)
        unique_together = ('title', 'game')


class Goal(models.Model):
    player = models.ForeignKey(Player, on_delete=CASCADE, verbose_name='بازیکن')
    game = models.ForeignKey(Game, on_delete=CASCADE, verbose_name='بازی')
    scoring_team = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم گل زده', related_name='scoring_team')
    receiving_team = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم گل خورده',
                                       related_name='receiving_team')
    minute = models.IntegerField(verbose_name='دقیقه')
    second = models.IntegerField(verbose_name='ثانیه')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} {}".format(self.player, self.game)

    class Meta:
        verbose_name = 'گل'
        verbose_name_plural = 'گل ها'
        ordering = ('-created_date_time', 'game',)


class PenaltyGoal(models.Model):
    player = models.ForeignKey(Player, on_delete=CASCADE, verbose_name='بازیکن')
    game = models.ForeignKey(Game, on_delete=CASCADE, verbose_name='بازی')
    scoring_team = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم گل زده',
                                     related_name='penalty_scoring_team')
    receiving_team = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم گل خورده',
                                       related_name='penalty_receiving_team')
    minute = models.IntegerField(verbose_name='دقیقه')
    second = models.IntegerField(verbose_name='ثانیه')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} {}".format(self.player, self.game)

    class Meta:
        verbose_name = 'گل پنالتی'
        verbose_name_plural = 'گل های پنالتی'
        ordering = ('-created_date_time', 'game',)


class YellowCard(models.Model):
    player = models.ForeignKey(Player, on_delete=CASCADE, verbose_name='بازیکن')
    game = models.ForeignKey(Game, on_delete=CASCADE, verbose_name='بازی')
    team = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم')
    minute = models.IntegerField(verbose_name='دقیقه')
    second = models.IntegerField(verbose_name='ثانیه')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} {}".format(self.player, self.game)

    class Meta:
        verbose_name = 'کارت زرد‌'
        verbose_name_plural = 'کارت های زرد'
        ordering = ('-created_date_time', 'game',)


class RedCard(models.Model):
    player = models.ForeignKey(Player, on_delete=CASCADE, verbose_name='بازیکن')
    game = models.ForeignKey(Game, on_delete=CASCADE, verbose_name='بازی')
    team = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم')
    minute = models.IntegerField(verbose_name='دقیقه')
    second = models.IntegerField(verbose_name='ثانیه')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} {}".format(self.player, self.game)

    class Meta:
        verbose_name = 'کارت قرمز'
        verbose_name_plural = 'کارت های قرمز'
        ordering = ('-created_date_time', 'game',)


class AssistGoal(models.Model):
    player = models.ForeignKey(Player, on_delete=CASCADE, verbose_name='بازیکن')
    goal = models.ForeignKey(Goal, unique=True, on_delete=CASCADE, verbose_name='گل')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} {}".format(self.player, self.goal)

    class Meta:
        ordering = ('-created_date_time', 'goal',)
        verbose_name = 'پاس گل'
        verbose_name_plural = 'پاس های گل'
