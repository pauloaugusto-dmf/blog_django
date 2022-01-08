import pytest

from publication.models import Topic, Post
from ..factories.publication import TopicFactory
from ..factories.users import UserFactory

pytestmark = pytest.mark.django_db


class TestTopicModel:
    def test_create_topic(self):
        topic = Topic.objects.create(name="test_topic")
        assert topic.name == "test_topic"

    def test___str__(self):
        topic = Topic.objects.create(name="test_topic")
        assert str(topic) == "test_topic"


class TestPostModel:
    def test_crete_post(self):
        topic = TopicFactory()
        author = UserFactory()
        post = Post.objects.create(
            title="test post",
            topic=topic,
            author=author,
            image="teste.jpg",
            alt="imagem de teste",
            article="artigo de teste",
        )

        assert post.title == "test post"
        assert post.topic == topic
        assert post.author == author
        assert post.image == "teste.jpg"
        assert post.alt == "imagem de teste"
        assert post.article == "artigo de teste"

    def test__str__(self):
        topic = TopicFactory()
        author = UserFactory()
        post = Post.objects.create(
            title="test post",
            topic=topic,
            author=author,
            image="teste.jpg",
            alt="imagem de teste",
            article="artigo de teste",
        )

        assert str(post) == "test post"
