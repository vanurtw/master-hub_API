# Generated by Django 5.0.6 on 2024-06-05 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_favorites'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorites',
            options={'verbose_name': 'избранное'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'отзыв'},
        ),
    ]