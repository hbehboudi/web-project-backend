# Generated by Django 2.1.5 on 2019-01-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190127_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='team_state1',
            field=models.CharField(default='Draw', max_length=31, verbose_name=(('W', 'Win'), ('D', 'Draw'), ('L', 'Lose'))),
        ),
        migrations.AddField(
            model_name='game',
            name='team_state2',
            field=models.CharField(default='Draw', max_length=31, verbose_name=(('W', 'Win'), ('D', 'Draw'), ('L', 'Lose'))),
        ),
    ]
