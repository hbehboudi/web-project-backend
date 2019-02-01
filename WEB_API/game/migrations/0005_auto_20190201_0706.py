# Generated by Django 2.1.5 on 2019-02-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20190201_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='corners1',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='کرنر های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='corners2',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='کرنر های تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='counter_attack1',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='ضدحمله های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='counter_attack2',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='ضدحمله های تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='fouls1',
            field=models.IntegerField(blank=True, null=True, verbose_name='خطا های تیم۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='fouls2',
            field=models.IntegerField(blank=True, null=True, verbose_name='خطا های تیم۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='goals1',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='گل های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='goals2',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='گل های تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='offsides1',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='آفساید های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='offsides2',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='آفساید های تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='out1',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='اخراج های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='out2',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='اخراج های تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='passes1',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='پاس های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='passes2',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='پاس های تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='possession1',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='مالکیت توپ تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='possession2',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='مالکیت توپ تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='red_cards1',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='کارت قرمز های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='red_cards2',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='کارت قرمز های تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='ribbond1',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='ریباند تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='ribbond2',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='ریباند تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='score1_team1',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='پرتاب های ۱ امتیازی تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='score1_team2',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='پرتاب های ۱ امتیازی تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='score2_team1',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='پرتاب های ۲ امتیازی تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='score2_team2',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='پرتاب های ۲ امتیازی تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='score3_team1',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='پرتاب های ۳ امتیازی تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='score3_team2',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='پرتاب های ۳ امتیازی تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='shots1',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='شوت های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='shots2',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='شوت های تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='shots_on_target1',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='شوت های داخل چارچوب تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='shots_on_target2',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='شوت های داخل چارچوب تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='style1',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='استیل های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='style2',
            field=models.IntegerField(blank=True, help_text='برای بازی بسکتبال', null=True, verbose_name='استیل های تیم ۲'),
        ),
        migrations.AlterField(
            model_name='game',
            name='yellow_cards1',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='کارت زرد های تیم ۱'),
        ),
        migrations.AlterField(
            model_name='game',
            name='yellow_cards2',
            field=models.IntegerField(blank=True, help_text='برای بازی فوتبال', null=True, verbose_name='کارت زرد های تیم ۲'),
        ),
    ]