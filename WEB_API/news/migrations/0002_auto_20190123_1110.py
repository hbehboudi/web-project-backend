# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-23 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('date', 'title'), 'verbose_name': 'News'},
        ),
    ]
