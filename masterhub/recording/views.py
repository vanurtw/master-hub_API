from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from user.models import ProfileMaster, Specialist
from user.serializers import SpecialistSerializer


# Create your views here.


class SpecialistRecordingAPIView(GenericViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=['get'], detail=True)
    def specialist(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        profile = get_object_or_404(ProfileMaster, pk=pk)
        specialists = profile.profile_specialist.all()
        serializer = SpecialistSerializer(specialists, many=True)
        return Response(serializer.data)

