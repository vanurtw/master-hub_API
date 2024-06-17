from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from user.models import ProfileMaster, Specialist
from .models import WorkTime
from user.serializers import SpecialistSerializer
from service.models import Service, Categories
from .serializers import ServicesSerializer, ServicesRecordingSerializer, WorkTimeSerializer
from rest_framework.mixins import RetrieveModelMixin


# Create your views here.

class SpecialistRecordingAPIView(GenericViewSet, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = []
        profile = ProfileMaster.objects.get(id=pk)
        # if profile.specialization == 'master':
        #     services = Service.objects.filter(profile=profile)
        # else:
        #     services = Service.objects.none()
        #     specialists = profile.profile_specialist.all()
        #     for i in specialists:
        #         services = services.union(i.specialist_services.all())
        services = Service.objects.filter(profile=profile)
        for i in services:
            if i.category not in queryset:
                queryset.append(i.category)
        # serializer = ServicesSerializer(services, many=True)
        serializer = ServicesRecordingSerializer(queryset, many=True, context={'services': services})
        return Response(serializer.data)

    @action(methods=['get'], detail=True, url_path='(?P<id_specialist>[^/.]+)')
    def recording(self, request, *args, **kwargs):
        '''если профиль мастера то передать параметром specialization'''
        pk = kwargs.get('id_specialist')
        param = request.GET.get('specialization', None)
        if param:
            profile_work_time = WorkTime.objects.get(profile__pk=pk)
        else:
            profile_work_time = WorkTime.objects.get(specialist__pk=pk)
        # services_time

        serializer = WorkTimeSerializer(profile_work_time, context={'request': request, 'kwargs': kwargs})
        return Response(serializer.data)

    # @action(methods=['get'], detail=True)
    # def services(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     queryset = []
    #     profile = ProfileMaster.objects.get(id=pk)
    #     if profile.specialization == 'master':
    #         services = Service.objects.filter(profile=profile)
    #     else:
    #         services = Service.objects.none()
    #         specialists = profile.profile_specialist.all()
    #         for i in specialists:
    #             services = services.union(i.specialist_services.all())
    #     for i in services:
    #         if i.category not in queryset:
    #             queryset.append(i.category)
    #     # serializer = ServicesSerializer(services, many=True)
    #     serializer = ServicesRecordingSerializer(queryset, many=True, context={'services': services})
    #     return Response(serializer.data)
