from .models import Service
from rest_framework.serializers import Serializer, ModelSerializer


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['user', 'title', 'description', 'price', 'photo']
