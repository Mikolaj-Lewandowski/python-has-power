from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from chess.chess_player_serializer import ChessPlayerSerializer
from chess.models import ChessPlayer


class ChessPlayerResource(APIView):

    def get(self, request, pk=None):
        if pk is None:
            serializer = ChessPlayerSerializer(ChessPlayer.objects.all(), many=True)
        else:
            serializer = ChessPlayerSerializer(ChessPlayer.objects.get(pk=pk))
        return Response(serializer.data)

    def post(self, request):
        serializer = ChessPlayerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        chess_player = ChessPlayer.objects.get(pk=pk)
        serializer = ChessPlayerSerializer(chess_player, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, pk):
        chess_player = ChessPlayer.objects.get(pk=pk)
        serializer = ChessPlayerSerializer(chess_player, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        ChessPlayer.objects.filter(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

