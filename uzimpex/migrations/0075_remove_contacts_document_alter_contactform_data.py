# Generated by Django 5.0.9 on 2024-09-30 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0074_alter_contactform_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='document',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 10, 1, 2, 3, 2, 897614), null=True, verbose_name='Получено'),
        ),
    ]
