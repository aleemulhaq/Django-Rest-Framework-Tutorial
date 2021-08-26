import pytest

import json

from django.urls import reverse

from snippets.views import SnippetViewSet

class TestSnippetApiViews():

    #Test:
    #The response status code
    #The response content
    # snippets created/remove
    
    def test_get_snippet_list(self):
        assert True

    def test_result_finished(self, rf):
        request = rf.get(reverse('snippetviewset'))
        response = SnippetViewSet.as_view()(request)

        assert response.status_code == 200

        content = json.loads(response.content)
        assert content['result'] == 'FINISHED'
     