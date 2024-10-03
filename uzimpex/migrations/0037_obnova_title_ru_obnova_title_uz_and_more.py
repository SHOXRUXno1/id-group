# Generated by Django 4.0.3 on 2022-05-31 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0036_obnova_image_obnova_slug_obnova_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='obnova',
            name='title_ru',
            field=models.CharField(max_length=2000, null=True, verbose_name='News title'),
        ),
        migrations.AddField(
            model_name='obnova',
            name='title_uz',
            field=models.CharField(max_length=2000, null=True, verbose_name='News title'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 5, 31, 11, 47, 59, 736206), null=True, verbose_name='Получено'),
        ),
    ]