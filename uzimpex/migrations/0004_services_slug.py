# Generated by Django 4.0.2 on 2022-02-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0003_plans'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.SlugField(null=True, verbose_name='Slug'),
        ),
    ]
