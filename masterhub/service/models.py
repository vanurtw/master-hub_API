from django.db import models

# Create your models here.


# class Service(models.Model):
#     user = models.OneToOneField(
#         CustomUser,
#         on_delete=models.CASCADE,
#         blank=True,
#
#     )
#     title = models.CharField(
#         verbose_name='заголовок',
#         max_length=255,
#         blank=True
#     )
#     description = models.TextField(
#         verbose_name='описание',
#         blank=True
#     )
#     price = models.IntegerField(
#         verbose_name='цена',
#         blank=True
#     )
#
#     class Meta:
#         verbose_name = 'услуга'
#         verbose_name_plural = 'услуги'
