# Generated by Django 4.0.3 on 2023-12-07 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 7, 17, 41, 0, 530814), null=True, verbose_name='Получено'),
        ),
    ]
