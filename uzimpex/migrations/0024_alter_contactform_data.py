# Generated by Django 4.0.3 on 2022-03-22 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0023_alter_contactform_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 3, 22, 21, 46, 54, 199135), null=True, verbose_name='Получено'),
        ),
    ]