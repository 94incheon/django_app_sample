from rest_framework import status
from rest_framework.views import Response, APIView

from apps.accounts.models.user import User
from apps.accounts.api.serializers.user import UserSerializer


class UserListAPI(APIView):

    def get(self, request):
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
