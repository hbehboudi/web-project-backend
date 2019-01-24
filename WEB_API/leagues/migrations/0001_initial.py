# Generated by Django 2.1.5 on 2019-01-24 07:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.UUIDField(auto_created=True, db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=64, verbose_name='نام لیگ')),
                ('year', models.IntegerField(verbose_name='سال')),
                ('confederation', models.CharField(max_length=32, verbose_name='کنفدراسیون')),
                ('country', models.CharField(blank=True, help_text='اجباری نیست.', max_length=32, verbose_name='کشور')),
                ('level', models.IntegerField(blank=True, verbose_name='دسته')),
                ('numberOfTeams', models.IntegerField(verbose_name='تعداد تیم ها')),
                ('bestTeam', models.CharField(blank=True, max_length=32, verbose_name='بهترین تیم')),
                ('establishedYear', models.IntegerField(verbose_name='سال تاسیس')),
                ('website', models.URLField(verbose_name='وب سایت')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('image_url', models.URLField(blank=True, verbose_name='آدرس تصویر لیگ')),
                ('field', models.CharField(choices=[('FTB', 'Football'), ('BSK', 'Basketball')], default='OTH', max_length=3, verbose_name='ورزش')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
                ('tags', models.ManyToManyField(blank=True, to='tag.Tag', verbose_name='تگ ها')),
            ],
            options={
                'verbose_name': 'لیگ',
                'ordering': ('-created_date_time', 'name'),
            },
        ),
        migrations.CreateModel(
            name='LeagueSliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('image_url', models.URLField(blank=True, verbose_name='آدرس تصویر')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League', verbose_name='لیگ')),
            ],
            options={
                'verbose_name': 'تصویر اسلایدر لیگ',
                'ordering': ('-created_date_time', 'title'),
            },
        ),
    ]