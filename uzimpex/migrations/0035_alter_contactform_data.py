# Generated by Django 4.0.3 on 2022-05-31 04:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0034_alter_obnova_options_alter_contactform_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 5, 31, 9, 53, 32, 607804), null=True, verbose_name='Получено'),
        ),
    ]