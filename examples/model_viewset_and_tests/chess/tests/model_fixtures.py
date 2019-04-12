import datetime

import pytest

from chess.models import ChessPlayer, ChessMatch


@pytest.fixture
def chess_match(db, chess_player, other_chess_player):
    return ChessMatch.objects.create(
        start_datetime=datetime.datetime(year=1990, month=10, day=20),
        white_player=chess_player,
        black_player=other_chess_player
    )


@pytest.fixture
def other_chess_match(db, chess_player, other_chess_player):
    return ChessMatch.objects.create(
        start_datetime=datetime.datetime(year=1990, month=10, day=20),
        white_player=chess_player,
        black_player=other_chess_player
    )


@pytest.fixture
def chess_player(db):
    return ChessPlayer.objects.create(
        email='test-player@mailinator.com',
        birth_date=datetime.date(year=1990, month=10, day=20),
        pesel='123456789',
        first_name='John',
        rodo_accepted=True
    )


@pytest.fixture
def other_chess_player(db):
    return ChessPlayer.objects.create(
        email='test-player@mailinator.com',
        birth_date=datetime.date(year=1990, month=10, day=20),
        pesel='123456789',
        first_name='Marry',
        rodo_accepted=True
    )

