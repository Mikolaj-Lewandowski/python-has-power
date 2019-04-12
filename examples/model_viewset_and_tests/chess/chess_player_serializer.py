from datetime import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from chess.chess_match_serializer import ChessMatchSerializer
from chess.models import ChessPlayer


class ChessPlayerSerializer(serializers.ModelSerializer):

    age = serializers.SerializerMethodField()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=ChessPlayer.objects.all())])
    main_name = serializers.CharField(source='first_name', read_only=True)
    matches_as_white = ChessMatchSerializer(read_only=True, many=True)
    matches_as_black = ChessMatchSerializer(read_only=True, many=True)

    class Meta:
        model = ChessPlayer
        fields = '__all__'

    def validate_pesel(self, value):
        try:
            int(value)
        except ValueError:
            raise serializers.ValidationError('Pesel must contains only digits!')
        return value

    def get_age(self, obj: ChessPlayer):
        return datetime.now().year - obj.birth_date.year
