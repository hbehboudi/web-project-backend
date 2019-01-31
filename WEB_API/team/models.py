from django.db import models
from django.utils.text import slugify

from news.models import Tag


class Team(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
    )

    name = models.CharField(max_length=63, unique=True, verbose_name='نام تیم')
    nickname = models.CharField(max_length=63, blank=True, verbose_name='لقب تیم')
    internationalRank = models.IntegerField(blank=True, verbose_name='رتبه جهانی')
    city = models.CharField(max_length=31, blank=True, verbose_name='شهر')
    country = models.CharField(max_length=31, blank=True, verbose_name='کشور')
    establishedYear = models.IntegerField(blank=True, verbose_name='سال تاسیس')
    coach = models.CharField(max_length=63, verbose_name='سرمربی')
    captain = models.CharField(max_length=63, verbose_name='کاپیتان')
    website = models.URLField(blank=True, verbose_name='وب سایت')
    image_url = models.URLField(null=False, verbose_name='آدرس تصویر تیم')
    field = models.CharField(max_length=3, choices=FIELDS, default='FTB', verbose_name='ورزش')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True, max_length=255)
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_date_time', 'name')
        verbose_name = 'تیم'
        verbose_name_plural = 'تیم ها'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__(), allow_unicode=True)
        super(Team, self).save(*args, **kwargs)


class TeamSliderImage(models.Model):
    title = models.CharField(max_length=127, verbose_name='عنوان')
    image_url = models.URLField(verbose_name='آدرس تصویر')
    team = models.ForeignKey(Team, verbose_name='تیم', on_delete=models.CASCADE)

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر اسلایدر تیم'
        ordering = ('-created_date_time', 'title')
        verbose_name_plural = 'تصاویر اسلایدر تیم ها'
