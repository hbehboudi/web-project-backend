# Generated by Django 2.1.5 on 2019-01-31 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='عنوان')),
                ('image_url', models.URLField(verbose_name='آدرس تصویر')),
                ('created_date_time', models.DateTimeField(verbose_name='زمان ساخت')),
                ('field', models.CharField(choices=[('FTB', 'Football'), ('BSK', 'Basketball')], default='FTB', max_length=3, verbose_name='ورزش')),
                ('deleted', models.BooleanField(default=False, verbose_name='حذف شده')),
            ],
            options={
                'verbose_name': 'تصویر اسلایدر اصلی',
                'verbose_name_plural': 'تصاویر اسلایدر اصلی',
                'ordering': ('-created_date_time', 'title'),
            },
        ),
    ]
