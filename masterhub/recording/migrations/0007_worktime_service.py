# Generated by Django 5.0.6 on 2024-06-17 05:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recording', '0006_alter_worktime_profile'),
        ('service', '0013_service_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktime',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]
