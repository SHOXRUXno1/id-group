# Generated by Django 5.0 on 2023-12-15 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0041_about_description2_en_about_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trust',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Company Link'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 15, 17, 42, 58, 623128), null=True, verbose_name='Получено'),
        ),
    ]