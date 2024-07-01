from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProfileAdminSerializer
from rest_framework import permissions
from user.serializers import ProfileMasterSerializer
from rest_framework.mixins import CreateModelMixin


class ProfileAdminViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = ProfileAdminSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        user = request.user
        try:
            profile = user.user_profile
            serializer = ProfileAdminSerializer(profile, context={'request': request})
            return Response(serializer.data)
        except AttributeError:
            return Response({'detail': 'no profile'})

    def create(self, request, *args, **kwargs):
        serializer = ProfileAdminSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response({'detail': 'error'})
