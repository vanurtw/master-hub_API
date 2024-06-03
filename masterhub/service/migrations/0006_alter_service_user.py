# Generated by Django 5.0.6 on 2024-05-31 04:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_service_user'),
        ('user', '0004_alter_profileimages_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='user.profilemaster'),
        ),
    ]
