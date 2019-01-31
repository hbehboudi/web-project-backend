from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify

from leagues.models import League
from news.models import Tag
from player.models import Player
from team.models import Team


class Game(models.Model):
    FIELDS = (
        ('FTB', 'فوتبال'),
        ('BSK', 'بسکتبال'),
    )

    STATE = (
        ('W', 'برنده'),
        ('D', 'تساوی'),
        ('L', 'بازنده'),
    )

    LEVEL = (
        ('1', 'هفته اول'),
        ('2', 'هفته دوم'),
        ('3', 'هفته سوم'),
        ('4', 'هفته چهارم'),
        ('5', 'هفته پنجم'),
        ('6', 'هفته ششم'),
        ('7', 'هفته هفتم'),
        ('8', 'هفته هشتم'),
        ('9', 'هفته نهم'),
        ('10', 'هفته دهم'),
        ('11', 'هفته یازدهم'),
        ('12', 'هفته دوازدهم'),
        ('13', 'هفته سیزدهم'),
        ('14', 'هفته چهاردهم'),
        ('15', 'هفته پانزدهم'),
        ('16', 'هفته شانزدهم'),
        ('17', 'هفته هفدهم'),
        ('18', 'هفته هجدهم'),
        ('19', 'هفته نوزدهم'),
        ('20', 'هفته بیستم'),
        ('21', 'هفته بیست و یکم'),
        ('22', 'هفته بیست و دوم'),
        ('23', 'هفته بیست و سوم'),
        ('24', 'هفته بیست و چهارم'),
        ('25', 'هفته بیست و پنجم'),
        ('26', 'هفته بیست و ششم'),
        ('27', 'هفته بیست و هفتم'),
        ('28', 'هفته بیست و هشتم'),
        ('29', 'هفته بیست و نهم'),
        ('30', 'هفته سی ام'),
        ('1/16', 'یک شانزدهم'),
        ('1/8', 'یک هشتم'),
        ('1/4', 'یک چهارم'),
        ('1/2', 'نیمه نهایی'),
        ('F', 'فینال'),
        ('R', 'رده بندی'),
    )

    team1 = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم۱', related_name='host')
    team2 = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم۲', related_name='guest')
    league = models.ForeignKey(League, on_delete=CASCADE, verbose_name='لیگ')
    level = models.CharField(max_length=7, choices=LEVEL, verbose_name='مرحله')

    team_state1 = models.CharField(max_length=1, choices=STATE, blank=True, verbose_name='نتیجه بازی ۱')
    team_state2 = models.CharField(max_length=1, choices=STATE, blank=True, verbose_name='نتیجه بازی ۲')
    goals1 = models.IntegerField(blank=True, verbose_name='گل های تیم ۱',
                                 help_text='در صورتی که بازی مورد نظر فوتبال است.')
    goals2 = models.IntegerField(blank=True, verbose_name='گل های تیم ۲',
                                 help_text='در صورتی که بازی مورد نظر فوتبال است.')
    shots1 = models.IntegerField(blank=True, verbose_name='شوت های تیم ۱',
                                 help_text='در صورتی که بازی مورد نظر فوتبال است.')
    shots2 = models.IntegerField(blank=True, verbose_name='شوت های تیم ۲',
                                 help_text='در صورتی که بازی مورد نظر فوتبال است.')
    shots_on_target1 = models.IntegerField(blank=True, verbose_name='شوت های داخل چارچوب تیم ۱',
                                           help_text='در صورتی که بازی مورد نظر فوتبال است.')
    shots_on_target2 = models.IntegerField(blank=True, verbose_name='شوت های داخل چارچوب تیم ۲',
                                           help_text='در صورتی که بازی مورد نظر فوتبال است.')
    possession1 = models.IntegerField(blank=True, verbose_name='مالکیت توپ تیم ۱',
                                      help_text='در صورتی که بازی مورد نظر فوتبال است.')
    possession2 = models.IntegerField(blank=True, verbose_name='مالکیت توپ تیم ۲',
                                      help_text='در صورتی که بازی مورد نظر فوتبال است.')
    passes1 = models.IntegerField(blank=True, verbose_name='پاس های تیم ۱',
                                  help_text='در صورتی که بازی مورد نظر فوتبال است.')
    passes2 = models.IntegerField(blank=True, verbose_name='پاس های تیم ۲',
                                  help_text='در صورتی که بازی مورد نظر فوتبال است.')
    yellow_cards1 = models.IntegerField(blank=True, verbose_name='کارت زرد های تیم ۱',
                                        help_text='در صورتی که بازی مورد نظر فوتبال است.')
    yellow_cards2 = models.IntegerField(blank=True, verbose_name='کارت زرد های تیم ۲',
                                        help_text='در صورتی که بازی مورد نظر فوتبال است.')
    red_cards1 = models.IntegerField(blank=True, verbose_name='کارت قرمز های تیم ۱',
                                     help_text='در صورتی که بازی مورد نظر فوتبال است.')
    red_cards2 = models.IntegerField(blank=True, verbose_name='کارت قرمز های تیم ۲',
                                     help_text='در صورتی که بازی مورد نظر فوتبال است.')
    offsides1 = models.IntegerField(blank=True, verbose_name='آفساید های تیم ۱',
                                    help_text='در صورتی که بازی مورد نظر فوتبال است.')
    offsides2 = models.IntegerField(blank=True, verbose_name='آفساید های تیم ۲',
                                    help_text='در صورتی که بازی مورد نظر فوتبال است.')
    corners1 = models.IntegerField(blank=True, verbose_name='کرنر های تیم ۱',
                                   help_text='در صورتی که بازی مورد نظر فوتبال است.')
    corners2 = models.IntegerField(blank=True, verbose_name='کرنر های تیم ۲',
                                   help_text='در صورتی که بازی مورد نظر فوتبال است.')
    
    fouls1 = models.IntegerField(blank=True, verbose_name='خطا های تیم۱')
    fouls2 = models.IntegerField(blank=True, verbose_name='خطا های تیم۱')
    game_date = models.DateTimeField(verbose_name='تاریخ و ساعت بازی')
    full_time = models.BooleanField(default=False, verbose_name='بازی انجام شده')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True, max_length=255)
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{}-{} ({})_{}".format(self.team1, self.team2, self.league, self.game_date)

    class Meta:
        ordering = ('-game_date', 'team1', 'team2', 'league')
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
    penalty = models.BooleanField(default=False, verbose_name='پنالتی')
    own_goal = models.BooleanField(default=False, verbose_name='گل به خودی')

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
    goal = models.OneToOneField(Goal, on_delete=CASCADE, verbose_name='گل')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} {}".format(self.player, self.goal)

    class Meta:
        ordering = ('-created_date_time', 'goal',)
        verbose_name = 'پاس گل'
        verbose_name_plural = 'پاس های گل'


class Substitute(models.Model):
    in_player = models.ForeignKey(Player, on_delete=CASCADE, related_name='in_player', verbose_name='بازیکن وارد شده')
    out_player = models.ForeignKey(Player, on_delete=CASCADE, related_name='out_player', verbose_name='بازیکن خارج شده')
    game = models.ForeignKey(Game, on_delete=CASCADE, verbose_name='بازی')
    team = models.ForeignKey(Team, on_delete=CASCADE, verbose_name='تیم')

    minute = models.IntegerField(verbose_name='دقیقه')
    second = models.IntegerField(verbose_name='ثانیه')
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} {} ({})".format(self.in_player, self.out_player, self.game)

    class Meta:
        verbose_name = 'تعویض'
        verbose_name_plural = 'تعویض'
        ordering = ('-created_date_time', 'game',)
