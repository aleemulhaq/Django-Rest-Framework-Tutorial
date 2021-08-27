import pytest
from django.urls import reverse

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

    @pytest.mark.django_db
    def test_snippet_list_url_view(self, client):
        url = reverse('snippet-list')
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_user_list_url_view(self, client):
        url = reverse('user-list')
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_user_list_url_view(self, client):
        url = reverse('user-list')
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_api_root_url_view(self, client):
        url = reverse('api-root')
        response = client.get(url)
        assert response.status_code == 200