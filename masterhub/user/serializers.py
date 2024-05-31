from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, ProfileMaster, ProfileImages
from rest_framework import serializers
from service.models import Service


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def validate_password(self, data):
        validate_password(data)
        return data

    def save(self):
        return CustomUser.objects.create_user(**self.initial_data)


class ProfileImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImages
        fields = ['image']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['title', 'description', 'price', 'photo']


class ProfileMasterSerializer(serializers.ModelSerializer):
    images_work = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()

    def get_images_work(self, obj):
        queryset = obj.profile_images.all()
        serializer = ProfileImagesSerializer(queryset, many=True)
        return serializer.data

    def get_services(self, obj):
        queryset = obj.services.all()
        serializer = ServiceSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = ProfileMaster
        fields = ['id', 'user', 'name', 'address', 'phone', 'link_vk', 'link_tg', 'description', 'images_work',
                  'services']
