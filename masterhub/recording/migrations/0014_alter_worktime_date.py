# Generated by Django 5.0.6 on 2024-07-22 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recording', '0013_worktime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='date',
            field=models.DateField(),
        ),
    ]