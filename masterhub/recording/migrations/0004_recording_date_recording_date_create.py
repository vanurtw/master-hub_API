# Generated by Django 5.0.6 on 2024-06-06 07:22

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recording', '0003_recording'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='дата записи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recording',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 6, 6, 7, 22, 28, 223641, tzinfo=datetime.timezone.utc), verbose_name='дата создания записи'),
            preserve_default=False,
        ),
    ]