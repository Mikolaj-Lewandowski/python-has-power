from rest_framework.viewsets import ModelViewSet

from chess.chess_match_serializer import ChessMatchSerializer
from chess.is_authenticated_for_delete import IsAuthenticatedForDelete
from chess.models import ChessMatch


class ChessMatchResource(ModelViewSet):

    permission_classes = (IsAuthenticatedForDelete, )
    queryset = ChessMatch.objects.all()
    serializer_class = ChessMatchSerializer
