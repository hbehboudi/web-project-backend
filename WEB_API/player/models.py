from django.db import models
from django.utils.text import slugify

from authentication.accounts.models import User
from news.models import Tag


class PlayerPost(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
    )

    name = models.CharField(max_length=127, unique=True, verbose_name='نام')
    short_name = models.CharField(max_length=3, verbose_name='نام مخفف')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    field = models.CharField(max_length=3, choices=FIELDS, default='FTB', verbose_name='ورزش')
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
    birth_place = models.CharField(max_length=31, verbose_name='محل تولد')
    team = models.CharField(max_length=63, verbose_name='باشگاه', blank=True)
    age = models.IntegerField(verbose_name='سن', blank=True, null=True)
    height = models.IntegerField(verbose_name='قد', blank=True, null=True)
    weight = models.IntegerField(verbose_name='وزن', blank=True, null=True)
    teamNum = models.IntegerField(verbose_name='شماره پیراهن در باشگاه', blank=True, null=True)
    nationalityTeamNum = models.IntegerField(verbose_name='شماره پیراهن در تیم ملی', blank=True, null=True)
    website = models.URLField(verbose_name='وب سایت', blank=True)
    image_url = models.URLField(verbose_name='آدرس تصویر بازیکن')
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True, max_length=255)

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    field = models.CharField(max_length=3, choices=FIELDS, default='FTB', verbose_name='ورزش')
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
    player = models.ForeignKey(Player, verbose_name='بازیکن', on_delete=models.CASCADE)
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر اسلایدر بازیکن'
        ordering = ('-created_date_time', 'title')
        verbose_name_plural = 'تصاویر اسلایدر بازیکن'


class LikePlayer(models.Model):
    user = models.ForeignKey(User, verbose_name='کاربر', on_delete=models.CASCADE)
    player = models.ForeignKey(Player, verbose_name='بازیکن', on_delete=models.CASCADE)

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} {}".format(self.player, self.user)

    class Meta:
        verbose_name = 'علاقه مندی'
        unique_together = ('user', 'player',)
        ordering = ('-created_date_time', 'player')
        verbose_name_plural = 'علاقه مندی ها'
