import pytest

from django.urls import reverse
from django.contrib.auth.models import User

class TestAuthentication():

    @pytest.mark.django_db
    def test_auth_login(self, client):
        #user = create_user()
        user = User.objects.create_user('poe', 'poe@thecat.com', 'poepass')
        url = reverse('rest_framework:login')
        client.login(
        username=user.username, password=user.password
        )
        response = client.get(url)
        assert response.status_code == 200
