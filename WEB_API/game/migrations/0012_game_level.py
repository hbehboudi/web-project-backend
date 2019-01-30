# Generated by Django 2.1.5 on 2019-01-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_auto_20190128_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='level',
            field=models.CharField(choices=[(1, 'هفته اول'), (2, 'هفته دوم'), (3, 'هفته سوم'), (4, 'هفته چهارم'), (5, 'هفته پنجم'), (6, 'هفته ششم'), (7, 'هفته هفتم'), (8, 'هفته هشتم'), (9, 'هفته نهم'), (10, 'هفته دهم'), (11, 'هفته یازدهم'), (12, 'هفته دوازدهم'), (13, 'هفته سیزدهم'), (14, 'هفته چهاردهم'), (15, 'هفته پانزدهم'), (16, 'هفته شانزدهم'), (17, 'هفته هفدهم'), (18, 'هفته هجدهم'), (19, 'هفته نوزدهم'), (20, 'هفته بیستم'), (21, 'هفته بیست و یکم'), (22, 'هفته بیست و دوم'), (23, 'هفته بیست و سوم'), (24, 'هفته بیست و چهارم'), (25, 'هفته بیست و پنجم'), (26, 'هفته بیست و ششم'), (27, 'هفته بیست و هفتم'), (28, 'هفته بیست و هشتم'), (29, 'هفته بیست و نهم'), (30, 'هفته سی ام'), ('1/16', 'یک شانزدهم'), ('1/8', 'یک هشتم'), ('1/4', 'یک چهارم'), ('1/2', 'نیمه نهایی'), ('F', 'فینال'), ('R', 'رده بندی')], default='1', max_length=7, verbose_name='مرحله'),
        ),
    ]
