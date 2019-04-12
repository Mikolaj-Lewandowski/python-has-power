import pytest
from rest_framework.test import APIClient


@pytest.fixture
def rest_client():
    return APIClient()

