# Generated by Django 5.0.6 on 2024-07-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_profilemaster_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemaster',
            name='time_relax',
            field=models.TimeField(default='00:30:00', verbose_name='время отдыха между процедурами'),
        ),
    ]
