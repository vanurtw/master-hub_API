from .models import Service, Categories
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.id')

    class Meta:
        model = Service
        fields = ['id', 'user_id', 'title', 'description', 'price', 'photo']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'title', 'photo']
