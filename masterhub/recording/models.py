from django.db import models
from user.models import ProfileMaster, CustomUser, Specialist
from service.models import Service
from datetime import time


class Recording(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='user_recordings'

    )
    profile_master = models.ForeignKey(
        ProfileMaster,
        on_delete=models.CASCADE,
        related_name='profile_recordings',
        blank=True,
        null=True

    )
    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    date = models.DateField(verbose_name='дата записи')
    time_start = models.TimeField()
    time_end = models.TimeField(
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=20,
        verbose_name='Имя',
        blank=True,
        null=True
    )

    surname = models.CharField(
        max_length=20,
        verbose_name='Фамилия',
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Номер',
        blank=True,
        null=True
    )
    date_create = models.DateTimeField(
        verbose_name='дата создания записи',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'запись'


class WorkTime(models.Model):
    profile_master = models.ForeignKey(
        ProfileMaster,
        verbose_name='Профиль мастера',
        on_delete=models.CASCADE,
        related_name='work_times',
        blank=True,
        null=True
    )
    specialist = models.ForeignKey(
        Specialist,
        verbose_name='Специалист',
        on_delete=models.CASCADE,
        related_name='work_times',
        blank=True,
        null=True
    )
    date = models.DateField()
    break_time = models.TimeField(
        verbose_name='время перерыва',
        default='00:30:00'
    )

    class Meta:
        verbose_name = 'Рабочее время'
