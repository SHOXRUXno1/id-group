# Generated by Django 5.0.8 on 2022-09-28 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0066_contacts_youtube_alter_contactform_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='content',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='content_uz',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 9, 29, 2, 39, 25, 105575), null=True, verbose_name='Получено'),
        ),
    ]
