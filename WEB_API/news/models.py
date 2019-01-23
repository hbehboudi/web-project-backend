import uuid

from django.db import models


class Tag(models.Model):
    tag = models.CharField(primary_key=True, max_length=32)

    def __str__(self):
        return self.tag


class News(models.Model):
    FIELDS = (
        ('FTB', 'Football'),
        ('BSK', 'Basketball'),
        ('OTH', 'Other'),
    )

    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=256, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=16, null=True)
    created_date_time = models.DateTimeField()
    image_url = models.URLField(null=False, blank=True)
    field = models.CharField(max_length=3, choices=FIELDS, default='OTH')
    url = models.UUIDField(default=uuid.uuid4, db_index=True, unique=True, editable=False, auto_created=True)
    tags = models.ManyToManyField(Tag, blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        ordering = ('-created_date_time', 'title')
