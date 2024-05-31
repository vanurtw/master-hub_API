from django.contrib import admin
from .models import CustomUser, ProfileMaster, ProfileImages


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['id', 'username']


@admin.register(ProfileMaster)
class ProfileMasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    list_display_links = ['id', 'name']


@admin.register(ProfileImages)
class ProfileImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'date_creation']
    list_filter = ['profile', 'date_creation']

