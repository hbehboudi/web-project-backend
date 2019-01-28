from django.db import models
from django.utils.text import slugify

from news.models import Tag


class PlayerPost(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
        ('OTH', 'Other'),
    )

    name = models.CharField(max_length=127, unique=True, verbose_name='نام')
    short_name = models.CharField(max_length=3, verbose_name='نام مخفف')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} ({})".format(self.name, self.short_name)

    class Meta:
        ordering = ('name', 'short_name')
        verbose_name = 'پست بازیکن'
        verbose_name_plural = 'پست های بازیکنان'


class Player(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
    )

    name = models.CharField(max_length=127, unique=True, verbose_name='نام')
    post = models.ForeignKey(PlayerPost, on_delete=models.CASCADE, verbose_name='پست')
    nationality = models.CharField(max_length=31, verbose_name='ملیت')
    team = models.CharField(max_length=63, verbose_name='باشگاه')
    city = models.CharField(max_length=31, verbose_name='محل تولد')
    age = models.IntegerField(verbose_name='سن')
    height = models.FloatField(verbose_name='قد')
    weight = models.IntegerField(verbose_name='وزن')
    teamNum = models.IntegerField(verbose_name='شماره پیراهن در باشگاه', blank=True)
    nationalityTeamNum = models.IntegerField(verbose_name='شماره پیراهن در تیم ملی', blank=True)
    website = models.URLField(verbose_name='وب سایت', blank=True)
    image_url = models.URLField(verbose_name='آدرس تصویر بازیکن')
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True, max_length=255)

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_date_time', 'name')
        verbose_name = 'بازیکن'
        verbose_name_plural = 'بازیکنان'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__(), allow_unicode=True)
        super(Player, self).save(*args, **kwargs)


class PlayerSliderImage(models.Model):
    title = models.CharField(max_length=127, verbose_name='عنوان')
    image_url = models.URLField(verbose_name='آدرس تصویر')
    player = models.ForeignKey(Player, verbose_name='تیم', on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر اسلایدر بازیکن'
        ordering = ('-created_date_time', 'title')
        verbose_name_plural = 'تصاویر اسلایدر بازیکن'
