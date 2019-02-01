# Generated by Django 2.1.5 on 2019-02-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190201_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_date_time', 'title'), 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت'),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('title',)},
        ),
    ]
