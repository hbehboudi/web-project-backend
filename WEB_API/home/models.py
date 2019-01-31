from django.db import models


class SliderImage(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
    )

    title = models.CharField(max_length=127, verbose_name='عنوان')
    image_url = models.URLField(verbose_name='آدرس تصویر')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    field = models.CharField(max_length=3, choices=FIELDS, default='FTB', verbose_name='ورزش')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return "{} ({})".format(self.title, self.image_url)

    class Meta:
        verbose_name = 'تصویر اسلایدر اصلی'
        verbose_name_plural = 'تصاویر اسلایدر اصلی'
        ordering = ('-created_date_time', 'title')
