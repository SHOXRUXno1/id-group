# Generated by Django 5.0 on 2023-12-15 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0042_trust_link_alter_contactform_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='trust',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 15, 17, 48, 12, 981656), null=True, verbose_name='Получено'),
        ),
    ]
