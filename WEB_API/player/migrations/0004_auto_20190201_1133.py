# Generated by Django 2.1.5 on 2019-02-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_auto_20190201_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.IntegerField(blank=True, verbose_name='قد'),
        ),
    ]
