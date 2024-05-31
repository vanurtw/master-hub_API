from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer, ProfileMasterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from .models import CustomUser, ProfileMaster, ProfileImages
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin


# Create your views here.


class UsersViewSet(GenericViewSet, RetrieveModelMixin):

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'auth_token': token.key})

    # def retrieve(self, request, pk):
    #     return Response({'a': 'wd'})

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomUserSerializer
        return ProfileMasterSerializer

    def get_queryset(self):
        if self.action == 'create':
            return CustomUser.objects.all()
        return ProfileMaster.objects.all()

# class Test(APIView):
#     def post(self, request):
#         data = request.data
#         return Response({'a':'wad'})
