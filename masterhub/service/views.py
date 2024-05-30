from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import ServiceSerializer
from .models import Service
from rest_framework.mixins import ListModelMixin


# Create your views here.


class ServiceAPIView(GenericAPIView, ListModelMixin):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

    def get(self, request):
        return self.list(request)
