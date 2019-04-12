from rest_framework import serializers


class ChessPlayerSerializer(serializers.Serializer):

    email = serializers.EmailField()
    birth_date = serializers.DateField()
    pesel = serializers.CharField(max_length=11, min_length=11)
    rodo_accepted = serializers.BooleanField()
