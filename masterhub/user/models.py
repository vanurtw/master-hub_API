from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


# Create your models here.

def upload_photo_profile(instance, filename):
    if instance.specialist:
        return f'{settings.BASE_DIR}/static/media/specialist/{instance.specialist.name}/{filename}'
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

    CHOICES = [
        ('master', 'мастер'),
        ('studio', 'студия'),
    ]
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
    specialization = models.CharField(
        choices=CHOICES,
        max_length=25,
        default='master',
        verbose_name='специализация'
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

    def __str__(self):
        return f'profile_{self.user}_{self.specialization}'


class Specialist(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=255
    )
    job = models.CharField(
        verbose_name='кфалификация',
        max_length=50
    )
    description = models.TextField(verbose_name='описание')
    profile = models.ForeignKey(
        ProfileMaster,
        on_delete=models.CASCADE,
        related_name='profile_specialist',
        verbose_name='профиль',
        blank=True,
        null=True
    )
    def __str__(self):
        return f'specialist_{self.profile}'


class ProfileImages(models.Model):
    profile = models.ForeignKey(
        ProfileMaster,
        verbose_name='профиль',
        on_delete=models.CASCADE,
        related_name='profile_images',
        blank=True,
        null=True
    )
    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        related_name='profile_services',
        verbose_name='специалист',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to=upload_photo_profile,
    )
    date_creation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'image_{self.profile}'


class Reviews(models.Model):
    CHOICES = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    ]
    profile = models.ForeignKey(
        ProfileMaster,
        on_delete=models.CASCADE,
        related_name='reviews_profile',
        verbose_name='профиль мастера/студии'
    )
    rating_star = models.CharField(
        verbose_name='кол-во звезд',
        choices=CHOICES,
        max_length=1,
        default='5'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )
    description = models.TextField(verbose_name='описание')
    data_create = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'отзыв'


class Favorites(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='favorites_user',
        verbose_name='пользователь'
    )
    profile = models.ForeignKey(
        ProfileMaster,
        related_name='favorites_profile',
        on_delete=models.CASCADE,
        verbose_name='профиль мастера/студии'
    )
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'избранное'

# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, **kwargs):
#     pass
