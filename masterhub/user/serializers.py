from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, ProfileMaster


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def validate_password(self, data):
        validate_password(data)
        return data

    def save(self):
        return CustomUser.objects.create_user(**self.initial_data)


class ProfileMasterSerializer(ModelSerializer):

    class Meta:
        model = ProfileMaster
        fields = ['id', 'user', 'name', 'address', 'phone', 'link_vk', 'link_tg', 'description']
