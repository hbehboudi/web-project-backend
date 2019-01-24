import uuid

from django.db import models


class SliderImage(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
        ('OTH', 'Other'),
    )

    title = models.CharField(max_length=128)
    created_date_time = models.DateTimeField()
    image_url = models.URLField(null=False, blank=True)
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تصویر اسلایدر اصلی'
        verbose_name_plural = 'تصاویر اسلایدر اصلی'
        ordering = ('-created_date_time', 'title')
