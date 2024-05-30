from django.db import models

from user.models import CustomUser
# Create your models here.
from django.conf import settings


def upload_photo_service(instance, filename):
    return f'{settings.BASE_DIR}/static/media/service/{instance.user}/{filename}'


class Service(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        blank=True,

    )
    title = models.CharField(
        verbose_name='заголовок',
        max_length=255,
        blank=True
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True
    )
    price = models.IntegerField(
        verbose_name='цена',
        default=0
    )
    photo = models.ImageField(
        verbose_name='изображение',
        upload_to=upload_photo_service,
        blank=True
    )

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
