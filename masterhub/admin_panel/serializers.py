from recording.serializers import SpecialistSerializer
from user.models import ProfileMaster, ProfileImages
from rest_framework import serializers
from recording.models import WorkTime


class ProfileAdminSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=False, required=False)

    class Meta:
        model = ProfileMaster
        fields = ['id',
                  'name',
                  'photo',
                  'address',
                  'phone',
                  'specialization',
                  'link_vk',
                  'link_tg',
                  'description',
                  'time_relax',
                  'date_creation'
                  ]


class ProfileImagesAdminSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)

    class Meta:
        model = ProfileImages
        fields = ['id', 'profile', 'specialist', 'image', 'date_creation']
        extra_kwargs = {'profile': {'read_only': True}}


class WorkTimeAdminSerializer(serializers.ModelSerializer):
    specialist = serializers.SerializerMethodField()

    def get_specialist(self, obj):
        specialist = obj.specialist
        if specialist:
            return SpecialistSerializer(specialist).data
        return {}

    class Meta:
        model = WorkTime
        fields = ['id', 'specialist', 'date', 'time_work', 'break_time']
