# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-23 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190123_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='news.Tag'),
        ),
    ]