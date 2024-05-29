from django.contrib import admin
from .models import CustomUser, ProfileMaster


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'specialization']
    list_display_links = ['id', 'username']


@admin.register(ProfileMaster)
class ProfileMasterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    list_display_links = ['id', 'name']

