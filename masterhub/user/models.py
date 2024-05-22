from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    CHOICES = [
        ('M', 'мастер'),
        ('S', 'студия'),
        ('C', 'клиент'),
    ]
    specialization = models.CharField(
        verbose_name='специализация',
        choices=CHOICES,
        max_length=1,
        blank=True,
    )
