from django.db import models
from django.utils.text import slugify

from authentication.accounts.models import User
from tag.models import Tag


class NewsType(models.Model):
    title = models.CharField(max_length=63, verbose_name='عنوان')
    text = models.TextField(blank=True, verbose_name='درباره ی تگ')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نوع خبر'
        verbose_name_plural = 'انواع خبر'
        ordering = ('-created_date_time', 'title')


class News(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
    )

    title = models.CharField(unique=True, max_length=127, verbose_name='عنوان')
    summary = models.CharField(max_length=255, blank=True, verbose_name='خلاصه خبر')
    text = models.TextField(blank=True, verbose_name='متن خبر')
    type = models.ForeignKey(NewsType, on_delete=models.CASCADE, verbose_name='نوع خبر')
    image_url = models.URLField(verbose_name='آدرس تصویر')
    field = models.CharField(max_length=3, choices=FIELDS, default='FTB', verbose_name='ورزش')
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


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name='خبر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    title = models.CharField(max_length=31, verbose_name='عنوان')
    text = models.CharField(max_length=255, verbose_name='متن')

    created_date_time = models.DateTimeField(verbose_name='زمان ساخت')
    deleted = models.BooleanField(default=False, verbose_name='حذف شده')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        ordering = ('-created_date_time', 'title',)

    def __str__(self):
        return self.title
