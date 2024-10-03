# Generated by Django 4.0.3 on 2023-12-19 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0003_alter_contactform_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsefulLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(null=True, upload_to='logo/', verbose_name='Useful links')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': '7.2 Полезные ссылки',
                'verbose_name_plural': '7.2 Полезные ссылки',
            },
        ),
        migrations.AddField(
            model_name='trust',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Company Link'),
        ),
        migrations.AddField(
            model_name='trust',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 12, 19, 20, 56, 34, 187674), null=True, verbose_name='Получено'),
        ),
    ]