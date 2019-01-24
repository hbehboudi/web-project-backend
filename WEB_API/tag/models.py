import uuid

from django.db import models


class Tag(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
        ('OTH', 'Other'),
    )

    name = models.CharField(primary_key=True, max_length=32, verbose_name='نام تگ', default='')
    text = models.TextField(verbose_name='درباره ی تگ', null=True, blank=True)
    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تگ'
        ordering = ('-created_date_time', 'name')
