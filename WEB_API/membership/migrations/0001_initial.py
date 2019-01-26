# Generated by Django 2.1.5 on 2019-01-26 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leagues', '0001_initial'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
            ],
            options={
                'verbose_name': 'حضور بازیکن در بازی',
                'verbose_name_plural': 'حضور بازیکن ها در بازی ها',
                'ordering': ('-created_date_time', 'player'),
            },
        ),
        migrations.CreateModel(
            name='PlayerTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='شماره پیراهن')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
            ],
            options={
                'verbose_name': 'حضور بازیکن در تیم',
                'verbose_name_plural': 'حضور بازیکن ها در تیم ها',
                'ordering': ('-created_date_time', 'player'),
            },
        ),
        migrations.CreateModel(
            name='TeamLeague',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
                ('active', models.BooleanField(default=False, verbose_name='در حال برگزاری مسابقات')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League', verbose_name='لیگ')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team', verbose_name='تیم')),
            ],
            options={
                'verbose_name': 'حضور تیم در لیگ',
                'verbose_name_plural': 'حضور تیم ها در لیگ ها',
                'ordering': ('-created_date_time', 'team', 'league'),
            },
        ),
    ]
