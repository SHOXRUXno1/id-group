# Generated by Django 4.0.3 on 2022-04-08 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0032_alter_contactform_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 4, 8, 16, 27, 56, 496304), null=True, verbose_name='Получено'),
        ),
    ]
