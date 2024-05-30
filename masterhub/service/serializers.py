from .models import Service
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id')

    class Meta:
        model = Service
        fields = ['id', 'user_id', 'title', 'description', 'price', 'photo']
