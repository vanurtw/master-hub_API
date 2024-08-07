from user.models import ProfileMaster
from rest_framework import serializers


class ProfileAminSerializer(serializers.ModelSerializer):
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
