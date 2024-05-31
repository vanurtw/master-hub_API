from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


# Create your models here.

def upload_photo_profile(instance, filename):
    return f'{settings.BASE_DIR}/static/media/profile/{instance.profile.user}/{filename}'


class CustomUser(AbstractUser):
    """Модель юзера"""

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
    """Профиль студии/мастера"""
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
    link_vk = models.URLField(
        verbose_name='ссылка на VK',
        blank=True
    )
    link_tg = models.URLField(
        verbose_name='ссылка на TG',
        blank=True
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True
    )
    date_creation = models.DateField(
        verbose_name='дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Профиль мастера/студия'
        verbose_name_plural = 'Профили мастеров/студий'


class ProfileImages(models.Model):
    profile = models.ForeignKey(
        ProfileMaster,
        verbose_name='профиль',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to=upload_photo_profile,
    )
    date_creation = models.DateField(auto_now_add=True)

# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, **kwargs):
#     pass
