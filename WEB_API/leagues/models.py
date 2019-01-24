import uuid

from django.db import models

from news.models import News
from tag.models import Tag


class League(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
    )

    name = models.CharField(max_length=64, verbose_name='نام لیگ')
    year = models.IntegerField(verbose_name='سال')
    confederation = models.CharField(max_length=32, verbose_name='کنفدراسیون')
    country = models.CharField(max_length=32, blank=True, verbose_name='کشور', help_text='اجباری نیست.')
    level = models.IntegerField(blank=True, verbose_name='دسته')
    numberOfTeams = models.IntegerField(verbose_name='تعداد تیم ها')
    bestTeam = models.CharField(max_length=32, blank=True, verbose_name='بهترین تیم')
    establishedYear = models.IntegerField(verbose_name='سال تاسیس')
    website = models.URLField(verbose_name='وب سایت')
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    image_url = models.URLField(null=False, blank=True, verbose_name='آدرس تصویر لیگ')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    url = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False, auto_created=True)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.name + str(self.year)

    class Meta:
        ordering = ('-created_date_time', 'name')
        verbose_name = 'لیگ'


class LeagueSliderImage(models.Model):
    title = models.CharField(max_length=128, verbose_name='عنوان')
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    image_url = models.URLField(null=False, blank=True, verbose_name='آدرس تصویر')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')
    league = models.ForeignKey(League, verbose_name='لیگ', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر اسلایدر لیگ'
        ordering = ('-created_date_time', 'title')
