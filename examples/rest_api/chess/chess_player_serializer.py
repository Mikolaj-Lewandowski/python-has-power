from rest_framework import serializers

from chess.models import ChessPlayer


class ChessPlayerSerializer(serializers.Serializer):

    email = serializers.EmailField()
    birth_date = serializers.DateField()
    pesel = serializers.CharField(max_length=11, min_length=11)
    rodo_accepted = serializers.BooleanField()

    def create(self, validated_data: dict) -> ChessPlayer:
        return ChessPlayer.objects.create(**validated_data)

    def update(self, instance: ChessPlayer, validated_data: dict):
        instance.email = validated_data.get('email', instance.email)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.pesel = validated_data.get('pesel', instance.pesel)
        instance.rodo_accepted = validated_data.get('rodo_accepted', instance.rodo_accepted)
        instance.save()
        return instance
