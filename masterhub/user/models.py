from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    CHOICES = [
        ('Мастер', 'мастер'),
        ('Студия', 'студия'),
        ('Клиент', 'клиент'),
    ]
    specialization = models.CharField(
        verbose_name='специализация',
        choices=CHOICES,
        max_length=10,
        blank=True,
    )
    username = models.CharField(
        verbose_name='имя',
        max_length=255,
        unique=True
    )
    email = models.EmailField(
        verbose_name='почта',
        unique=True
    )
