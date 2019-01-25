from django.db import models
from django.utils.text import slugify

from tag.models import Tag


class News(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
        ('OTH', 'Other'),
    )

    title = models.CharField(unique=True, max_length=127, verbose_name='عنوان')
    summary = models.CharField(max_length=255, blank=True, verbose_name='خلاصه خبر')
    text = models.TextField(blank=True, verbose_name='متن خبر')
    category = models.CharField(max_length=31, verbose_name='نوع خبر')
    image_url = models.URLField(verbose_name='آدرس تصویر')
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH', verbose_name='ورزش')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='تگ ها')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True, max_length=255)
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'
        ordering = ('-created_date_time', 'title',)
        unique_together = ('title',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__(), allow_unicode=True)
        super(News, self).save(*args, **kwargs)
