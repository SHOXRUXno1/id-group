# Generated by Django 5.0.9 on 2024-09-30 20:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0073_alter_about_banner_image1_alter_about_banner_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 10, 1, 1, 51, 59, 844057), null=True, verbose_name='Получено'),
        ),
    ]
