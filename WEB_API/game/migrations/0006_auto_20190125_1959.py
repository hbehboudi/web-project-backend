# Generated by Django 2.1.5 on 2019-01-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20190125_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereport',
            name='minute',
            field=models.IntegerField(verbose_name='دقیقه'),
        ),
        migrations.AlterField(
            model_name='gamereport',
            name='second',
            field=models.IntegerField(verbose_name='ثانیه'),
        ),
    ]