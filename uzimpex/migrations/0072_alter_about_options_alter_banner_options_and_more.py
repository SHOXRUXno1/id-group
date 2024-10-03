# Generated by Django 5.0.9 on 2022-09-29 21:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0071_documents_content_documents_content_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'О Компании', 'verbose_name_plural': 'О Компании'},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Баннер', 'verbose_name_plural': 'Баннер'},
        ),
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name': 'Контактная форма', 'verbose_name_plural': 'Контактная форма'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='documents',
            options={'verbose_name': 'Документы', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterModelOptions(
            name='homevideo',
            options={'verbose_name': 'Видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.AlterModelOptions(
            name='links',
            options={'verbose_name': 'Полезные ссылки', 'verbose_name_plural': 'Полезные ссылки'},
        ),
        migrations.AlterModelOptions(
            name='otdeli',
            options={'verbose_name': 'Отделы', 'verbose_name_plural': 'Отделы'},
        ),
        migrations.AlterModelOptions(
            name='ruk',
            options={'verbose_name': 'Руководство', 'verbose_name_plural': 'Руководство'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Сервисы', 'verbose_name_plural': 'Сервисы'},
        ),
        migrations.AlterModelOptions(
            name='usefullinks',
            options={'verbose_name': 'Партнёры', 'verbose_name_plural': 'Партнёры'},
        ),
        migrations.AlterModelOptions(
            name='vacansiya',
            options={'verbose_name': 'Вакансии', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 9, 30, 2, 54, 41, 366197), null=True, verbose_name='Получено'),
        ),
    ]