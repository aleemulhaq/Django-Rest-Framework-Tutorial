import pytest

import json

from django.urls import reverse

from snippets.views import SnippetViewSet
from rest_framework.test import force_authenticate 

from django.contrib.auth.models import User

class TestSnippetApiViews():

    #Test:
    #The response status code
    #The response content
    # snippets created/remove

    '''
    Arrange: set everything needed for the test
    Mock: mock everything needed to isolate your test
    Act: trigger your code unit.
    Assert: assert the outcome is exactly as expected to avoid any unpleasant surprises later.
    '''
    
    def test_get_snippet_list(self):
        assert True
     
    @pytest.mark.django_db
    def test_user_create(self):
        User.objects.create_user('poe', 'poe@thecat.com', 'poepass')
        assert User.objects.count() == 1

    @pytest.mark.django_db
    def test_view(client):
        url = reverse('homepage-url')
        response = client.get(url)
        assert response.status_code == 200