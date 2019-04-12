from rest_framework.viewsets import ModelViewSet

from chess.chess_match_serializer import ChessMatchSerializer
from chess.models import ChessMatch


class ChessMatchResource(ModelViewSet):

    queryset = ChessMatch.objects.all()
    serializer_class = ChessMatchSerializer
