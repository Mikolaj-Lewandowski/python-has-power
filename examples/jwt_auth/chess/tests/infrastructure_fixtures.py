import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from chess.models import User


@pytest.fixture
def rest_client():
    return APIClient()


@pytest.fixture
def auth_client(user: User, rest_client: APIClient):
    token_url = reverse('token_obtain_pair')
    token_response = rest_client.post(token_url, {'username': user.username, 'password': 'test-password'}, format='json')
    token = token_response.data['access']
    rest_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    return rest_client

