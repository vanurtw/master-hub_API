from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import CategoriesSerializer
from .models import Service, Categories
from rest_framework.mixins import ListModelMixin


# Create your views here.


class CategoriesAPIView(GenericAPIView, ListModelMixin):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()

    def get(self, request):
        return self.list(request)
