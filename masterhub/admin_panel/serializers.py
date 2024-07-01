from user.models import ProfileMaster
from rest_framework import serializers


class ProfileAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileMaster
        fields = ['id']