import uuid

from django.db import models


class Tag(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
        ('OTH', 'Other'),
    )

    title = models.CharField(max_length=63, verbose_name='نام تگ')
    text = models.TextField(blank=True, verbose_name='درباره ی تگ')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'
        ordering = ('-created_date_time', 'title')
