# Generated by Django 5.0.6 on 2024-07-01 04:37

import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_profilemaster_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemaster',
            name='photo',
            field=models.ImageField(default='media/users/default.jpg', upload_to=user.models.upload_photo_profile),
        ),
    ]
