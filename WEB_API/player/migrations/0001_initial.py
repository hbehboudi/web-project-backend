# Generated by Django 2.1.5 on 2019-01-24 08:31

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
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.UUIDField(auto_created=True, db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=64, verbose_name='نام')),
                ('nickname', models.CharField(max_length=64, verbose_name='لقب')),
                ('post', models.CharField(choices=[('GK', 'Goalkeeper'), ('CB', 'Center fullback'), ('SW', 'Sweeper'), ('LFB', 'Left fullback'), ('RFB', 'Right fullback'), ('WB', 'Wingback'), ('LM', 'Left midfield'), ('RM', 'Right midfield'), ('DM', 'Defensive midfield'), ('CM', 'Center midfield'), ('WM', 'Wide midfield'), ('CF', 'Center forward'), ('AM', 'Attacking midfield'), ('S', 'Striker'), ('SS', 'Second striker'), ('LW', 'Left winger'), ('RW', 'Right winger')], max_length=3, verbose_name='پست')),
                ('nationality', models.CharField(max_length=64, verbose_name='ملیت')),
                ('team', models.CharField(max_length=64, verbose_name='باشگاه')),
                ('city', models.CharField(max_length=64, verbose_name='محل تولد')),
                ('age', models.IntegerField(max_length=3, verbose_name='سن')),
                ('height', models.FloatField(max_length=4, verbose_name='قد')),
                ('weight', models.IntegerField(max_length=3, verbose_name='وزن')),
                ('teamNum', models.IntegerField(max_length=2, verbose_name='شماره پیراهن در باشگاه')),
                ('nationalityTeamNum', models.IntegerField(max_length=2, verbose_name='شماره پیراهن در تیم ملی')),
                ('website', models.URLField(verbose_name='وب سایت')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('image_url', models.URLField(blank=True, verbose_name='آدرس تصویر لیگ')),
                ('field', models.CharField(choices=[('FTB', 'Football'), ('BSK', 'Basketball')], default='OTH', max_length=3, verbose_name='ورزش')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
                ('tags', models.ManyToManyField(blank=True, to='tag.Tag', verbose_name='تگ ها')),
            ],
            options={
                'verbose_name': 'بازیکن',
                'ordering': ('-created_date_time', 'name'),
            },
        ),
        migrations.CreateModel(
            name='PlayerSliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='عنوان')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('image_url', models.URLField(blank=True, verbose_name='آدرس تصویر')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.Player', verbose_name='تیم')),
            ],
            options={
                'verbose_name': 'تصویر اسلایدر بازیکن',
                'ordering': ('-created_date_time', 'title'),
            },
        ),
    ]