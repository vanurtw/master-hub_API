from django.contrib import admin
from .models import WorkTime


# Register your models here.


@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    pass
