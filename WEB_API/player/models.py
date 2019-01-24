import uuid

from django.db import models

from news.models import Tag


class Player(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
    )
    POSITIONS = (
        ('GK', 'Goalkeeper'),
        ('CB', 'Center fullback'),
        ('SW', 'Sweeper'),
        ('LFB', 'Left fullback'),
        ('RFB', 'Right fullback'),
        ('WB', 'Wingback'),
        ('LM', 'Left midfield'),
        ('RM', 'Right midfield'),
        ('DM', 'Defensive midfield'),
        ('CM', 'Center midfield'),
        ('WM', 'Wide midfield'),
        ('CF', 'Center forward'),
        ('AM', 'Attacking midfield'),
        ('S', 'Striker'),
        ('SS', 'Second striker'),
        ('LW', 'Left winger'),
        ('RW', 'Right winger'),
    )

    name = models.CharField(max_length=64, verbose_name='نام')
    nickname = models.CharField(max_length=64, verbose_name='لقب')
    post = models.CharField(choices=POSITIONS, max_length=3, verbose_name='پست')
    nationality = models.CharField(max_length=64, verbose_name='ملیت')
    team = models.CharField(max_length=64, verbose_name='باشگاه')
    city = models.CharField(max_length=64, verbose_name='محل تولد')
    age = models.IntegerField(verbose_name='سن')
    height = models.FloatField(verbose_name='قد')
    weight = models.IntegerField(verbose_name='وزن')
    teamNum = models.IntegerField(verbose_name='شماره پیراهن در باشگاه')
    nationalityTeamNum = models.IntegerField(verbose_name='شماره پیراهن در تیم ملی')
    website = models.URLField(verbose_name='وب سایت')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    image_url = models.URLField(null=False, blank=True, verbose_name='آدرس تصویر لیگ')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    url = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False, auto_created=True)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_date_time', 'name')
        verbose_name = 'بازیکن'
        verbose_name_plural = 'بازیکنان'


class PlayerSliderImage(models.Model):
    title = models.CharField(max_length=128, verbose_name='عنوان')
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    image_url = models.URLField(null=False, blank=True, verbose_name='آدرس تصویر')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')
    player = models.ForeignKey(Player, verbose_name='تیم', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر اسلایدر بازیکن'
        ordering = ('-created_date_time', 'title')
        verbose_name_plural = 'تصاویر اسلایدر بازیکن'
