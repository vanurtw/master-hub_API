from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer


# Create your views here.


class UsersAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response({'status': 'ok'})
        return Response({'status': 'ne ok'})
