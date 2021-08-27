import pytest

from snippets.models import Snippet

from django.contrib.auth.models import User

class TestSnippetsModel():
    
    @pytest.mark.django_db
    def test_snippet_can_be_created(self):
        Snippet.objects.create(
            title = "test_snippet",
            code = "Print(\"Testing snippet\")",
            owner = User.objects.create_user('poe', 'poe@thecat.com', 'poepass')
        )
        latest_snippet = Snippet.objects.last()
        assert latest_snippet.title == "test_snippet"
        assert latest_snippet.owner.username == "poe"

