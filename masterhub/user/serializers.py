from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'specialization', 'password']

    def validate_password(self, data):
        validate_password(data)
        return data

    def save(self):
        return CustomUser.objects.create_user(**self.initial_data)
