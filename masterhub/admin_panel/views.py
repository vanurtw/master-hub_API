from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProfileAdminSerializer


class ProfileAdminViewSet(GenericViewSet):
    serializer_class = ProfileAdminSerializer

    @action(methods=['get'], detail=False)
    def profile(self, request):
        return Response({'a': 'a'})
