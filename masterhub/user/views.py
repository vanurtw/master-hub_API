from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser


# Create your views here.


class UsersAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'auth_token': token.key})
        return Response({'status': 'ne ok'})


class UsersViewSet(ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.onjects.all()


