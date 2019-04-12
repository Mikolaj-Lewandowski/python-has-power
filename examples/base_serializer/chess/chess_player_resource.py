from datetime import date
from typing import List

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from chess.chess_player import ChessPlayer
from chess.chess_player_serializer import ChessPlayerSerializer

CHESS_PLAYERS: List[ChessPlayer] = [
    ChessPlayer(
        email='chess-player-1@mailinator.com',
        birth_date=date(year=1990, month=10, day=20),
        pesel='1234656789',
        rodo_accepted=True
    ),
    ChessPlayer(
        email='chess-player-2@mailinator.com',
        birth_date=date(year=1990, month=8, day=20),
        pesel='1010101010',
        rodo_accepted=True
    ),
    ChessPlayer(
        email='chess-player-3@mailinator.com',
        birth_date=date(year=1990, month=5, day=20),
        pesel='222555222',
        rodo_accepted=False
    ),
]


class ChessPlayerResource(APIView):

    def get(self, request):
        serializer = ChessPlayerSerializer(CHESS_PLAYERS, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

