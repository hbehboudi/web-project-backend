import uuid

from django.db import models
from django.utils.text import slugify

from news.models import News
from tag.models import Tag


class League(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
    )

    name = models.CharField(max_length=63, verbose_name='نام لیگ')
    year = models.IntegerField(verbose_name='سال')
    confederation = models.CharField(max_length=31, verbose_name='کنفدراسیون')
    country = models.CharField(max_length=31, blank=True, verbose_name='کشور', help_text='الزامی نیست.')
    level = models.IntegerField(blank=True, verbose_name='دسته')
    numberOfTeams = models.IntegerField(verbose_name='تعداد تیم ها')
    bestTeam = models.CharField(max_length=63, blank=True, verbose_name='بهترین تیم')
    establishedYear = models.IntegerField(verbose_name='سال تاسیس')
    website = models.URLField(verbose_name='وب سایت', blank=True)
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    image_url = models.URLField(verbose_name='آدرس تصویر لیگ')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    slug = models.SlugField(unique=True, blank=True)
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
