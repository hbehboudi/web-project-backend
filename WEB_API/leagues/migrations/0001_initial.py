# Generated by Django 2.1.5 on 2019-01-31 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=31, verbose_name='عنوان')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
            ],
            options={
                'verbose_name': 'برترین بازیکن',
                'verbose_name_plural': 'برترین بازیکنان',
                'ordering': ('-created_date_time', 'player'),
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, verbose_name='نام لیگ')),
                ('year', models.CharField(max_length=31, verbose_name='سال')),
                ('confederation', models.CharField(max_length=31, verbose_name='کنفدراسیون')),
                ('country', models.CharField(blank=True, max_length=31, verbose_name='کشور')),
                ('numberOfTeams', models.IntegerField(verbose_name='تعداد تیم ها')),
                ('bestTeam', models.CharField(blank=True, max_length=63, verbose_name='بهترین تیم')),
                ('establishedYear', models.IntegerField(verbose_name='سال تاسیس')),
                ('website', models.URLField(blank=True, verbose_name='وب سایت')),
                ('field', models.CharField(choices=[('FTB', 'Football'), ('BSK', 'Basketball')], default='OTH', max_length=3, verbose_name='ورزش')),
                ('image_url', models.URLField(verbose_name='آدرس تصویر لیگ')),
                ('active', models.BooleanField(default=True, verbose_name='در حال برگذاری مسابقات')),
                ('level', models.CharField(choices=[('1', 'هفته اول'), ('2', 'هفته دوم'), ('3', 'هفته سوم'), ('4', 'هفته چهارم'), ('5', 'هفته پنجم'), ('6', 'هفته ششم'), ('7', 'هفته هفتم'), ('8', 'هفته هشتم'), ('9', 'هفته نهم'), ('10', 'هفته دهم'), ('11', 'هفته یازدهم'), ('12', 'هفته دوازدهم'), ('13', 'هفته سیزدهم'), ('14', 'هفته چهاردهم'), ('15', 'هفته پانزدهم'), ('16', 'هفته شانزدهم'), ('17', 'هفته هفدهم'), ('18', 'هفته هجدهم'), ('19', 'هفته نوزدهم'), ('20', 'هفته بیستم'), ('21', 'هفته بیست و یکم'), ('22', 'هفته بیست و دوم'), ('23', 'هفته بیست و سوم'), ('24', 'هفته بیست و چهارم'), ('25', 'هفته بیست و پنجم'), ('26', 'هفته بیست و ششم'), ('27', 'هفته بیست و هفتم'), ('28', 'هفته بیست و هشتم'), ('29', 'هفته بیست و نهم'), ('30', 'هفته سی ام'), ('1/16', 'یک شانزدهم'), ('1/8', 'یک هشتم'), ('1/4', 'یک چهارم'), ('1/2', 'نیمه نهایی'), ('F', 'فینال'), ('R', 'رده بندی')], max_length=7, verbose_name='مرحله')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=255, unique=True)),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
                ('tags', models.ManyToManyField(blank=True, to='tag.Tag', verbose_name='تگ ها')),
            ],
            options={
                'verbose_name': 'لیگ',
                'verbose_name_plural': 'لیگ ها',
                'ordering': ('-created_date_time', 'name'),
            },
        ),
        migrations.CreateModel(
            name='LeagueSliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='عنوان')),
                ('image_url', models.URLField(verbose_name='آدرس تصویر')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League', verbose_name='لیگ')),
            ],
            options={
                'verbose_name': 'تصویر اسلایدر لیگ',
                'verbose_name_plural': 'تصاویر اسلایدر لیگ',
                'ordering': ('-created_date_time', 'title'),
            },
        ),
        migrations.AddField(
            model_name='bestplayer',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League', verbose_name='لیگ'),
        ),
        migrations.AddField(
            model_name='bestplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Player', verbose_name='بازیکن'),
        ),
        migrations.AlterUniqueTogether(
            name='league',
            unique_together={('name', 'year')},
        ),
    ]
