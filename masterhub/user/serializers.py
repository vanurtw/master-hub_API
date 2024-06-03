from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, ProfileMaster, ProfileImages, Specialist
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


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['id', 'name', 'job', 'description']


class ProfileMasterSerializer(serializers.ModelSerializer):
    images_work = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    specialists = serializers.SerializerMethodField()

    def get_images_work(self, obj):
        specialization = obj.specialization
        if specialization == 'master':
            queryset = obj.profile_images.all()
        else:
            queryset = ProfileImages.objects.none()
            for specialist in obj.profile_specialist.all():
                query = specialist.profile_services.all()
                queryset = queryset.union(query)
        serializer = ProfileImagesSerializer(queryset, many=True)
        return serializer.data

    def get_services(self, obj):
        specialization = obj.specialization
        if specialization == 'master':
            queryset = obj.profile_services.all()
        else:
            queryset = Service.objects.none()
            for specialist in obj.profile_specialist.all():
                services = specialist.specialist_services.all()
                queryset = queryset.union(services)
        serializer = ServiceSerializer(queryset[:5], many=True)
        return serializer.data

    def get_specialists(self, obj):
        queryset = obj.profile_specialist.all()
        serializer = SpecialistSerializer(queryset, many=True)
        return serializer.data

    class Meta:
        model = ProfileMaster
        fields = [
            'id',
            'user',
            'name',
            'specialization',
            'address', 'phone',
            'link_vk', 'link_tg',
            'description',
            'specialists',
            'images_work',
            'services',
        ]
