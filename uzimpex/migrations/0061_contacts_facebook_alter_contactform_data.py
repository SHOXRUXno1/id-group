# Generated by Django 5.0.8 on 2022-09-16 20:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0060_alter_contactform_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='facebook',
            field=models.CharField(default='EXIT', max_length=200, verbose_name='Facebook'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 9, 17, 1, 14, 30, 63725), null=True, verbose_name='Получено'),
        ),
    ]
