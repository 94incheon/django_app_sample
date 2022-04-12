from rest_framework import status
from rest_framework.views import Response, APIView

from apps.boards.models.board import Board
from apps.boards.api.serializers.board import BoardSerializer


class BoardListAPI(APIView):

    def get(self, request):
        qs = Board.objects.all()
        serializer = BoardSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
