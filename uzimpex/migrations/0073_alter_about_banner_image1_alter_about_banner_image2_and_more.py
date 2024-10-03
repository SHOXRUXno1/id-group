# Generated by Django 5.0.9 on 2024-09-30 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0072_alter_about_options_alter_banner_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='banner_image1',
            field=models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Banner1'),
        ),
        migrations.AlterField(
            model_name='about',
            name='banner_image2',
            field=models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Banner2'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 10, 1, 1, 33, 32, 269584), null=True, verbose_name='Получено'),
        ),
    ]
