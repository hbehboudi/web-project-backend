# Generated by Django 2.1.5 on 2019-02-01 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20190201_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='placeBirth',
            new_name='birth_place',
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.IntegerField(blank=True, verbose_name='سن'),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.FloatField(blank=True, verbose_name='قد'),
        ),
        migrations.AlterField(
            model_name='player',
            name='nationalityTeamNum',
            field=models.IntegerField(blank=True, verbose_name='شماره پیراهن در تیم ملی'),
        ),
        migrations.AlterField(
            model_name='player',
            name='teamNum',
            field=models.IntegerField(blank=True, verbose_name='شماره پیراهن در باشگاه'),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.IntegerField(blank=True, verbose_name='وزن'),
        ),
    ]