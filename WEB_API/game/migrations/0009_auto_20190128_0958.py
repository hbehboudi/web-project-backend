# Generated by Django 2.1.5 on 2019-01-28 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_game_full_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('-game_date', 'team1', 'team2', 'league'), 'verbose_name': 'بازی', 'verbose_name_plural': 'بازی ها'},
        ),
    ]