# Generated by Django 4.0.2 on 2022-03-18 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0013_rename_small_banner_about_banner_image1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plans',
            name='banner',
        ),
        migrations.AddField(
            model_name='plans',
            name='file',
            field=models.FileField(null=True, upload_to='about/', verbose_name='File name'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 3, 18, 11, 8, 35, 175855), null=True, verbose_name='Получено'),
        ),
    ]
