from rest_framework.serializers import ModelSerializer, Serializer

from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'specialization', 'password']
