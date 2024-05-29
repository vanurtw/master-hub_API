from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from .models import CustomUser
from rest_framework.mixins import CreateModelMixin


# Create your views here.


class UsersViewSet(GenericViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'auth_token': token.key})

# class Test(APIView):
#     def post(self, request):
#         data = request.data
#         return Response({'a':'wad'})
