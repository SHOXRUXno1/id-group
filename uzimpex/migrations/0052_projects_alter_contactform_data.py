# Generated by Django 4.0.3 on 2022-01-19 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0051_merge_20240119_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viloyat', models.CharField(max_length=60)),
                ('project_soni', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': '7.4 Проекты',
                'verbose_name_plural': '7.4 Проекты',
            },
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 1, 19, 9, 49, 28, 98461), null=True, verbose_name='Получено'),
        ),
    ]
