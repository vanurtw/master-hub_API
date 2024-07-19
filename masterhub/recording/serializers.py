from rest_framework import serializers

from service.serializers import CategoriesSerializer
from user.models import Specialist
from service.models import Service
from user.models import ProfileMaster
from .models import WorkTime, Recording
from datetime import datetime, timedelta
from recording.models import WorkTime


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['id', 'name', 'job']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileMaster
        fields = ['id', 'name']


class ServicesSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=False, required=False)

    def __init__(self, *args, **kwargs):
        super(ServicesSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'GET':
            self.fields['category'] = CategoriesSerializer()

    specialist = serializers.SerializerMethodField()

    def get_specialist(self, obj):
        if obj.specialist:
            serializer = SpecialistSerializer(obj.specialist)
        else:
            serializer = ProfileSerializer(obj.profile)
        return serializer.data

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'price', 'photo', 'time', 'date_creation', 'category', 'specialist', ]


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


class TimeSerializer(serializers.Serializer):
    def to_representation(self, instance: timedelta):
        hour = str(instance.seconds // 3600).rjust(2, '0')
        minute = str((instance.seconds - int(hour) * 3600) // 60).rjust(2, '0')
        return f'{hour}:{minute}'


class WorkTimeSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        request = self.context.get('request')
        kwargs = self.context.get('kwargs')
        services = self.context.get('service')
        result = []
        date = request.GET.get('date', None)
        if date:
            date_now = datetime.strptime(date, '%d/%m/%Y')
        else:
            date_now = datetime.now()  # дата записи

        services_date = timedelta(hours=services.time.hour, minutes=services.time.minute)  # время оказания услуги
        date_day = date_now.strftime('%A').lower()
        work_time_day = getattr(obj, date_day).split('-')
        if len(work_time_day) <= 1:
            return 'no time'
        work_start_datetime = datetime.strptime(work_time_day[0], '%H:%M')
        work_start = timedelta(hours=work_start_datetime.hour,
                               minutes=work_start_datetime.minute)  # время начала работы мастера
        work_end_datetime = datetime.strptime(work_time_day[1], '%H:%M')
        work_end = timedelta(hours=work_end_datetime.hour,
                             minutes=work_end_datetime.minute)  # время конца работы мастера
        if self.context.get('param') == 'master':
            recordings = Recording.objects.filter(profile_master__id=kwargs.get('pk'), date=date_now).values(
                'time_start', 'time_end')
        else:
            recordings = Recording.objects.filter(specialist__id=services.specialist.id, date=date_now).values(
                'time_start', 'time_end')
        while work_start < work_end:
            flag = True
            for i in recordings:
                datetime_start = timedelta(hours=i['time_start'].hour, minutes=i['time_start'].minute)
                datetime_end = timedelta(hours=i['time_end'].hour, minutes=i['time_end'].minute)
                if work_start + services_date < datetime_start:
                    flag = False
                    result.append(work_start)
                    work_start += timedelta(minutes=30)
                else:
                    if work_start > datetime_end:
                        result.append(work_start)
                        work_start += timedelta(minutes=30)
                    else:
                        work_start = datetime_end + timedelta(minutes=30)
            result.append(work_start)
            work_start += timedelta(minutes=30)
        return TimeSerializer(result, many=True).data

    class Meta:
        model = WorkTime
        fields = ['time']


class RecordingSerializer(serializers.ModelSerializer):
    profile_master = serializers.SerializerMethodField()
    service = serializers.SerializerMethodField()

    def get_profile_master(self, obj):
        serializer = ProfileSerializer(obj.profile_master)
        return serializer.data

    def get_service(self, obj):
        serializer = ServicesSerializer(obj.service)
        return serializer.data

    class Meta:
        model = Recording
        fields = ['id', 'profile_master', 'service', 'date', 'time_start', 'time_end']


class RecordinCreateSerializer(serializers.Serializer):
    time = serializers.TimeField(format='%H:%M')
    date = serializers.DateField(format='%Y-%m-%d')
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    name = serializers.CharField(max_length=30)
    surname = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=12)