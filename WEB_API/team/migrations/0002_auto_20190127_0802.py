# Generated by Django 2.1.5 on 2019-01-27 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='internatinalRank',
            new_name='internationalRank',
        ),
    ]
