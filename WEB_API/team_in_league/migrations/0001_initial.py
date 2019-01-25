# Generated by Django 2.1.5 on 2019-01-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamLeague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
                ('active', models.BooleanField(default=False, verbose_name='در حال برگزاری مسابقات')),
                ('league', models.ForeignKey(on_delete=True, to='leagues.League', verbose_name='لیگ')),
                ('team', models.ForeignKey(on_delete=True, to='team.Team', verbose_name='تیم')),
            ],
            options={
                'verbose_name': 'حضور تیم در لیگ',
                'verbose_name_plural': 'حضور تیم ها در لیگ ها',
                'ordering': ('-created_date_time', 'team', 'league'),
            },
        ),
    ]