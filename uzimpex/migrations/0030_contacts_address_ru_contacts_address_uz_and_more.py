# Generated by Django 4.0.2 on 2022-04-07 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0029_rename_description2_en_about_description2_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='address_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Address '),
        ),
        migrations.AddField(
            model_name='contacts',
            name='address_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='Address '),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 4, 7, 15, 42, 34, 136076), null=True, verbose_name='Получено'),
        ),
    ]
