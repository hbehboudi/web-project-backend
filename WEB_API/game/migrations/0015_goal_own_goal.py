# Generated by Django 2.1.5 on 2019-01-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_auto_20190130_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='own_goal',
            field=models.BooleanField(default=False, verbose_name='گل به خودی'),
        ),
    ]