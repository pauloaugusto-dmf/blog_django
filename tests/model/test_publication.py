import pytest

from publication.models import Topic

pytestmark = pytest.mark.django_db


class TestTopicModel:
    def test_create_topic(self):
        topic = Topic.objects.create( name="test_topic" )
        assert topic.name == "test_topic"
    
    def test___str__(self):
        topic = Topic.objects.create( name="test_topic" )
        assert str(topic) == "test_topic"

