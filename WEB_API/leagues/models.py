import uuid

from django.db import models
from django.utils.text import slugify

from news.models import News
from player.models import Player
from tag.models import Tag


class League(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
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

    name = models.CharField(max_length=63, verbose_name='نام لیگ')
    year = models.CharField(max_length=31, verbose_name='سال')
    confederation = models.CharField(max_length=31, verbose_name='کنفدراسیون')
    country = models.CharField(max_length=31, blank=True, verbose_name='کشور')
    numberOfTeams = models.IntegerField(verbose_name='تعداد تیم ها')
    bestTeam = models.CharField(max_length=63, blank=True, verbose_name='بهترین تیم')
    establishedYear = models.IntegerField(verbose_name='سال تاسیس')
    website = models.URLField(verbose_name='وب سایت', blank=True)
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    image_url = models.URLField(verbose_name='آدرس تصویر لیگ')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')

    active = models.BooleanField(default=True, verbose_name='در حال برگذاری مسابقات')
    level = models.CharField(max_length=7, choices=LEVEL, verbose_name='مرحله')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True, max_length=255)
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return str(self.name) + ' ' + str(self.year)

    class Meta:
        ordering = ('-created_date_time', 'name')
        verbose_name = 'لیگ'
        verbose_name_plural = 'لیگ ها'
        unique_together = ('name', 'year',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__(), allow_unicode=True)
        super(League, self).save(*args, **kwargs)


class LeagueSliderImage(models.Model):
    title = models.CharField(max_length=127, verbose_name='عنوان')
    image_url = models.URLField(verbose_name='آدرس تصویر')
    league = models.ForeignKey(League, verbose_name='لیگ', on_delete=models.CASCADE)

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title + (self.league.__str__())

    class Meta:
        verbose_name = 'تصویر اسلایدر لیگ'
        ordering = ('-created_date_time', 'title')
        verbose_name_plural = 'تصاویر اسلایدر لیگ'


class BestPlayer(models.Model):
    player = models.ForeignKey(Player, verbose_name='بازیکن', on_delete=models.CASCADE)
    league = models.ForeignKey(League, verbose_name='لیگ', on_delete=models.CASCADE)
    title = models.CharField(max_length=31, verbose_name='عنوان')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} {} ({})".format(self.player.__str__(), self.league.__str__(), self.title.__str__())

    class Meta:
        verbose_name = 'برترین بازیکن'
        ordering = ('-created_date_time', 'player')
        verbose_name_plural = 'برترین بازیکنان'
