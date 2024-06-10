from .models import Service, Categories
from rest_framework import serializers
from user.models import ProfileMaster


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'title', 'photo']


class ProfileCatalogSerialize(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    def get_reviews(self, obj):
        queryset = [i.get_rating_star_display() for i in obj.reviews_profile.all()]
        len_queryset = len(queryset)
        if len_queryset==0:
            average_rating = 0
        else:
            average_rating = round(sum(queryset) / len_queryset, 2)
        data = {
            'average_rating': average_rating,
            'count': len_queryset
        }
        return data

    class Meta:
        model = ProfileMaster
        fields = ['id', 'name', 'address', 'specialization', 'reviews']
