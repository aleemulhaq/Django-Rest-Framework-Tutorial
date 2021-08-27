import pytest

from django.urls import reverse
from django.contrib.auth.models import User

class TestUsers():
     
    @pytest.mark.django_db
    def test_user_create(self):
        User.objects.create_user('poe', 'poe@thecat.com', 'poepass')
        assert User.objects.count() == 1

    @pytest.mark.django_db
    def test_user_detail(self, client):
        # user = create_user(username='someone') # create_user fixture
        user = User.objects.create_user('poe', 'poe@thecat.com', 'poepass')
        url = reverse('user-detail', kwargs={'pk': user.pk})
        response = client.get(url)
        assert response.status_code == 200
        assert 'poe'.encode() in response.content