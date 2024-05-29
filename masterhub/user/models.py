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


class ProfileMaster(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True
    )
    name = models.CharField(
        verbose_name='имя',
        max_length=255,
        blank=True
    )
    address = models.CharField(
        verbose_name='адрес',
        max_length=255,
        blank=True
    )
    phone = models.CharField(
        verbose_name='телефон',
        max_length=255,
        blank=True
    )
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'Профиль мастера/студия'
        verbose_name_plural = 'Профили мастеров/студий'


