import uuid

from django.db import models

from tag.models import Tag


class News(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
        ('OTH', 'Other'),
    )

    title = models.CharField(max_length=128, verbose_name='عنوان')
    summary = models.CharField(max_length=256, null=True, blank=True, verbose_name='خلاصه خبر')
    text = models.TextField(null=True, blank=True, verbose_name='متن خبر')
    category = models.CharField(max_length=16, null=True, verbose_name='نوع خبر')
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    image_url = models.URLField(null=False, blank=True, verbose_name='آدرس تصویر')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    url = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False, auto_created=True)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'
        ordering = ('-created_date_time', 'title')
