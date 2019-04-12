from rest_framework.viewsets import ModelViewSet

from chess.chess_player_serializer import ChessPlayerSerializer
from chess.models import ChessPlayer


class ChessPlayerResource(ModelViewSet):

    queryset = ChessPlayer.objects.all()
    serializer_class = ChessPlayerSerializer
