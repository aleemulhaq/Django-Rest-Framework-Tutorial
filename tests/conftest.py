import pytest
from rest_framework.test import APIClient, APITestCase

@pytest.fixture
def api_client():
    return APIClient