# Generated by Django 5.0.6 on 2024-07-05 04:27

import service.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_service_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=service.models.upload_photo_service, verbose_name='изображение'),
        ),
    ]
