from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from chess.models import ChessMatch, ChessPlayer


def test_should_return_list_of_chess_matches(
        rest_client: APIClient,
        chess_match: ChessMatch,
        other_chess_match: ChessMatch
):
    endpoint_url = reverse('chessmatch-list')

    response = rest_client.get(endpoint_url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['white_player'] == chess_match.white_player_id


def test_should_return_chess_match(rest_client: APIClient, chess_match: ChessMatch):
    endpoint_url = reverse('chessmatch-detail', args=[chess_match.id])

    response = rest_client.get(endpoint_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == chess_match.id


def test_should_create_chess_match(
        rest_client: APIClient,
        chess_player: ChessPlayer,
        other_chess_player: ChessPlayer
):
    endpoint_url = reverse('chessmatch-list')

    response = rest_client.post(
        endpoint_url,
        data={
            'start_datetime': '1990-10-10T10:10:00Z',
            'white_player': chess_player.id,
            'black_player': other_chess_player.id
        }
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert ChessMatch.objects.get(id=response.data['id']).white_player_id == chess_player.id


def test_should_update_chess_match(
        rest_client: APIClient,
        chess_match: ChessMatch,
        chess_player: ChessPlayer,
        other_chess_player: ChessPlayer
):
    endpoint_url = reverse('chessmatch-detail', args=[chess_match.id])

    response = rest_client.put(
        endpoint_url,
        data={
            'start_datetime': '1990-10-10T10:10:00Z',
            'white_player': other_chess_player.id,
            'black_player': chess_player.id
        }
    )

    assert response.status_code == status.HTTP_200_OK
    chess_match.refresh_from_db()
    assert chess_match.white_player_id == other_chess_player.id


def test_should_partially_update_chess_match(rest_client: APIClient, chess_match: ChessMatch):
    endpoint_url = reverse('chessmatch-detail', args=[chess_match.id])

    response = rest_client.patch(
        endpoint_url,
        data={
            'result': 'DRAW',
        }
    )

    assert response.status_code == status.HTTP_200_OK
    updated_match = ChessMatch.objects.get(id=chess_match.id)
    assert updated_match.white_player_id == chess_match.white_player_id
    assert updated_match.result == 'DRAW'


def test_should_reject_delete_by_non_authorized_user(rest_client: APIClient, chess_match: ChessMatch):
    endpoint_url = reverse('chessmatch-detail', args=[chess_match.id])
    response = rest_client.delete(endpoint_url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert ChessMatch.objects.filter(id=chess_match.id).exists()


def test_should_delete(auth_client: APIClient, chess_match: ChessMatch):
    endpoint_url = reverse('chessmatch-detail', args=[chess_match.id])
    response = auth_client.delete(endpoint_url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert ChessMatch.objects.filter(id=chess_match.id).exists() is False
