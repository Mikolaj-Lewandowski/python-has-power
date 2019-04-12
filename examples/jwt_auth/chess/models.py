from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class ChessPlayer(models.Model):

    email = models.EmailField()
    birth_date = models.DateField()
    pesel = models.TextField()
    rodo_accepted = models.BooleanField()
    first_name = models.TextField(max_length=20)
    second_name = models.TextField(max_length=20, null=True)
    is_premium = models.BooleanField(default=False)


class ChessMatchResults:
    WHITE_WIN = 'WHITE_WIN'
    BLACK_WIN = 'BLACK_WIN'
    DRAW = 'DRAW'

    CHESS_MATCH_RESULTS_CHOICES = (
        (WHITE_WIN, WHITE_WIN),
        (BLACK_WIN, BLACK_WIN),
        (DRAW, DRAW),
    )


class ChessMatchAgeCategories:
    UNDER_20 = 'UNDER_20'
    UNDER_30 = 'UNDER_30'
    UNDER_40 = 'UNDER_40'
    UNDER_50 = 'UNDER_50'
    OPEN = 'OPEN'

    CHESS_MATCH_AGE_CATEGORIES_CHOICES = (
        (UNDER_20, UNDER_20),
        (UNDER_30, UNDER_30),
        (UNDER_40, UNDER_40),
        (UNDER_50, UNDER_50),
        (OPEN, OPEN),
    )


class ChessMatch(models.Model):
    start_datetime = models.DateTimeField()
    result = models.TextField(choices=ChessMatchResults.CHESS_MATCH_RESULTS_CHOICES, null=True)
    white_player = models.ForeignKey(ChessPlayer, related_name='matches_as_white', on_delete=models.CASCADE)
    black_player = models.ForeignKey(ChessPlayer, related_name='matches_as_black', on_delete=models.CASCADE)
    age_category = models.TextField(
        choices=ChessMatchAgeCategories.CHESS_MATCH_AGE_CATEGORIES_CHOICES,
        default=ChessMatchAgeCategories.OPEN,
    )


class User(AbstractUser):
    pass

