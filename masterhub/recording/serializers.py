from rest_framework import serializers
from user.models import ProfileMaster, Specialist
from service.models import Service
from user.models import ProfileMaster
from .models import WorkTime, Recording
from datetime import datetime, time


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['id', 'name', 'job']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileMaster
        fields = ['id', 'name']


class ServicesSerializer(serializers.ModelSerializer):
    specialist = serializers.SerializerMethodField()

    def get_specialist(self, obj):
        if obj.specialist:
            serializer = SpecialistSerializer(obj.specialist)
        else:
            serializer = ProfileSerializer(obj.profile)
        return serializer.data

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'price', 'photo', 'time', 'category', 'specialist', ]


class ServicesRecordingSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        self.categories = []
        super(ServicesRecordingSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        cat_id = instance.id
        if cat_id not in self.categories:
            self.categories.append(cat_id)
            services_context = self.context.get('services')
            services = services_context.filter(category__id=cat_id)
            serializer = ServicesSerializer(services, many=True)
            return {instance.title: serializer.data}


class WorkTimeSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        request = self.context.get('request')
        kwargs = self.context.get('kwargs')
        result = []
        date_now = datetime.now()
        services = Service.objects.get(id=kwargs.get('pk'))
        services_datetime = date_now.replace(hour=services.time.hour, minute=services.time.minute)
        date_day = date_now.strftime('%A').lower()
        work_time_day = getattr(obj, date_day).split('-')
        work_start = datetime.strptime(work_time_day[0], '%H:%M')
        work_end = datetime.strptime(work_time_day[1], '%H:%M')
        recordings = Recording.objects.filter(profile_master__id=kwargs.get('id_specialist'), date=date_now).values(
            'time_start', 'time_end')
        while work_start < work_end:
            flag = True
            for i in recordings:
                datetime_start = date_now.replace(hour=i['time_start'].hour, minute=i['time_start'].minute)
                datetime_end = date_now.replace(hour=i['time_end'].hour, minute=i['time_end'].minute)
                if work_start + services_datetime >= datetime_start:
                    flag = False
                    work_start = work_end.replace()
                pass

    class Meta:
        model = WorkTime
        fields = ['time']
