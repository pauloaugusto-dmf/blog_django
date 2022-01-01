import pytest

from publication.models import Topic

pytestmark = pytest.mark.django_db


class TestTopicModel:
    def test_create_topic(self):
        user = Topic.objects.create(
            name="test_topic"
        )
        
        assert user.name == "test_topic"
    

