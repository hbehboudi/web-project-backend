# Generated by Django 2.1.5 on 2019-01-28 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_substitute'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='substitute',
            options={'ordering': ('-created_date_time', 'game'), 'verbose_name': 'تعویض', 'verbose_name_plural': 'تعویض'},
        ),
    ]