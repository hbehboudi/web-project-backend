# Generated by Django 2.1.5 on 2019-02-01 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20190201_1804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ('-created_date_time', 'team'), 'verbose_name': 'علاقه مندی', 'verbose_name_plural': 'علاقه مندی ها'},
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
    ]
