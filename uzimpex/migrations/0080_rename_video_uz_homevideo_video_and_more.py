# Generated by Django 5.0.9 on 2024-10-01 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0079_homevideo_video_uz_alter_contactform_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homevideo',
            old_name='video_uz',
            new_name='video',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 10, 2, 4, 3, 37, 509069), null=True, verbose_name='Получено'),
        ),
    ]
