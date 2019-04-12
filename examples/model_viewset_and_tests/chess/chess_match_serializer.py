from rest_framework import serializers

from chess.models import ChessMatch


class ChessMatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChessMatch
        fields = '__all__'
