from recording.serializers import SpecialistSerializer
from user.models import ProfileMaster, ProfileImages, Reviews, Categories, Specialist
from rest_framework import serializers
from recording.models import WorkTime
from datetime import datetime, timedelta


class CategoriesAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id']


class ProfileAdminSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=False, required=False)
    categories = serializers.CharField(required=False, write_only=True)

    def validate_categories(self, attrs):
        categories = [int(i) for i in attrs.split()]
        cat_count = Categories.objects.filter(id__in=categories).count()
        if cat_count != len(categories):
            raise serializers.ValidationError('No such category')
        return categories

    class Meta:
        model = ProfileMaster
        fields = ['id',
                  'name',
                  'photo',
                  'address',
                  'phone',
                  'specialization',
                  'categories',
                  'link_vk',
                  'link_tg',
                  'description',
                  'time_relax',
                  'date_creation',
                  ]

    def create(self, validated_data):
        instance = super(ProfileAdminSerializer, self).create(validated_data)
        Specialist.objects.create(name=validated_data.get('name'),
                                  description=validated_data.get('description'),
                                  profile=instance,
                                  photo=instance.photo
                                  )
        return instance


class ProfileImagesAdminSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)

    class Meta:
        model = ProfileImages
        fields = ['id', 'profile', 'specialist', 'image', 'date_creation']
        extra_kwargs = {'profile': {'read_only': True}}


class WorkTimeAdminSerializer(serializers.ModelSerializer):
    specialist = serializers.SerializerMethodField()
    time_work = serializers.SerializerMethodField()

    def get_time_work(self, obj):
        time = obj.time_work.split('-')
        time_start = datetime.strptime(time[0], '%H:%M')
        time_end = datetime.strptime(time[-1], '%H:%M')
        time_break = obj.break_time
        if time_break:
            time_br = time_break.split('-')
            time_br_start = datetime.strptime(time_br[0], '%H:%M')
            time_br_end = datetime.strptime(time_br[-1], '%H:%M')
            time_br_start_td = timedelta(hours=time_br_start.hour, minutes=time_start.minute)
            time_br_end_td = timedelta(hours=time_br_end.hour, minutes=time_end.minute)
        result = []
        time_start_timedelta = timedelta(hours=time_start.hour, minutes=time_start.minute)
        time_end_timedelta = timedelta(hours=time_end.hour, minutes=time_end.minute)
        while time_start_timedelta <= time_end_timedelta:
            if time_break:
                if time_start_timedelta <= time_br_start_td or time_start_timedelta >= time_br_end_td:
                    result.append(str(time_start_timedelta))
            else:
                result.append(str(time_start_timedelta))
            time_start_timedelta += timedelta(hours=1)

        return result

    def get_specialist(self, obj):
        specialist = obj.specialist
        if specialist:
            return SpecialistSerializer(specialist).data
        return {}

    class Meta:
        model = WorkTime
        fields = ['id', 'specialist', 'date', 'time_work', 'break_time']


class ReviewsAdminSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    data_create = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Reviews
        fields = ['id', 'rating_star', 'user_name', 'description', 'data_create', 'active']
