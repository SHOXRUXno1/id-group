# Generated by Django 5.0 on 2023-12-15 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0043_trust_name_alter_contactform_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 15, 18, 13, 28, 715508), null=True, verbose_name='Получено'),
        ),
    ]